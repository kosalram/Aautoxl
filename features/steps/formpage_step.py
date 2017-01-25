__author__ = 'i5'
from textBox import Textbox
from behave import given, when, then

testcase_count = 0


# SCENARIO 1 - Verify the text boxes in the form tab

@given('the form page is available')
def step_impl(context):
    # prepare the text boxes to accept the data
    context.textbox = Textbox(context.driver)
    print('The form page is available for testing')


@when('we enter the "{test_data}" to validate "{input_type}" in single line text input element')
def step_impl(context, test_data, input_type):
    # pass the test data to the text boxes
    context.textbox.send_textbox_values(input_type, test_data)
    print('The values are entered')


@then('it displays the values')
def step_impl(context):
    # validate the contents of the text boxes
    context.test_result = context.textbox.validate_textbox()
    print(context.test_result)

    global testcase_count
    testcase_count += 1

    # Take a screenshot of the page
    context.driver.save_screenshot(
        context.screenservloc + context.step.name + str(testcase_count) + ".jpg")
    print('The test results are displayed')