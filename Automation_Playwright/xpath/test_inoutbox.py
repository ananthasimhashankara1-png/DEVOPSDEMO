import pytest
from playwright.sync_api import Page, expect


def test_inoutbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)
    input_name=page.locator("#name")

    expect(input_name).to_be_visible()
    expect(input_name).to_be_enabled()
    input_name.fill("ananthasimha")
    page.wait_for_timeout(5000)
    name_placeholder=input_name.get_attribute("placeholder")
    print("placeholder is=",name_placeholder)
    assert name_placeholder=="Enter Name"
    input_email=page.locator("#email")
    expect(input_email).to_be_visible()
    expect(input_email).to_be_enabled()
    page.wait_for_timeout(5000)
    emai_palceholsder=input_email.get_attribute("placeholder")
    print("email place holder is =",emai_palceholsder)
    assert emai_palceholsder=="Enter EMail"
    input_email.fill("ananthasimha@exapple.com")
    page.wait_for_timeout(50000)
    male_radio=page.locator("//input[@id='male']")
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()
    expect(male_radio).not_to_be_checked()
    page.wait_for_timeout(5000)
    male_radio.check()
    page.wait_for_timeout(5000)
    female_radio=page.locator("//input[@id='female']")
    expect(female_radio).to_be_visible()
    expect(female_radio).to_be_enabled()
    expect(female_radio).not_to_be_checked()
   
    page.wait_for_timeout(5000)
    female_radio.check()
    page.wait_for_timeout(5000)
    expect(female_radio).to_be_checked()
