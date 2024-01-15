import streamlit as st
from embedchain import App
import os





askabraham = App.from_config(config_path="config.yaml")

# Load OpenAI API key from secrets.toml
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.title("💬 Ask Abraham")
st.markdown("""
    <p style="font-size: small;">
        An initiative by Tokenofme 💗 <img src="https://s3.us-west-1.amazonaws.com/soulcompass-installation.instructions/SoulcompassDashboard/launchscreenTOM.png" 
        alt="Tokenofme Logo" style="vertical-align: middle; width: 40px; height: 40px; margin-right: 5px;">
        
    </p>
    """, unsafe_allow_html=True)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
        Hi! I'm a Abraham. I can answer questions based on the knowledge I have been provided!\n
        Ask me any questions and I'll share some wisdom.
        """,
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything!"):
    

    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        msg_placeholder.markdown("Downloading some thoughts and wisdom...")
        full_response = ""

        for response in askabraham.chat(prompt):
            msg_placeholder.empty()
            full_response += response

        msg_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})