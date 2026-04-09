# environment.py
# Behave runs these functions automatically before/after tests.
# You do NOT need to call these yourself.

def after_scenario(context, scenario):
    """Close the browser after every scenario (pass or fail)."""
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()

def before_scenario(context, scenario):
    """Print the scenario name — helps you see which test is running."""
    print(f"\n▶ Running: {scenario.name}")
