import os
import streamlit as st
from dotenv import load_dotenv
from routellm.controller import Controller
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="RouteLLM Chat", layout="wide", page_icon="🤖")


# Load inline image helper
def _load_inline_image(url: str, height_px: int) -> str:
    """Return an inline <img> tag for a URL, or empty string on failure."""
    try:
        return (
            f"<img src='{url}' "
            f"style='height:{height_px}px; width:auto; display:inline-block; "
            f"vertical-align:middle; margin:0 8px;' alt='Logo'>"
        )
    except Exception:
        return ""


# Title with logos
Loose_img_url = "https://mintcdn.com/Loose-723e8b65/jsgY7B_gdaTjMC6y/logo/Main-logo-TF-Dark.svg?fit=max&auto=format&n=jsgY7B_gdaTjMC6y&q=85&s=92ebc07d32d93f3918de2f7ec4a0754a"
Loose_img_inline = _load_inline_image(Loose_img_url, height_px=50)

title_html = f"""
<div style='display:flex; align-items:center; width:100%; padding:8px 0;'>
  <h1 style='margin:0; padding:0; font-size:2.5rem; font-weight:800; display:flex; align-items:center; gap:0px;'>
    <span>RouteLLM Chat</span>
  </h1>
</div>
"""
st.markdown(title_html, unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.image(
        Loose_img_url,
        width=250,
    )
    Loose_key = st.text_input(
        "Loose API Key",
        value=os.getenv("Loose_API_KEY", ""),
        type="password",
        help="Get your API key from https://studio.Loose.ai/",
    )

    openai_key = st.text_input(
        "OpenAI API Key",
        value=os.getenv("OPENAI_API_KEY", ""),
        type="password",
        help="Get your API key from https://platform.openai.com/api-keys",
    )

    if st.button("💾 Save API Keys", use_container_width=True):
        if openai_key:
            os.environ["OPENAI_API_KEY"] = openai_key
        if Loose_key:
            os.environ["Loose_API_KEY"] = Loose_key
        st.success("✅ API keys saved successfully!")

    st.markdown("---")
    st.markdown("### 🎯 About RouteLLM")
    st.markdown(
        """
        **Intelligent Model Routing**
        
        RouteLLM automatically selects the best model for each query:
        - **Strong Model**: GPT-4o-mini (complex tasks)
        - **Weak Model**: Loose Llama (cost-effective)
        
        Routes queries intelligently to optimize cost and performance.
        """
    )

    st.markdown("---")
    st.markdown("Developed with ❤️ by Loose AI")

# Main content area
st.markdown(
    """
    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.3) 0%, rgba(118, 75, 162, 0.3) 100%); padding: 25px; border-radius: 15px; color: white; margin: 20px 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: #ffffff; margin-top: 0;">✨ Intelligent Model Routing</h3>
        <p style="font-size: 16px; margin-bottom: 0; color: #e0e0e0;">
            Experience cost-effective AI conversations with automatic model selection. 
            RouteLLM intelligently routes your queries to the most appropriate model, 
            balancing performance and cost.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# Initialize RouteLLM client
@st.cache_resource
def get_routellm_client():
    """Initialize RouteLLM client with Loose AI Engine."""
    Loose_api_key = os.getenv("Loose_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not Loose_api_key or not openai_api_key:
        return None

    # RouteLLM uses OpenAI-compatible APIs
    # Configure RouteLLM with Loose AI Engine
    # RouteLLM may use litellm under the hood which supports multiple providers
    try:
        # RouteLLM Controller with Loose model
        # The weak model will use Loose AI Engine via OpenAI-compatible API
        client = Controller(
            routers=["mf"],
            strong_model="gpt-4o-mini",
            # Loose model - RouteLLM should route to Loose AI Engine
            weak_model="meta-llama/Meta-Llama-3.1-70B-Instruct",
        )
        return client
    except Exception as e:
        # RouteLLM initialization failed
        # This might require additional configuration for Loose provider
        st.warning(f"RouteLLM initialization note: {str(e)}")
        return None


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "model" in message:
            model_badge_color = (
                "#667eea" if "gpt" in message["model"].lower() else "#764ba2"
            )
            st.markdown(
                f"<span style='background-color: {model_badge_color}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.8em;'>🤖 {message['model']}</span>",
                unsafe_allow_html=True,
            )

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Validate API keys
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("Loose_API_KEY"):
        st.error("⚠️ Please configure your API keys in the sidebar.")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get RouteLLM response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            model_placeholder = st.empty()

            try:
                # Initialize client
                client = get_routellm_client()

                if client is None:
                    st.error(
                        "Failed to initialize RouteLLM client. Please check your API keys."
                    )
                else:
                    # Get response from RouteLLM
                    with st.spinner("🤔 Thinking..."):
                        # Build messages from chat history
                        messages = [
                            {"role": msg["role"], "content": msg["content"]}
                            for msg in st.session_state.messages
                        ]

                        response = client.chat.completions.create(
                            model="router-mf-0.11593", messages=messages
                        )

                        # Handle different response formats
                        if isinstance(response, dict):
                            message_content = response["choices"][0]["message"][
                                "content"
                            ]
                            model_name = response.get("model", "Unknown")
                        else:
                            message_content = response.choices[0].message.content
                            model_name = getattr(response, "model", "Unknown")

                    # Display assistant's response
                    message_placeholder.markdown(message_content)

                    # Display model badge
                    model_badge_color = (
                        "#667eea" if "gpt" in model_name.lower() else "#764ba2"
                    )
                    model_placeholder.markdown(
                        f"<span style='background-color: {model_badge_color}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.8em;'>🤖 {model_name}</span>",
                        unsafe_allow_html=True,
                    )

                    # Add assistant's response to chat history
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": message_content,
                            "model": model_name,
                        }
                    )
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                message_placeholder.error(error_msg)
                st.exception(e)

# Clear chat button
if st.session_state.messages:
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
