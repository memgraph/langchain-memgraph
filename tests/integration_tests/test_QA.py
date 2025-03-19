#TODO: (@antejavor) Add a description of the file. 

import os
from langchain_memgraph.graphs.memgraph import Memgraph
from langchain_memgraph.chains.graph_qa import MemgraphQAChain

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

url = os.environ.get("MEMGRAPH_URI", "bolt://localhost:7687")
username = os.environ.get("MEMGRAPH_USERNAME", "")
password = os.environ.get("MEMGRAPH_PASSWORD", "")

graph = Memgraph(
    url=url, username=username, password=password, refresh_schema=False
)


# Creating and executing the seeding query
query = """
    MERGE (g:Game {name: "Baldur's Gate 3"})
    WITH g, ["PlayStation 5", "Mac OS", "Windows", "Xbox Series X/S"] AS platforms,
            ["Adventure", "Role-Playing Game", "Strategy"] AS genres
    FOREACH (platform IN platforms |
        MERGE (p:Platform {name: platform})
        MERGE (g)-[:AVAILABLE_ON]->(p)
    )
    FOREACH (genre IN genres |
        MERGE (gn:Genre {name: genre})
        MERGE (g)-[:HAS_GENRE]->(gn)
    )
    MERGE (p:Publisher {name: "Larian Studios"})
    MERGE (g)-[:PUBLISHED_BY]->(p);
"""
graph.query(query)

graph.refresh_schema()

print(graph.get_schema)

os.environ["OPENAI_API_KEY"] = ""


chain = MemgraphQAChain.from_llm(
    ChatOpenAI(temperature=0),
    graph=graph,
    model_name="gpt-4-turbo",
    allow_dangerous_requests=True,
)

response = chain.invoke("Which platforms is Baldur's Gate 3 available on?")
print(response["result"])