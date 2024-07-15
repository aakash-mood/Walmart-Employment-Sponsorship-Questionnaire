from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

def fill_form(driver):
    # Define a dictionary with label texts and their corresponding input values
    field_data = {
        "First Name": "<Enter your first name>",
        "Last Name": "<Enter your last name>",
        "E-mail Address": "<Enter your email address>",
        "What is your country of birth?": "<Enter your country of birth>",
        "In what country do you currently reside?": "<Enter the country you currently reside in>",
        "Do you have a degree from a university, college, or vocational school": "<Enter Yes or No>",
        "What is your country(ies) of citizenship?": "<Enter your country(ies) of citizenship>",
        "What is your highest level of degree attained?": "<Enter your highest level of degree>",
        "Do you currently hold an EAD card?": "<Enter Yes or No>",
        "Select your EAD type": "<Enter your EAD type (e.g., F-1 OPT)>",
        "Please provide the following information on your current status: Visa Status type or work authorization status: Select all that apply.": ["<Enter your visa status type(s)>"],
        "Expiration date of your current status:": "<Enter the expiration date of your current status (MM/DD/YYYY)>",
        "Additional details surrounding U.S. work authorization:": "<Enter additional details regarding your U.S. work authorization>",
        "Have you previously held H1-B status in the last 6 years?": "<Enter Yes or No>",
        "Total time spent in H1-B status in the last 6 years?": "<Enter total time in H1-B status>",
        "Have you been in L-1 status?": "<Enter Yes or No>",
        "Are you currently employed?": "<Enter Yes or No>",
        "Has your previous employer filed an I-140 or immigrant petition on your behalf?": "<Enter Yes or No>",
        "Has an I-485 or Adjustment of Status application been filed on your behalf?": "<Enter Yes or No>",
        "Have you previously held J-1 status?": "<Enter Yes or No>",
        "If Yes, what was your field of study?": "<Enter your field of study>",
        "EAD Card expiration date:": "<Enter your EAD card expiration date (MM/DD/YYYY)>",
        "If no, date you became unemployed?": "<Enter the date you became unemployed (MM/DD/YYYY)>",
        "If you have an H-1B visa, is it CAP exempt? How do I know if I’m CAP Exempt:  If you obtained your H-1B through a University or related non-profit entity, non-profit or government research organization without being subject to the H-1B lottery, your visa is likely CAP exempt. Please confirm with your employer, as your H-1B would not be transferrable.": "<Enter Yes or No>"
    }


    try:
        # Iterate over the field data dictionary and fill the form
        for label_text, input_value in field_data.items():
            try:
                if isinstance(input_value, list):
                    for item in input_value:
                        checkbox_label = driver.find_element(By.XPATH, f"//label[text()='{item}']")
                        checkbox_input_id = checkbox_label.get_attribute("for")
                        checkbox = driver.find_element(By.ID, checkbox_input_id)
                        if not checkbox.is_selected():
                            driver.execute_script("arguments[0].click();", checkbox)
                else:
                    if "H-1B visa" in label_text:
                        label = driver.find_element(By.XPATH, f"//label[contains(text(), 'H-1B visa')]")
                    else:
                        label = driver.find_element(By.XPATH, f"//label[contains(text(), '{label_text}')]")
                    input_id = label.get_attribute("for")
                    input_element = driver.find_element(By.ID, input_id)

                    if input_element.tag_name in ["textarea", "input"]:
                        input_element.clear()
                        input_element.send_keys(input_value)
                    elif input_element.tag_name == "div":
                        if label_text == "Select your EAD type":
                            driver.execute_script("arguments[0].click();", input_element)  # Use JavaScript to click
                            time.sleep(1)  # Wait for the dropdown options to be visible
                            option_element = driver.find_element(By.XPATH, f"//div[text()='{input_value}']")
                            driver.execute_script("arguments[0].click();", option_element)  # Use JavaScript to click
                        else:
                            input_element.send_keys(input_value)
            except NoSuchElementException:
                print(f"Element not found for: {label_text}")
            time.sleep(1)
        time.sleep(60)
        try:
            ok_button = driver.find_element(By.XPATH, "//button[@data-automation-id='wd-CommandButton_uic_okButton' and @title='OK']")
            driver.execute_script("arguments[0].click();", ok_button)
            print("Clicked OK button")
        except NoSuchElementException:
            print("OK button not found")
    except NoSuchElementException as e:
        print(f"An error occurred while filling the form: {e}")
    except ElementClickInterceptedException as e:
        print(f"An error occurred while clicking the element: {e}")
