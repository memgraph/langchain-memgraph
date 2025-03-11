# langchain-memgraph

This package contains the LangChain integration with Memgraph

## Installation

```bash
pip install -U langchain-memgraph
```

And you should configure credentials by setting the following environment variables:

* TODO: fill this out

## Chat Models

`ChatMemgraph` class exposes chat models from Memgraph.

```python
from langchain_memgraph import ChatMemgraph

llm = ChatMemgraph()
llm.invoke("Sing a ballad of LangChain.")
```

## Embeddings

`MemgraphEmbeddings` class exposes embeddings from Memgraph.

```python
from langchain_memgraph import MemgraphEmbeddings

embeddings = MemgraphEmbeddings()
embeddings.embed_query("What is the meaning of life?")
```

## LLMs
`MemgraphLLM` class exposes LLMs from Memgraph.

```python
from langchain_memgraph import MemgraphLLM

llm = MemgraphLLM()
llm.invoke("The meaning of life is")
```
