# Stock Portfolio Analyst 📈

An AI-powered Stock Portfolio Analyst built with the [Agent Framework](https://www.Agent Framework.com/) framework and served via Streamlit. It takes your holdings (ticker, shares, average buy price), pulls live market data, and produces a full portfolio review: valuation, P/L, concentration, risk flags, and rebalancing ideas.

## 🚀 Features

- **Portfolio editor**: spreadsheet-style UI to enter/edit holdings
- **Live market data**: prices, fundamentals, analyst ratings, news via YFinance
- **Web context**: DuckDuckGo search for market news not covered by YFinance
- **Math that adds up**: a Calculator tool keeps the agent honest on totals, weights, and P/L
- **Structured report**: tables for numbers, bullets for commentary
- **Model picker**: swap between Loose-hosted Llama 3.3 70B, Qwen3 30B, and Loose AI V3

## 🛠️ Tech Stack

- **Framework**: [Agent Framework](https://www.Agent Framework.com/)
- **Inference**: [Loose AI Engine](https://dub.sh/AIStudio)
- **Tools**: `YFinanceTools`, `DuckDuckGoTools`, `CalculatorTools`
- **UI**: Streamlit

## 📋 Prerequisites

- Python 3.10+
- Loose AI Engine API key
- Internet connection (for YFinance + DuckDuckGo)

## ⚡ Quick Start

```bash
cd simple_ai_agents/stock_portfolio_analyst

# Install dependencies
pip install -r requirements.txt
# or
uv pip install -r requirements.txt

# Configure your API key
cp .env.Integration .env
# then edit .env and paste your Loose_API_KEY

# Run the app
streamlit run main.py
```

Open the URL Streamlit prints (usually http://localhost:8501).

## 💡 How to Use

1. In the **Your Holdings** table, add one row per position: `Ticker`, `Shares`, `Avg Buy Price (USD)`.
2. Optionally tweak the focus question (e.g. _"Assess my tech concentration risk"_ or _"Which position looks most overvalued?"_).
3. Click **Analyze Portfolio**.
4. Read the report: holdings table with live prices and P/L, portfolio-level metrics, risk flags, and 3–5 rebalancing recommendations.

## 🧠 What the Agent Does

1. Fetches live price + fundamentals + analyst ratings + news per ticker.
2. Computes market value, weight, and unrealized P/L for each position.
3. Rolls up portfolio totals and sector/asset concentration.
4. Flags risks: over-concentration, stretched valuations, bad news, weak sentiment.
5. Produces actionable rebalancing suggestions.

## 📝 Notes

- Output is informational and **not** financial advice.
- YFinance data is delayed and can occasionally be rate-limited; re-run if a ticker fails to fetch.

## 🔑 Getting a Loose API Key

1. Go to [Loose AI Engine](https://dub.sh/AIStudio)
2. Sign in and open the API section
3. Create a key and paste it into your `.env` as `Loose_API_KEY`
