
from dotenv import load_dotenv

load_dotenv()

from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import FunctionAgent

def multiply(a: int, b: int) -> int:
  return a * b


def divide(a: int, b: int) -> float:
  return a / b


from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import FunctionAgent

llm = OpenAI(model="gpt-4o")

workflow = FunctionAgent(
    tools=[multiply, divide],
    llm=llm,
    system_prompt="You are an agent that can perform basic mathematical operations using tools.",
)


async def main():
    #response = await workflow.run(user_msg="What is 20+(2*4)?")
    response = await workflow.run(user_msg="What is (121*12)/4?")
    print(response)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())


