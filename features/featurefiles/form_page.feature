Feature: testing form page elements

Scenario Outline: Verify the text box element in the form page
     Given the form page is available
     When we enter the "<test_data>" to validate "<input_type>" in single line text input element
     Then it displays the values

    Examples: TestData
    | input_type       | test_data      |
    | Number           | 123            |
    | Alphabet         | a              |
    | Alphanumeric     | Orexel 123     |
    | Special Character| #              |