from langchain.utilities import SQLDatabase
import agent_config


def get_db():
    return SQLDatabase.from_uri(agent_config.DATABASE_URI)
