"""Test Memgraph embeddings."""

from typing import Type

from langchain_memgraph.embeddings import MemgraphEmbeddings
from langchain_tests.integration_tests import EmbeddingsIntegrationTests


class TestParrotLinkEmbeddingsIntegration(EmbeddingsIntegrationTests):
    @property
    def embeddings_class(self) -> Type[MemgraphEmbeddings]:
        return MemgraphEmbeddings

    @property
    def embedding_model_params(self) -> dict:
        return {"model": "nest-embed-001"}
