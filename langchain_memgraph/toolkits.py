"""Memgraph toolkits."""

from typing import List

from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseTool, BaseToolkit
from pydantic import ConfigDict, Field

from langchain_memgraph.graphs.memgraph import Memgraph
from langchain_memgraph.tools import (
    QueryMemgraphTool,
)


class MemgraphToolkit(BaseToolkit):
    """Memgraph toolkit for interacting with the Memgraph database.

    Setup:
        Install ``langchain-memgraph``.

        .. code-block:: bash

            pip install -U langchain-memgraph
            pip install -U neo4j # Client for Memgraph

    Key init args:
        db: MemgraphDB
            MemgraphDB database object.
        llm: BaseLanguageModel
            The language model used by the toolkit, in particular for query generation.

    Instantiate:
        .. code-block:: python

            from langchain-memgraph.toolkits import MemgraphToolkit
            from langchain-memgraph.memgraph import MemgraphDB

            toolkit = MemgraphToolkit(
                db=db,
                llm=llm,
            )
    Tools:
        .. code-block:: python

            toolkit.get_tools()

        .. code-block:: none

            QueryMemgraphTool


    """  # noqa: E501

    db: Memgraph = Field(exclude=True)
    llm: BaseLanguageModel = Field(exclude=True)

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    def get_tools(self) -> List[BaseTool]:
        """Return the list of tools in the toolkit."""
        return [
            QueryMemgraphTool(db=self.db),
        ]
