from assertpy import assert_that
from behave import *

use_step_matcher("re")


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given("User '(?P<name>.+)' as admin")
def implementaion(context, name):
    context.login = name
    print(f"user {name}")


@when("Add additional user '(?P<name>.*)'")
def second_user(context, name):
    context.second_name = name
    print(f"added name {name}")
    return name


@then("Compare Users names (?P<amount>\d+)")
def some_name_(context, amount):
    assert_that(context.login).is_not_none()
