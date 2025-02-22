import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tempmail import TempMail

# Setup Selenium options for headless browsing
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Generate random Name, Gender, DOB, Password
names = ["John", "Mike", "Alice", "Sara"]
gender = random.choice(["Male", "Female"])
dob = f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1990, 2003)}"
password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))

# Fetch TempMail address
tempmail = TempMail()
email = tempmail.get_email_address()

# Navigate to Facebook and fill out the form
driver.get("https://www.facebook.com/r.php")
time.sleep(2)

driver.find_element("name", "firstname").send_keys(random.choice(names))
driver.find_element("name", "lastname").send_keys(random.choice(names))
driver.find_element("name", "reg_email__").send_keys(email)
driver.find_element("name", "reg_passwd__").send_keys(password)
driver.find_element("name", "birthday_day").send_keys(dob.split("/")[0])
driver.find_element("name", "birthday_month").send_keys(dob.split("/")[1])
driver.find_element("name", "birthday_year").send_keys(dob.split("/")[2])

if gender == "Male":
    driver.find_element("name", "sex").click()

# Manually solve CAPTCHA (user interaction needed)
print("Please solve CAPTCHA manually and press Enter to continue.")
input("Press Enter after CAPTCHA is solved...")

# Once CAPTCHA is solved, submit form
driver.find_element("name", "websubmit").click()
time.sleep(3)

# Check if the account was created successfully
print(f"Temp Email: {email}")
print(f"Password: {password}")

# Close driver
driver.quit()
