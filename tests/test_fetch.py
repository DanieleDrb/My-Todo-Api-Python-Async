import asyncio
from api_utils import fetch_todos

async def test_fetch_todos():
    todos = await fetch_todos()
    print(f"Fetched todos: {todos}")

# Entry point
if __name__ == "__main__":
    asyncio.run(test_fetch_todos())
