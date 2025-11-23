from pages.base_page import BasePage


# This is the class to write all elements and actions in the login page
class LoginPage(BasePage):
    USERNAME = '#user-name'
    PASSWORD = '#password'
    LOGIN_BTN = '#login-button'
    ERROR_MSG = "h3[data-test='error']"

    # Login steps: input username, input password, click login
    def login(self, username, password):
        self.page.fill(self.USERNAME,username)
        self.page.fill(self.PASSWORD,password)
        self.page.click(self.LOGIN_BTN)

    # Assert login failed message
    def assert_login_error(self, msg):
        self.assert_text(self.ERROR_MSG, msg)