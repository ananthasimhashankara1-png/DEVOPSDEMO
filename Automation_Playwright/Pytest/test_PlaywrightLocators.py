from playwright.sync_api import Page
from playwright.sync_api import expect



# def test_verify_altText(page: Page):
#     page.goto("http://www.automationpractice.pl/index.php")
#     page.wait_for_timeout(5000)
#     # Verify page title
#     title = page.title()
#     expect(page).to_have_title("My Shop")   # or whatever the actual title is
    
#     # Verify image alt text
# def test_verify_altText1(page: Page):
#     page.wait_for_timeout(5000)
#     img_text = page.get_by_alt_text("My Shop")
#     expect(img_text).to_be_visible()
#     # img2_text=page.get_by_alt_text("Faded Short Sleeve T-shirts")
#     # expect(img2_text).to_be_visible()

#     # verify the get_by_text
# def test_verify_Text(page: Page):
#     page.goto("http://www.automationpractice.pl/index.php")

#     page.wait_for_timeout(5000)
#     text_cart=page.get_by_text("Sign in")
#     expect(text_cart).to_be_visible()
#     # verify the get_by_role
#     validte_women=page.get_by_role("link", name="Contact us")

#     expect(validte_women).to_be_visible()

def test_verify_byplscefolder(page:Page):
    page.goto("http://www.automationpractice.pl/index.php?id_category=8&controller=category")
    page.wait_for_timeout(5000)
    ispresent=page.get_by_placeholder("Search")
    ispresent.fill("newjerssy")
    page.wait_for_timeout(5000)

    # verify the get by label
def test_verify_label(page: Page):
    page.goto("https://demo.nopcommerce.com/register")
    page.wait_for_timeout(5000)
    page.get_by_label("First name:").fill("ananthasimha")
    page.get_by_label("Last name:").fill("shankara")
    page.get_by_label("Email:").fill("Email@abc.com")
    page.wait_for_timeout(5000)


def test_verifyby_title(page:Page):
    page.goto("http://www.automationpractice.pl/index.php?id_category=8&controller=category")
    page.wait_for_timeout(5000)
    verify_bt_title=page.get_by_title("View my shopping cart")
    expect(verify_bt_title).to_be_visible()
    page.wait_for_timeout(5000)



