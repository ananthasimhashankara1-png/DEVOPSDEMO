import pytest
from playwright.sync_api import Page, expect

def test_xpathlocators(page:Page):
    page.goto("https://demo.nopcommerce.com/register")
    logo=page.locator("//html[1]/body[1]/div[6]/header[1]/div[2]/div[1]/a[1]/img[1]")
    page.wait_for_timeout(5000)
    expect(logo).to_be_visible()
    logo1=page.locator("//img[@alt='nopCommerce demo store']")
    expect(logo1).to_be_visible()

    # xpath with contains
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    search_computer=page.locator("//h2/a[contains(@href,'computer')]")
    search_computer.count()
    print("computer coutn is=",search_computer.count())
    count_computer=search_computer.count() 
    expect(search_computer).to_have_count(count_computer)
    print_frist_name=search_computer.first.text_content()
    print("first computer is=",print_frist_name)
    last_item=search_computer.last.text_content()
    print("last computer is=",last_item)

    nth_item=search_computer.nth(2).text_content()
    print("nth item is=",nth_item)
     
    assert count_computer>=4

    all_title=search_computer.all_text_contents()
    print(" all teh titile ---",all_title)
    for title in all_title:
        print("title is=",title)
        if "14.1-inch Laptop" in title:
            print("title found=",title)
            title.click()
            page.wait_for_timeout(5000)
            
    page.wait_for_timeout(5000)
    search_gift_card=page.locator("//h2/a[contains(@href,'gift')]")
    count1=search_gift_card.count()
    print(search_gift_card.count())
    assert count1>=1

    search_laptop=page.locator("//h2/a[contains(@href,'laptop')]")
    search_laptop.count()
    print(search_laptop.count())

    expect(search_laptop).to_have_count(1)
