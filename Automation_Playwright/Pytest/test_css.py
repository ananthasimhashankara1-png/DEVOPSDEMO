from playwright.sync_api import Page,expect
import pytest

def test_cssloactors(page:Page):

    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    # tag and id
    page.locator("input#small-searchterms").fill("laptop")

    page.wait_for_timeout(5000)

    # tag and class
    page.locator("input[value='Search']").click()

