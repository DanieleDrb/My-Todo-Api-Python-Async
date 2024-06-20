
from playwright.async_api import async_playwright
from config import BASE_URL

async def fetch_todos():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        try:
            response = await page.goto(BASE_URL)
            assert response.status == 200, "Failed to fetch todos"
            todos = await response.json()
            return todos

        finally:
            await browser.close()

async def create_todo(new_todo):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        try:
            response = await page.request.post(BASE_URL, data=new_todo)
            assert response.status == 201, "Failed to create todo"
            todo = await response.json()
            return todo

        finally:
            await browser.close()

async def update_todo(todo_id, updated_data):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        try:
            response = await page.request.put(f"{BASE_URL}/{todo_id}", data=updated_data)
            assert response.status == 200, "Failed to update todo"
            updated_todo = await response.json()
            return updated_todo

        finally:
            await browser.close()

async def delete_todo(todo_id):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        try:
            response = await page.request.delete(f"{BASE_URL}/{todo_id}")
            assert response.status == 200, "Failed to delete todo"
            return response.status == 200

        finally:
            await browser.close()
