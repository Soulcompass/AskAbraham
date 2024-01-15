import os
from embedchain import Pipeline as App
import streamlit as st
from embedchain.config import ChunkerConfig, AddConfig

# Load OpenAI API key from secrets.toml
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Create an Embedchain app
askabraham = App.from_config(config_path="config.yaml")

# Add your PDF data source
askabraham.add('combined_transcripts.pdf')
