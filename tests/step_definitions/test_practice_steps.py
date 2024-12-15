from pytest_bdd import given, when, then, scenario


@scenario(r'../features/automation_practice.feature', 'Check the link is working on the page')
def test_scenario():
    pass


@given('User is on Homepage')
def i_am_on_the_practice_page():
    pass


@when('user click on the link')
def i_click_on_the_link():
    pass


@then('link text should be printed')
def i_should_be_redirected_to_the_correct_page():
    pass


@then('user should be redirected to correct link')
def i_should_see_the_correct_page_title():
    pass