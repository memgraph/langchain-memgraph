## TODO (@antejavor) Add this test to a pytest abstraction. 
import getpass
import os
from langgraph.prebuilt import create_react_agent


if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model

llm = init_chat_model("gpt-4o-mini", model_provider="openai")


from langchain_memgraph import MemgraphToolkit
from langchain_memgraph.memgraph import Memgraph


db = Memgraph(url="bolt://localhost:7687", username= "", password="")

toolkit = MemgraphToolkit(
    db=db,
    llm=llm,
)


tools = toolkit.get_tools()

print(tools)


agent_executor = create_react_agent(llm, toolkit.get_tools(), prompt="You will get a cypher query, try to execute it on the Memgraph database.")


example_query = "MATCH (n) WHERE n.name = 'Jon Snow' RETURN n"

events = agent_executor.stream(
    {"messages": [("user", example_query)]},
    stream_mode="values",
)
for event in events:
    event["messages"][-1].pretty_print()