**----------- SauceDemo E-commerce Automation (Pytest BDD)  ----------**

This project is a web automation framework built with Python, Playwright, and Pytest-BDD to test the core flows of the SauceDemo e-commerce website. It adheres strictly to the Page Object Model (POM) for maximum maintainability.

**Tech Stack:**
(1) Automation: Playwright (Python)
(2) Framework: Pytest
(3) Test Style: Pytest-BDD (Gherkin syntax)
(4) Reporting: Allure Report
(5) Design: Page Object Model (POM)

**Quick Setup:**
1. Clone the Repository: 
  git clone https://github.com/buyunli1997/Playwright-E-commerce-Automation-Practice.git
  cd playwright-sauce-automation

2. Install Dependencies:
  pip install -r requirements.txt

3. Install Playwright Browser Binaries:
   playwright install

4. Running Tests:
   All tests are run via pytest. The default setting runs on Chromium.

   (1) Execute All Tests: pytest
   (2) The framework supports BDD tags (@smoke, @regression, @critical, @data_driven): pytest -m [marker]

5. Viewing Reports (Allure)
   Go to the reports folder > allure-report-[timestamp] folder > index.html > Open it in a browser
