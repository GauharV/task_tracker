import asyncio
from behave import given, when, then
from playwright.async_api import async_playwright

def run(context, coro):
    if not hasattr(context, '_loop') or context._loop.is_closed():
        context._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(context._loop)
    return context._loop.run_until_complete(coro)

@given('the user navigates to "{url}"')
def step_navigate(context, url):
    async def _go():
        context._pw = await async_playwright().start()
        context._browser = await context._pw.chromium.launch(headless=True)
        context._page = await context._browser.new_page()
        await context._page.goto(url)
    run(context, _go())

@given("the user is on the task list page")
def step_on_page(context):
    run(context, context._page.wait_for_selector("#task-list"))

@when('the user adds a task "{task_title}"')
def step_add_task(context, task_title):
    async def _add():
        await context._page.fill("#task-input", task_title)
        await context._page.click("#add-btn")
    run(context, _add())

@when("the user submits an empty task")
def step_empty_task(context):
    async def _empty():
        await context._page.fill("#task-input", "")
        await context._page.click("#add-btn")
    run(context, _empty())

@then('the task list should contain "{task_title}"')
def step_check_list(context, task_title):
    async def _check():
        await context._page.wait_for_selector("#task-list")
        list_text = await context._page.text_content("#task-list")
        assert task_title in list_text, \
            f"Expected '{task_title}' in list but got: {list_text}"
    run(context, _check())

@then('an error message "{message}" should be displayed')
def step_check_error(context, message):
    async def _check():
        await context._page.wait_for_selector("#error-msg")
        error_text = await context._page.text_content("#error-msg")
        assert message in error_text, \
            f"Expected error '{message}' but got: {error_text}"
    run(context, _check())