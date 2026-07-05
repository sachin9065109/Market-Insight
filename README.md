# 🚀 InsightIQ AI
### AI-Powered Financial Market Intelligence Platform

InsightIQ AI is a modern financial intelligence platform that combines Large Language Models (LLMs), real-time market data, and AI agents to provide investors with conversational stock market analysis and actionable insights.

Built using **FastAPI**, **React**, **LangChain**, **LangGraph**, and **OpenAI**, the platform enables users to interact with financial data using natural language while delivering real-time analytics powered by Yahoo Finance.

---

## ✨ Features

- 🤖 AI-powered conversational financial assistant
- 📈 Real-time stock market analysis
- 💹 Live stock price tracking
- 📊 Historical market data visualization
- 📑 Financial statement analysis
  - Balance Sheet
  - Income Statement
  - Cash Flow Statement
- 🏢 Company profile and business overview
- 📌 Financial ratios and valuation metrics
- 💰 Dividend and stock split history
- 👥 Institutional and insider ownership analysis
- 🧠 AI-generated investment insights
- 📋 Analyst recommendations
- 🔍 Company ticker symbol lookup
- ⚡ Streaming AI responses
- 🌙 Responsive modern UI

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
          React Frontend
                  │
                  ▼
           FastAPI Backend
                  │
      ┌───────────┴────────────┐
      │                        │
      ▼                        ▼
 LangGraph Agent         Yahoo Finance API
      │
      ▼
 LangChain Tools
      │
      ▼
 OpenAI GPT Models
      │
      ▼
 AI Generated Financial Insights
```

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- LangChain
- LangGraph
- OpenAI API
- Yahoo Finance (yfinance)
- Langfuse

## Frontend

- React
- TypeScript
- Vite
- CSS

## Deployment

- Render (Backend)
- Vercel (Frontend)

---

# 📂 Project Structure

```
InsightIQ/
│
├── components/
│   ├── agent.py
│   └── utils/
│
├── config/
│   └── config.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
│
├── main.py
├── requirements.txt
├── render.yaml
├── pyproject.toml
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/InsightIQ.git

cd InsightIQ
```

---

## Backend Setup

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENAI_API_KEY=your_api_key
LANGFUSE_SECRET_KEY=your_key
LANGFUSE_PUBLIC_KEY=your_key
```

Run the backend

```bash
python main.py
```

Backend runs at

```
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# 📡 API Capabilities

InsightIQ AI provides multiple AI-powered financial tools including:

| Capability | Description |
|------------|-------------|
| Stock Price | Live market prices |
| Historical Data | Market trends |
| Company Information | Business profile |
| Financial Statements | Balance Sheet, Income Statement, Cash Flow |
| Financial Ratios | P/E, EPS, ROE, etc. |
| Dividend History | Historical dividends |
| Stock Splits | Split information |
| Shareholders | Institutional ownership |
| Insider Transactions | Insider trading data |
| Analyst Ratings | Buy/Hold/Sell recommendations |
| Company News | Latest financial news |
| Ticker Search | Company symbol lookup |

---

# 📈 AI Workflow

```
User Query

      │

      ▼

FastAPI API

      │

      ▼

LangGraph Agent

      │

      ▼

Tool Selection

      │

      ▼

Yahoo Finance

      │

      ▼

OpenAI GPT

      │

      ▼

AI Generated Response
```

---

# 📷 Screenshots

> Add application screenshots here.

```
Home Page

Dashboard

Stock Analysis

Financial Report

AI Chat
```

---

# 🔥 Future Improvements

- Portfolio Tracking
- Watchlist Management
- Technical Indicators
- Candlestick Charts
- Authentication
- PDF Report Generation
- AI Investment Recommendations
- News Sentiment Analysis
- Dark Mode
- Multi-language Support

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a feature branch

3. Commit your changes

4. Push to GitHub

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sachin Kumar**

AI • Machine Learning • Full Stack Development

GitHub: https://github.com/sachin9065109

LinkedIn: www.linkedin.com/in/sachin-bhagat-b3ab06353

---

## ⭐ If you found this project useful, consider giving it a star.
