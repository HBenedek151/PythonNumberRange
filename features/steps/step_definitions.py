from behave import given, when, then
from src.number_range import inRange


@given('The number is {number}')
def step_given_a_number(context, number):
    context.number = float(number)

@when("The number is in range")
def step_when_i_ask_the_number_is_in_range(context):
    context.actual_answer = inRange(context.number)

@then('I should be told "{answer}"')
def step_when_i_should_be_told(context, answer):
    assert context.actual_answer == answer