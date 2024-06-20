import asyncio
from api_utils import create_todo, delete_todo

async def test_delete_todo():
    new_todo = {
        "title": "Learn Playwright"
    }
    created_todo = await create_todo(new_todo)

    delete_status = await delete_todo(created_todo['id'])
    print(f"Deleted todo status: {delete_status}")

# Entry point
if __name__ == "__main__":
    asyncio.run(test_delete_todo())
