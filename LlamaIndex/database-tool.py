import os
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
# Import and initialize our tool spec
from llama_index.tools.database.base import DatabaseToolSpec

db_spec = DatabaseToolSpec(
    scheme="postgresql",  # Database Scheme
    host="localhost",  # Database Host
    port="5432",  # Database Port
    user="postgres",  # Database User
    password="x",  # Database Password
    dbname="your_db",  # Database Name
)

tools = db_spec.to_tool_list()
for tool in tools:
    print(tool.metadata.name)
    print(tool.metadata.description)
    print(tool.metadata.fn_schema)

agent = FunctionAgent(
    tools=db_tools.to_tool_list(),
    llm=OpenAI(model="gpt-4.1"),
)

# Context to store chat history
from llama_index.core.workflow import Context
ctx = Context(agent)

print(await agent.run("What tables does this database contain", ctx=ctx))
print(await agent.run("Can you describe the messages table", ctx=ctx))
print(await agent.run("Fetch the most recent message and display the body", ctx=ctx))


