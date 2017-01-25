__author__ = 'i5'


class Textbox(object):

    def __init__(self,driver):
        self.driver =driver

    def send_textbox_values(self, input_type, test_data):
        # entering the data in the text boxes
        self.input_type = input_type
        self.driver.find_element_by_name('first_name').clear()
        self.driver.find_element_by_name('last_name').clear()
        self.driver.find_element_by_name('first_name').send_keys(test_data)
        self.driver.find_element_by_name('last_name').send_keys(test_data)

    def check_get_textbox_values(self):
        # accessing the data entered in the text boxes
        self.driver.implicitly_wait(30)
        firstbox = self.driver.find_element_by_name('first_name').get_attribute('value')
        secondbox = self.driver.find_element_by_name('last_name').get_attribute('value')
        return firstbox, secondbox

    def validate_textbox(self):
        # checking the text boxes
        self.firstTextBox, self.secondTextBox = self.check_get_textbox_values()

        # validating the test outcome
        if self.input_type == "Alphabet" and not (self.firstTextBox == "1a" and self.secondTextBox == "a"):
            return "Textbox Testing Failed - Alphabet"
        elif self.input_type == "Number" and not (self.firstTextBox == "123" and self.secondTextBox == "1234"):
            return "Textbox Testing Failed - Number"
        elif self.input_type == "Alphanumeric" and not (
                self.firstTextBox == "Orexel 123" and self.secondTextBox == "Orexel 123"):
            return "Textbox Testing Failed - Alphanumeric"
        elif self.input_type == "Special Character" and not (
                        self.firstTextBox == "#" and self.secondTextBox == "#"):
            return "Textbox Testing Failed - Special Character"
        else:
            return "Textbox Testing Passed " + self.input_type
