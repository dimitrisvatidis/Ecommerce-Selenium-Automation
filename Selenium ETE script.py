from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    NoAlertPresentException,
    TimeoutException,
)
import string
import random
import time


def get_random_email():
    return 'user_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + '@test.com'


def get_random_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        password = ''.join(random.choices(chars, k=12))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in "!@#$%^&*" for c in password)):
            return password


def dismiss_alert(driver):
    try:
        alert = driver.switch_to.alert
        alert.dismiss()
        print('Alert Dismissed')
    except NoAlertPresentException:
        print("No alert to handle")


def accept_cookies(driver):
    try:
        driver.find_element(By.ID, 'ACCEPT-COOKIES_BUTTON-ID').click()
        print('Cookies Accepted')
    except NoSuchElementException:
        print('No Accept Cookies Button Found')

def get_random_clothing_item():
    items = ['Beanie', 'Cap', 'Hoodie', 'T-shirt', 'Jacket']
    return random.choice(items)

def get_random_greek_firstname():
    firstnames = ["Giorgos", "Maria", "Nikos", "Eleni", "Kostas"]
    return random.choice(firstnames)


def get_random_greek_lastname():
    lastnames = ["Papadopoulos", "Nikolaou", "Karagiannis", "Konstantinou", "Georgiou"]
    return random.choice(lastnames)

def get_random_greek_tech_company():
    companies = ['Intrasoft', 'SingularLogic', 'Upstream', 'Beat', 'SoftOne']
    return random.choice(companies)

def get_random_greek_street():
    streets = ['Ermou', 'Panepistimiou', 'Venizelou', 'Patision', 'Tsimiski']
    return random.choice(streets)

def get_random_greek_city():
    cities = ['Athens', 'Thessaloniki', 'Patras', 'Heraklion', 'Larissa']
    return random.choice(cities)


def get_random_greek_postal_code():
    postal_codes = ['104 31', '546 24', '262 21', '713 04', '412 21']
    return random.choice(postal_codes)

def get_random_greek_mobile():
    return "69" + ''.join(random.choices("0123456789", k=8))

def get_random_street_number():
    return str(random.randint(1, 200))

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)  # ← Set default wait time here

    try:
        start_time=time.time()
        driver.get("http://demostore.supersqa.com/")
        driver.maximize_window()
        time.sleep(2)

        accept_cookies(driver)
        dismiss_alert(driver)

        wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'My account')]"))).click()

        register(wait)

        time.sleep(2)

        get_random_item_in_cart_and_checkout(driver, wait)

        fname=get_random_greek_firstname()
        lname=get_random_greek_lastname()
        company=get_random_greek_tech_company()
        city=get_random_greek_city()
        postcode=get_random_greek_postal_code()
        phone=get_random_greek_mobile()
        street=get_random_greek_street()
        street_number = get_random_street_number()

        print(f"""
        Generated Information:
        First Name: {fname}
        Last Name: {lname}
        Company: {company}
        City: {city}
        Postal Code: {postcode}
        Phone: {phone}
        Street: {street} {street_number}
        """)

        fill_out_form(city, company, fname, lname, phone, postcode, street, street_number, wait)

        time.sleep(1)

        wait.until(EC.element_to_be_clickable((By.ID,'place_order'))).click()
        time.sleep(2)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Home')]"))).click()


        time.sleep(2)
        end_time=time.time()
        duration = end_time-start_time
        print(f'Script ran successfully, runtime: {duration:.2f} seconds')
    finally:
        driver.quit()


def fill_out_form(city, company, fname, lname, phone, postcode, street, street_number, wait):
    wait.until(EC.presence_of_element_located((By.ID, 'billing_first_name'))).send_keys(fname)
    wait.until(EC.presence_of_element_located((By.ID, 'billing_last_name'))).send_keys(lname)
    wait.until(EC.presence_of_element_located((By.ID, 'billing_company'))).send_keys(company)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='selection']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']"))).send_keys(
        'Greece' + Keys.RETURN)
    wait.until(EC.presence_of_element_located((By.ID, 'billing_address_1'))).send_keys(street + ' ' + street_number)
    wait.until(EC.presence_of_element_located((By.ID, 'billing_city'))).send_keys(city)
    wait.until(EC.presence_of_element_located((By.ID, 'billing_postcode'))).send_keys(postcode)
    wait.until(EC.presence_of_element_located((By.ID, 'billing_phone'))).send_keys(phone)


def get_random_item_in_cart_and_checkout(driver, wait):
    item = get_random_clothing_item()
    print('Item generated: ' + item)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'search-field')]"))).send_keys(item + Keys.RETURN)

    try:
        grid = driver.find_element(By.XPATH, "//ul[contains(@class,'products')]")
        products = grid.find_elements(By.XPATH, ".//li[contains(@class,'product')]")
        random.choice(products).click()
    except NoSuchElementException:
        print('No results returned, script ended')

    time.sleep(1)

    try:
        select_element = Select(driver.find_element(By.ID, 'pa_color'))
        options = select_element.options
        if options:
            random_choice = random.choice(options[1:])
            select_element.select_by_visible_text(random_choice.text)
            print(f"Selected color: {random_choice.text}")
    except NoSuchElementException:
        print("Color selection not available.")

    time.sleep(1)

    try:
        size_select = Select(driver.find_element(By.ID, 'pa_size'))
        size_options = size_select.options
        if len(size_options) > 1:
            random_size = random.choice(size_options[1:])
            size_select.select_by_visible_text(random_size.text)
            print(f"Selected size: {random_size.text}")
        else:
            print("Only placeholder option found in size dropdown.")
    except NoSuchElementException:
        print("No size option available.")


    try:
        logo_select = Select(driver.find_element(By.ID, 'logo'))
        logo_options = logo_select.options
        if len(logo_options) > 1:
            random_logo = random.choice(logo_options[1:])
            logo_select.select_by_visible_text(random_logo.text)
            print(f"Selected logo option: {random_logo.text}")
        else:
            print("Only placeholder option found in logo dropdown.")
    except NoSuchElementException:
        print("No logo option available.")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'cart-contents')]"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'checkout-button')]"))).click()
    time.sleep(2)


def register(wait):
    email = get_random_email()
    password = get_random_password()
    print('Email generated: ' + email + ' Password generated: ' + password)
    wait.until(EC.presence_of_element_located((By.ID, 'reg_email'))).send_keys(email)
    wait.until(EC.presence_of_element_located((By.ID, 'reg_password'))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.NAME, 'register'))).click()


if __name__ == "__main__":
    main()