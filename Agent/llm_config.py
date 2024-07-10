from langchain.llms import OpenAI
from langchain.agents import create_sql_agent
import agent_config
import os

os.environ["OPENAI_API_KEY"] = agent_config.OPENAI_API_KEY


def configure_llm():
    return OpenAI(
        temperature=0, verbose=True, openai_api_key=agent_config.OPENAI_API_KEY
    )
