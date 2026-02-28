import time

from playwright.sync_api import Playwright, expect


def test_playwrightBasics(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("//input[@id='username']").fill("rahulsheetyacademy")
    page.locator("//input[@id='password']").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox").click()
    page.locator("//input[@id='signInBtn']").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    title_name = page.title()
    print(title_name)
    url= page.url
    print(url)

    time.sleep(5)





