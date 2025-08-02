from re import VERBOSE
from langchain.docstore.wikipedia import Wikipedia
from langchain.agents import Tool
from langchain.agents.react.base import DocstoreExplorer

docstore = DocstoreExplorer(Wikipedia())
tools = [
    Tool(
        name="Search",
        func=docstore.search,
        description="docstore에서 용어를 검색하세요",
    ),
    Tool(
        name="Lookup",
        func=docstore.lookup,
        description="docstore에서 용어 검색."
    )
]

react = initialize_agent(
    tools= tools,
    llm=llm,
    agent=AgentType.REACT_DOCSTORE,
    handle_parsing_errors=True,
    max_iterations=1,
    max_execution_time=1,
    verbose=True,
)

def query_data(query):
  try:
    response = react.invoke(query)
    print("--------------------------", response)
    return response
  except Exception as e:
    print(f"Error: {e}")
    raise


query = "밍크 선인장 키우는 방법은?"
response = query_data(query)
print(response['output'])
