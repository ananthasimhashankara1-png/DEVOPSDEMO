from playwright.sync_api import Page
from playwright.sync_api import expect




async def test_verifypageurl(page:Page):
    page.goto("http://www.automationpractice.pl/index.php") # passing the url
    myurl=page.url()
   
    expect(myurl).to_have_url("http://www.automationpractice.pl/index.php") # expected url and assertion


async def test_verify_pagetitle(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")
   
    expect(page).to_have_url("http://www.automationpractice.pl/index.php")
    page_title=page.title
    expect(page_title).to_have_title("My Shop")
    


