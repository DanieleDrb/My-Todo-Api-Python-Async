import asyncio
from api_utils import update_todo, create_todo

async def test_update_todo():
    new_todo = {
        "title": "Learn Playwright"
    }
    created_todo = await create_todo(new_todo)

    updated_data = {
        "title": "Learn Playwright and Async",
        "completed": True
    }
    updated_todo = await update_todo(created_todo['id'], updated_data)
    print(f"Updated todo: {updated_todo}")

# Entry point
if __name__ == "__main__":
    asyncio.run(test_update_todo())
