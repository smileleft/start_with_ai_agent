import os
from langchain import hub
from langchain.agents import AgentExecutor, create_self_ask_with_search_agent
from langchain_community.tools.tavily_search import TavilyAnswer

os.environ["TAVILY_API_KEY"] = "{your tavily api key}"

tools = [TavilyAnswer(max_result=5, name="Intermediate Answer")]

prompt = hub.pull("hwchase17/self-ask-with-search")

agent = create_self_ask_with_search_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    handle_parsing_errors=True
)

agent_executor.invoke({"input": "AI Agent를 세 문장으로 설명해 줘"})
