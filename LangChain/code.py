import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, load_tools, AgentType

os.environ["OPENAI_API_KEY"] = "{your openai api key}"

llm = ChatOpenAI(model="gpt-4o-2024-11-20")



tools = load_tools(["wikipedia", "llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True
)

agent.invoke("소나무를 옮겨심기 좋은 계절은?")
