# /// script
# dependencies = [
#   "pydantic-settings",
#   "pydantic-ai-slim[openai,web]",
#   "uvicorn",
# ]
# ///

from __future__ import annotations

import uvicorn
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    INFOMANIAK_AI_TOKEN: str
    INFOMANIAK_PROJECT_ID: str
    INFOMANIAK_MODEL: str


load_dotenv()
s = _Settings()


model = OpenAIChatModel(
    s.INFOMANIAK_MODEL,
    provider=OpenAIProvider(
        api_key=s.INFOMANIAK_AI_TOKEN,
        base_url=f"https://api.infomaniak.com/2/ai/{s.INFOMANIAK_PROJECT_ID}/openai/v1",
    ),
)
agent = Agent(
    model,
    system_prompt="",
)


uvicorn.run(
    agent.to_web(),
    port=8000,
    log_level="info",
    reload=False,
)
