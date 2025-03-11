from importlib import metadata

from langchain_memgraph.chat_models import ChatMemgraph
from langchain_memgraph.document_loaders import MemgraphLoader
from langchain_memgraph.embeddings import MemgraphEmbeddings
from langchain_memgraph.retrievers import MemgraphRetriever
from langchain_memgraph.toolkits import MemgraphToolkit
from langchain_memgraph.tools import MemgraphTool
from langchain_memgraph.vectorstores import MemgraphVectorStore

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)

__all__ = [
    "ChatMemgraph",
    "MemgraphVectorStore",
    "MemgraphEmbeddings",
    "MemgraphLoader",
    "MemgraphRetriever",
    "MemgraphToolkit",
    "MemgraphTool",
    "__version__",
]
