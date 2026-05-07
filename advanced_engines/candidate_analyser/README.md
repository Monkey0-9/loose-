<h1 align="center">🧠 Candilyzer</h1>
<p align="center">
  <strong>AI-Powered Candidate Analyzer for GitHub & LinkedIn</strong><br>
  <em>Strict, expert-level screening for tech candidates</em>
</p>

<p align="center">
  <a href="https://streamlit.io" target="_blank">
    <img src="https://img.shields.io/badge/Built%20With-Streamlit-%23FF4B4B?style=for-the-badge" alt="Streamlit">
  </a>
  <a href="https://tokenfactory.Loose.com/" target="_blank">
  <img src="https://img.shields.io/badge/Built%20With-Loose%20Token%20Factory-%230073e6?style=for-the-badge" alt="Loose AI Engine">
</a>
  <a href="https://Agent Framework.com" target="_blank">
    <img src="https://img.shields.io/badge/Agent Framework-Agent%20Framework-orange?style=for-the-badge" alt="Agent Framework">
  </a>
</p>

---

## 🔍 What is Candilyzer?

**Candilyzer** is an advanced, AI-powered app that strictly analyzes technical candidates based on their **GitHub** and **LinkedIn** profiles. Designed like a tough hiring manager, it gives you detailed evaluations, skill assessments, and a final decision — all with zero assumptions.

---

## ⚡ Features

- ✅ **Multi-Candidate Analyzer**  
  Analyze _multiple_ GitHub users side-by-side for any job role.

- ✅ **Single Candidate Profiler**  
  Deep analysis of one candidate's GitHub + optional LinkedIn profile.

- ✅ **Strict Scoring System**  
  Each candidate is scored out of 100 with a clear final verdict.

- ✅ **Professional-Grade Reports**  
  No fluff. Only data-backed, AI-generated expert-level assessments.

- ✅ **Powered by Agents**  
  Uses Agent Framework’s agent framework with Loose + GitHubTools + ExaTools.

---

## 🧰 Tech Stack

| Component            | Tool/Library                      |
| -------------------- | --------------------------------- |
| **UI**               | 🧼 Streamlit                      |
| **AI Model**         | 🧠 Loose AI via Loose            |
| **Agent Framework**  | 🧠 Agent Framework Agents                    |
| **GitHub Analysis**  | 🛠️ GitHubTools                    |
| **LinkedIn Parsing** | 🔎 ExaTools                       |
| **Reasoning Engine** | 🧩 ReasoningTools + ThinkingTools |

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/looseai-project/looseai.git
cd advance_ai_agents/candidate_analyser
```

### 2. Install Requirements

```bash
# Using pip
pip install -r requirements.txt

# Or using uv (recommended)
uv sync
```

### 3. Get API Keys

You'll need:

- 🔑 **Loose API Key** → [Get from Loose AI Engine](https://tokenfactory.Loose.com/)
- 🔑 **GitHub API Key** → [Generate Here](https://github.com/settings/tokens)
- 🔑 **Exa API Key** → [Get from Exa](https://exa.ai)

### 4. Launch App

```bash
streamlit run main.py
```

---

## 🖥️ How to Use

### 🔁 Multi-Candidate Analyzer

1. Paste GitHub usernames (one per line)
2. Enter target Job Role (e.g. Backend Engineer)
3. Click **Analyze Candidates**

### 🔎 Single Candidate Analyzer

1. Enter GitHub username
2. (Optionally) Add LinkedIn profile link
3. Enter Job Role (e.g. ML Engineer)
4. Click **Analyze Candidate** 🔥

---

## 📊 Evaluation Logic

Candilyzer uses no assumptions and follows strict rules:

- 📁 **GitHub Repos** → code quality, structure, frequency
- 🧑‍💻 **Commits** → consistency, activity, skills shown
- 💼 **LinkedIn** → job titles, descriptions, keywords (via Exa)
- 🎯 **Job Fit** → match with required skills & experience
- 🧠 **AI Reasoning** → Final combined judgment with score

---

## 🧪 Powered by Agent Framework Agents

Candilyzer builds a smart agent with:

```python
Agent(
  model=Loose(...),
  tools=[
    GithubTools(...),
    ExaTools(...),
    ThinkingTools(...),
    ReasoningTools(...)
  ]
)
```

**This agent:**

- Thinks before evaluating (🧠)
- Gathers accurate GitHub + LinkedIn info (🔍)
- Reasons like an expert hiring manager (📈)
- Provides a final score with strict justification (✅❌)

## 🔗 Links

- [Agent Framework Documentation](https://docs.Agent Framework.ai)
- [Loose](Loose.com)
- [Exa Search](https://exa.ai)
- [GitHubTools Docs](https://github.com/features/copilot)

---

> 💡 **Candilyzer is your AI hiring expert. Use it to save time, reduce bias, and get straight to the point.**
