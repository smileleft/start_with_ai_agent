from langchain.memory import ConversationBufferMemory

tools = load_tools(["llm-math"], llm=llm)
memory = ConversationBufferMemory(memory_key="chat_history")

conversation_agent = initialize_agent(
    agent='conversational-react-description',
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    memory=memory,
)
conversation_agent.invoke("에드 시런은 누구이며, 2025년 현재 나이는 몇 살이야?")
