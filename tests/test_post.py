import asyncio
from api_utils import create_todo

async def test_create_todo():
    new_todo = {
        "title": "Learn Playwright with Python!!!"
    }
    created_todo = await create_todo(new_todo)
    print(f"Created todo: {created_todo}")

# Entry point
if __name__ == "__main__":
    asyncio.run(test_create_todo())
