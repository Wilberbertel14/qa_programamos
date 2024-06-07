from behave import then

@then('I should see "{expected_text}" in the results')
def step_verify_search_results(context, expected_text):
    assert expected_text in context.home_page.get_search_results(), f"Expected text '{expected_text}' not found in search results."