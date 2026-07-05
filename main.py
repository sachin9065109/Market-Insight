import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain_core.messages import SystemMessage, HumanMessage
from langfuse import Langfuse

from config.config import RequestObject
from MarketInsight.components.agent import agent
from MarketInsight.utils.logger import get_logger

logger = get_logger(__name__)

STOCK_ANALYST_PROMPT = (
    "You are a professional stock market analyst. For every user query, first determine "
    "whether a relevant tool can provide accurate or real-time data. If an appropriate "
    "tool exists, you must use it before answering. If the user does not provide an exact "
    "stock ticker, use the available tool to identify or resolve the correct ticker when "
    "required. Only when no suitable tool applies should you respond using your own "
    "reasoning and general market knowledge. Never guess, assume, or fabricate any financial data."
)

langfuse_client = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

app = FastAPI(
    title="MarketInsight Agent API",
    description="Streaming API for an AI-powered stock market analyst.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("ALLOWED_ORIGINS", "*")], 
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Monitoring"])
async def health_check():
    """Health check endpoint for deployment orchestration and monitoring."""
    return {"status": "healthy", "service": "MarketInsight"}


async def _stream_agent_response(prompt_content: str, thread_id: str):
    """
    Generator function isolated from the route. Handles the LangChain 
    streaming logic and Langfuse tracing.
    """
    agent_config = {'configurable': {'thread_id': thread_id}}
    messages = [
        SystemMessage(content=STOCK_ANALYST_PROMPT),
        HumanMessage(content=prompt_content)
    ]
    
    try:
        with langfuse_client.start_as_current_observation(
            as_type="span", 
            name="chat_request_span",
            input=prompt_content,
            metadata={"user_id": thread_id}
        ) as span:
            
            with langfuse_client.start_as_current_observation(
                as_type="generation",
                name="agent_stream",
                model="agentic-workflow",
                input=prompt_content
            ) as generation:
                
                full_response = ""
                
                for token, _ in agent.stream(
                    {'messages': messages},
                    stream_mode='messages',
                    config=agent_config
                ):
                    if token.content:
                        full_response += token.content
                        yield token.content
                
                generation.update(output=full_response)
            
            span.update(output="Stream completed successfully")
            
    except Exception as e:
        logger.error(f"Streaming error for thread {thread_id}: {str(e)}", exc_info=True)
        yield "\n\
