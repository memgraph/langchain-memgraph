#TODO(@antejavor): Implement this as part of pytest abstraction.

import os
from langchain_memgraph.graphs.memgraph import Memgraph
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI


text = """
    Charles Robert Darwin was an English naturalist, geologist, and biologist,
    widely known for his contributions to evolutionary biology. His proposition that
    all species of life have descended from a common ancestor is now generally
    accepted and considered a fundamental scientific concept. In a joint
    publication with Alfred Russel Wallace, he introduced his scientific theory that
    this branching pattern of evolution resulted from a process he called natural
    selection, in which the struggle for existence has a similar effect to the
    artificial selection involved in selective breeding. Darwin has been
    described as one of the most influential figures in human history and was
    honoured by burial in Westminster Abbey.
"""

url = os.environ.get("MEMGRAPH_URI", "bolt://localhost:7687")
username = os.environ.get("MEMGRAPH_USERNAME", "")
password = os.environ.get("MEMGRAPH_PASSWORD", "")

graph = Memgraph(
    url=url, username=username, password=password, refresh_schema=False
)

os.environ["OPENAI_API_KEY"] = ""
llm = ChatOpenAI(temperature=0, model_name="gpt-4-turbo")
llm_transformer = LLMGraphTransformer(llm=llm)
documents = [Document(page_content=text)]
graph_documents = llm_transformer.convert_to_graph_documents(documents)


print(graph_documents)


graph.add_graph_documents(graph_documents)

