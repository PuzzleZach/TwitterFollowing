import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# CSV will have Name, Desc, URL
contacts =[]
urls = []

# Open a list of all our followers
with open("following.txt") as file:
    for line in file:
        urls.append(line.strip())

# Selenium options for headless Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
options = ChromeOptions()
options.add_argument("--headless")

def get_contact(url):
    # Open Chrome up
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    original_size = driver.get_window_size()
    driver.get(url)
    time.sleep(2.5)
    # First off we need to get the users name
    name = driver.title
    name = name.replace(" / Twitter", "")
    raw_names = name.split(" ")[:-1]
    name = "".join(raw_names) # This should get rid of the last item (the parenthesis)

    # Now find the user description
    found_desc = ""
    try:
        desc = driver.find_element(By.XPATH, "//div[@data-testid='UserDescription']")
        found_desc = desc.text
    except:
        found_desc = "No Description"
    # Finding the user URL with a try/except since not everyone has one
    found_url = ""
    try:
        user_url = driver.find_element(By.XPATH, "//a[@data-testid='UserUrl']")
        found_url = user_url.text
    except:
        found_url = "None"

    tmp = [name, found_desc, found_url]
    contacts.append(tmp)

    # Click our button to remove the text box
    try:
        button = driver.find_element(By.XPATH, "//span[contains(text(), 'No, thanks')]")
        button.click()
    except:
        holder = "" #ignoring, we'll just get a screenshot and see what happens
    # Save screenshot
    screenshot_name = name.strip() + "_screenshot.png"
    driver.save_screenshot(screenshot_name)
    # Close our driver
    driver.close()
    driver.quit()

for i in range(len(urls)):
    if i % 50 == 0:
        print(i)
    get_contact(urls[i])

with open("Contacts.csv", "wb") as tfile:
    tfile.write(b"Name, Description, URL\n")
    for item in contacts:
        for i, v in enumerate(item):
            # Modifying the data for CSV format
            remove_newline = v.replace("\n", "")
            remove_comma = remove_newline.replace(",", " ")
            tfile.write(remove_comma.encode("utf-8"))
            # Add a comma except at the end
            if i < len(item):
                tfile.write(b",")
        # Start our new line
        tfile.write(b"\n")
