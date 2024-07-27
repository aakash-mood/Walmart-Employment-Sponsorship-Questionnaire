# Walmart-Employment-Sponsorship-Questionnaire
To automate answering the questionnaire on the provided Walmart Workday page, you can use Selenium to interact with the page elements. Here's a basic Python script to get you started:
  1. Install Selenium:
     pip install selenium
     pip install undetected-chromedriver
     
  2. Enable Remote Debugging in Chrome:
     Start Chrome with remote debugging enabled: & "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\<YourUserName>\chrome_devtools"

  3. Set Up WebDriver:
     Ensure you have the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
  4. Make necessary changes in form_filler.py (fill your answers)
  5. Run main.py

Note: Make sure you login to career portal after starting the chrome (after step 2)
