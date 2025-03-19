## Test setup 

1. Start Memgraph in the background. 
2. Create and .env file that points to Memgraph and OpenAI API
```
MEMGRAPH_URI=bolt://localhost:7687
MEMGRAPH_USERNAME=
MEMGRAPH_PASSWORD=
OPENAI_API_KEY=your_openai_api_key
```
3. Start the tests

```
poetry run pytest --asyncio-mode=auto tests/integration_tests
```
