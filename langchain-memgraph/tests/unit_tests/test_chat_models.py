"""Test chat model integration."""

from typing import Type

from langchain_memgraph.chat_models import ChatMemgraph
from langchain_tests.unit_tests import ChatModelUnitTests


class TestChatMemgraphUnit(ChatModelUnitTests):
    @property
    def chat_model_class(self) -> Type[ChatMemgraph]:
        return ChatMemgraph

    @property
    def chat_model_params(self) -> dict:
        # These should be parameters used to initialize your integration for testing
        return {
            "model": "bird-brain-001",
            "temperature": 0,
            "parrot_buffer_length": 50,
        }
