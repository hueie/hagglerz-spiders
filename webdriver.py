from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()  # can be webdriver.PhantomJS()
browser.get('https://www.woolworths.com.au/shop/browse/specials/half-price')
#browser.get('https://www.woolworths.com.au/shop/browse/specials/half-price/bakery')
# wait for the select element to become visible
#page = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.selectedFilters-count")))
page = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.tileList-tiles")))
item_list_element = page.find_elements_by_css_selector(".shelfProductTile-content")
#36
for div_element in item_list_element:
    print(div_element)
    title = div_element.find_element_by_class_name("shelfProductTile-descriptionLink")
    print(title.text)
    try:
        priceDollars = div_element.find_element_by_class_name("price-dollars")
        priceCents = div_element.find_element_by_class_name("price-cents")
        wasPrice = div_element.find_element_by_class_name("shelfProductTile-wasPrice")
        print(priceDollars.text)
        print(priceCents.text)
        print(wasPrice.text)
    except NoSuchElementException:
        print("OUT OF STOCK")

    #select = Select(select_element)
    #for option in select.options[1:]:
    #    print(option.text)

    # browser.quit()