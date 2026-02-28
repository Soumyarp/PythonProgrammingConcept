import time

from playwright.sync_api import Page, expect


def test_amazon_Cart(page:Page):
    page.goto("https://www.amazon.in/")

    # page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.hover("//div[@class='nav-div']//a[contains(text(),'Mobiles')]")
    page.click("//div[@class='nav-div']//a[contains(text(),'Mobiles')]")
    time.sleep(5)
    page.get_by_placeholder("Search Amazon.in").fill("Samsung mobile")
    time.sleep(5)
    page.keyboard.press("Enter")
    time.sleep(5)
    Galaxy_S26_5G=page.locator("div[role='listitem'][data-component-type='s-search-result']").filter(has_text="Galaxy S26 5G")
    Galaxy_S26_5G.locator("text=Add to Cart").click()
    time.sleep(5)
    page.evaluate("window.scrollTo(0,0)")
    page.locator("//a[@id='nav-cart']").click()
    time.sleep(5)
    expect(page.locator("div[role='listitem']")).to_have_count(1)
    time.sleep(5)


