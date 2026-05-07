import streamlit as st
import os
import time
import json

CATEGORIES = [
    "Core_ai_agents", "simple_ai_agents", "mcp_ai_agents",
    "memory_agents", "rag_apps", "advance_ai_agents"
]
st.set_page_config(
    page_title="Loose AI | Developer Showcase",
    page_icon="🚀",
    layout="wide"
)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    .stApp {
        background: radial-gradient(
            circle at 15% 50%, rgba(99, 102, 241, 0.12), transparent 25%
        ),
        radial-gradient(
            circle at 85% 30%, rgba(168, 85, 247, 0.12), transparent 25%
        ),
        #020617 !important;
        font-family: 'Outfit', sans-serif;
    }
    
    /* Hide top header bar */
    header {visibility: hidden;}
    
    /* Typography */
    h1, h2, h3, h4, p, span, div {
        font-family: 'Outfit', sans-serif !important;
    }
    
    h1 {
        background: linear-gradient(135deg, #818cf8 0%, #c084fc 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        letter-spacing: -2px;
        font-size: 3.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Glassmorphism Cards */
    .card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 32px;
        padding: 2.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(
            90deg, transparent, rgba(255,255,255,0.15), transparent
        );
    }
    
    .card:hover {
        transform: translateY(-8px) scale(1.01);
        box-shadow: 0 20px 60px rgba(99, 102, 241, 0.15);
        border: 1px solid rgba(99, 102, 241, 0.25);
    }
    
    /* System Pulse Animation */
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(99, 102, 241, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(99, 102, 241, 0); }
    }
    
    .pulse-dot {
        width: 10px;
        height: 10px;
        background: #6366f1;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
        animation: pulse 2s infinite;
    }
    
    /* Animated Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1, #a855f7) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 3rem !important;
        border-radius: 16px !important;
        font-weight: 700 !important;
        letter-spacing: 1px;
        transition: all 0.4s ease !important;
        box-shadow: 0 10px 20px rgba(99, 102, 241, 0.2) !important;
        text-transform: uppercase;
        font-size: 0.9rem !important;
    }
    
    .stButton>button:hover {
        transform: scale(1.05) translateY(-3px) !important;
        box-shadow: 0 15px 30px rgba(168, 85, 247, 0.3) !important;
        background: linear-gradient(135deg, #818cf8, #c084fc) !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #010409 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image(
        "https://placehold.co/400x100/1e1b4b/818cf8?text=LOOSE+AI",
        use_container_width=True
    )
    st.markdown("---")
    st.markdown(
        '### <span class="pulse-dot"></span> System Pulse',
        unsafe_allow_html=True
    )
    st.markdown("### 🛠️ Active Agents")
    st.info("Finance Agent: ONLINE")
    st.info("Tech Analyst: ONLINE")
    st.info("MCP Agent: ONLINE")
    st.markdown("---")
    st.success("Mode: MOCK (Ready for Demo)")

# Header
st.title("🚀 Loose AI Developer Showcase")
st.markdown("#### The ultimate modular platform for autonomous AI agents.")

# Health Dashboard (New)
if os.path.exists("health_report.json"):
    with open("health_report.json", "r") as f:
        health_data = json.load(f)
    
    with st.sidebar:
        st.markdown("### 🏥 System Health")
        total = health_data["total_agents"]
        healthy = sum(c["healthy"] for c in health_data["categories"].values())
        st.progress(healthy / total)
        st.write(f"**{healthy}/{total}** Agents Verified")
        
    with st.expander("🏥 Global Health Dashboard"):
        cols = st.columns(len(CATEGORIES))
        for i, cat in enumerate(CATEGORIES):
            cat_data = health_data["categories"][cat]
            with cols[i]:
                st.metric(
                    cat.split('_')[0].title(),
                    f"{cat_data['healthy']}/{cat_data['total']}",
                    delta=f"{cat_data['healthy'] - cat_data['total']}"
                )
else:
    st.warning("⚠️ No health report found. Run `python verify_health.py` to generate one.")

# Comprehensive Developer Experience & Polyglot Core
st.markdown("---")
st.header("💎 Comprehensive Developer Experience")

p_col1, p_col2, p_col3 = st.columns(3)
with p_col1:
    st.markdown("""
    ### 🌐 Polyglot Core
    High-performance modules in:
    - **Go**: Parallel Auditing
    - **Rust**: Secure Compute
    - **TypeScript**: Eco-Monitoring
    """)

with p_col2:
    st.markdown("""
    ### 🏥 Health Guard
    - **99%** System Integrity
    - **Automated** Audits
    - **Zero-Error** Readiness
    """)

with p_col3:
    st.markdown("""
    ### 🛠️ Advanced Tooling
    - **Comprehensive CLI** Dashboard
    - **Fail-Safe** Mock Layer
    - **AI Discovery** Agent
    """)

st.info("💡 **Tip**: Run `python cli/loose_cli.py dashboard` for the high-fidelity terminal experience.")
st.markdown("---")

# Repository Explorer (New)
with st.expander("📂 Repository Explorer & Agent Discovery", expanded=True):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    CATEGORIES = [
        "Core_ai_agents", "simple_ai_agents", "mcp_ai_agents",
        "memory_agents", "rag_apps", "advance_ai_agents"
    ]
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        cat_select = st.selectbox("Select Category:", CATEGORIES)
    
    # List agents in category
    agent_dirs = [
        d for d in os.listdir(cat_select)
        if os.path.isdir(os.path.join(cat_select, d))
        and not d.startswith("__")
    ]
    
    with col_b:
        agent_select = st.selectbox("Select Agent to Explore:", sorted(agent_dirs))
    
    if agent_select:
        agent_path = os.path.join(cat_select, agent_select)
        readme_path = os.path.join(agent_path, "README.md")
        
        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown(f"### 📄 {agent_select.replace('_', ' ').title()}")
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as f:
                    st.markdown("\n".join(f.readlines()[:10]) + "...")
            else:
                st.write("No README available for this agent.")
        
        with c2:
            st.markdown("### ⚡ Quick Action")
            if st.button(f"Launch {agent_select} Sandbox"):
                st.session_state.sandbox_agent = agent_select
                st.session_state.sandbox_category = cat_select
                st.success(f"Loaded {agent_select} into Sandbox below!")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("💹 Finance Agent")
    st.write("Analyze stocks and market trends using Loose AI Engine.")
    f_q = st.text_input(
        "Ask Finance Agent:",
        placeholder="Compare NVIDIA and AMD stock"
    )
    if st.button("Query Finance Agent"):
        with st.spinner("Processing with Loose AI..."):
            time.sleep(1.5)
            st.markdown("""
            | Metric | NVIDIA (NVDA) | AMD (AMD) |
            | :--- | :--- | :--- |
            | **Price** | $145.20 | $162.10 |
            | **Market Cap** | $3.2T | $260B |
            
            **Insights:**
            - NVDA continues to dominate AI training.
            - AMD is gaining share in inference.
            """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📰 Tech News Analyst")
    st.write("Real-time HackerNews analysis and trend discovery.")
    hn_q = st.text_input(
        "Ask Tech Analyst:",
        placeholder="What's trending in LLMs today?"
    )
    if st.button("Analyze News"):
        with st.spinner("Scanning HackerNews..."):
            time.sleep(1.2)
            st.markdown("""
            ### 🔥 Trending Topics
            1. **Agentic Frameworks**: Discussion on agno framework.
            2. **Loose AI Launch**: Community excited about modular agents.
            """)
    st.markdown('</div>', unsafe_allow_html=True)

# Agent Sandbox (New)
if 'sandbox_agent' in st.session_state:
    st.markdown(
        '<div class="card" style="border: 1px solid #818cf8;">',
        unsafe_allow_html=True
    )
    st.header(f"🛠️ Sandbox: {st.session_state.sandbox_agent}")
    
    agent_name = st.session_state.sandbox_agent
    cat_name = st.session_state.sandbox_category
    
    st.write(f"Env: **Mock Mode** | Category: `{cat_name}`")
    
    u_i = st.text_area(
        "Interact:",
        placeholder=f"Enter instructions for {agent_name}..."
    )
    
    if st.button("Run in Sandbox"):
        with st.spinner(f"Agent {agent_name} is thinking..."):
            time.sleep(2)
            st.code(
                f"Executed {agent_name} in mock mode.\n"
                f"Output: [MOCK_RESULT_FOR_{agent_name.upper()}]",
                language="bash"
            )
    
    if st.button("Clear Sandbox"):
        del st.session_state.sandbox_agent
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "© 2026 Loose AI Project | [GitHub](https://github.com/looseai-project)"
)
