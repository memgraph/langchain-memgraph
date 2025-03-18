# langchain-memgraph

This package contains the LangChain integration with [Memgraph](https://memgraph.com/)

## Installation

```bash
pip install -U langchain-memgraph
```

Make sure Memgraph is running, during initialization of a Memgraph, pass the
proper `url`, `username` and `password` if it is set. 

Here is an example:
```python
db = Memgraph("bolt://localhost:7687", "", "")
```


