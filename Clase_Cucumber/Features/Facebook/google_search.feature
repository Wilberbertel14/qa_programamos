Feature: Google Search

Scenario: Search for 'Facebook'
  Given I open Google homepage
  When I search for "Facebook"
  Then I should see "Facebook - Log In or Sign Up" in the results