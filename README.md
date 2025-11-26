<h1> SauceDemo E-commerce Automation (Pytest BDD) </h1>

<h2> Summary: </h2>
This project is a web automation framework built with Python, Playwright, and Pytest-BDD to test the core flows of the SauceDemo e-commerce website. It adheres strictly to the Page Object Model (POM) for maximum maintainability.

<h2> Tech Stack: </h2>
(1) Automation: Playwright (Python) <br>
(2) Framework: Pytest <br>
(3) Test Style: Pytest-BDD (Gherkin syntax) <br>
(4) Reporting: Allure Report <br>
(5) Design: Page Object Model (POM) <br>

<h2> Quick Setup: </h2>
<h3> 1. Clone the Repository: </h3>
  git clone https://github.com/buyunli1997/Playwright-E-commerce-Automation-Practice.git <br>
  cd playwright-sauce-automation <br>

<h3> 2. Install Dependencies: </h3>
  pip install -r requirements.txt

<h3> 3. Install Playwright Browser Binaries: </h3>
   playwright install

<h3> 4. Running Tests: </h3>
   All tests are run via pytest. The default setting runs on Chromium. <br>
   (1) Execute All Tests: pytest <br>
   (2) The framework supports BDD tags (@smoke, @regression, @critical, @data_driven): pytest -m [marker] <br>

<h3> 5. Viewing Reports (Allure) : </h3>
   Go to the reports folder > allure-report-[timestamp] folder > index.html > Open it in a browser
