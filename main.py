from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException, StaleElementReferenceException
import time
from form_filler import fill_form

# Connect to the existing Chrome session
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)

def click_start_buttons(driver):
    # Get all "Start" buttons
    start_buttons = driver.find_elements(By.XPATH, "//a[@data-automation-id='taskButton' and text()='Start']")
    return start_buttons

try:
    # Open the webpage
    driver.get('https://walmart.wd5.myworkdayjobs.com/en-US/WalmartExternal/userHome')

    # Wait for the page to load completely
    time.sleep(5)

    # Process tasks until no more "Start" buttons are found
    while True:
        start_buttons = click_start_buttons(driver)
        if not start_buttons:
            break
        
        # Iterate over each "Start" button
        for index in range(len(start_buttons)):
            try:
                # Retry logic to handle stale element reference
                for _ in range(3):  # Retry up to 3 times
                    try:
                        # Re-fetch the "Start" button to avoid stale element reference
                        start_buttons = click_start_buttons(driver)
                        if index >= len(start_buttons):
                            break
                        button = start_buttons[index]
                        # Click on the "Start" button
                        driver.execute_script("arguments[0].click();", button)
                        time.sleep(5)  # Wait for the task page to load

                        # Fill the form
                        fill_form(driver)

                        # Navigate back to the task list
                        driver.get('https://walmart.wd5.myworkdayjobs.com/en-US/WalmartExternal/userHome')
                        time.sleep(5)  # Wait for the page to load

                        break  # Break the retry loop if successful
                    except StaleElementReferenceException:
                        print(f"Retrying due to stale element reference for task {index + 1}")
                else:
                    continue  # If retry loop did not break, continue to next iteration

            except TimeoutException:
                print(f"Timeout while processing task {index + 1}")

    print("All tasks processed.")

    # Pause the script to keep the browser open
    input("Press Enter to close the browser...")

except Exception as e:
    print(f"An error occurred while initializing the WebDriver: {e}")

finally:
    # Close the WebDriver
    driver.quit()
