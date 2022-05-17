import pytest


@pytest.mark.usefixtures("driver")
def test_add_to_cart(driver):
    driver.get('https://www.google.co.in/')
    driver.implicitly_wait(10)
    if not "Google" in driver.title:
        raise Exception("Are you not on google? How come!")
    elem = driver.find_element_by_name("q")
    elem.send_keys("Browserstack")
    elem.submit()
    driver.implicitly_wait(10)
    print(driver.title)



@pytest.mark.usefixtures("driver")
def test_add_two_to_cart(driver):
     driver.get('https://www.google.co.in/')
     driver.implicitly_wait(10)
     if not "Google" in driver.title:
        raise Exception("Are you not on google? How come!")
     elem = driver.find_element_by_name("q")
     elem.send_keys("Browserstack")
     elem.submit()
     driver.implicitly_wait(10)
     print(driver.title)
