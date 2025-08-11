import os, asyncio
import dotenv
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
# Import and initialize our tool spec
from llama_index.tools.database.base import DatabaseToolSpec

load_dotenv()
db_spec = DatabaseToolSpec(
    scheme=os.env["DB_SCHEMA"],
    host=os.env["DB_HOST"],
    port=os.env["DB_PORT"],  # Database Port
    user=os.env["DB_USER"],  # Database User
    password=os.env["DB_PASSWORD"],  # Database Password
    dbname=os.env["DB_NAME"],  # Database Name
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

async def main():
    print(await agent.run("What tables does this database contain", ctx=ctx))
    print(await agent.run("Can you describe the messages table", ctx=ctx))
    print(await agent.run("Fetch the most recent message and display the body", ctx=ctx))


if __name__ == "__main__":
    asyncio.run(main())


