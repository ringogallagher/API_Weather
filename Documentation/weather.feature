Feature: Weather Forecast Web Application
  As a user
  I want to see the current weather and 5-day forecast for my location
  So that I can plan my activities based on upcoming weather conditions

  Background:
    Given the API_Weather web application is running
    And I have access to the main page

  Scenario: View weather automatically detected by IP
    Given I open the main weather page
    When the system detects my location via IP
    Then I should see the current temperature, condition, and city name
    And I should see a 5-day weather forecast
    And the interface should show weather animations

  Scenario: View weather in selected language
    Given I am on the weather page
    When I select language "Russian"
    And the system fetches weather data in Russian
    Then I should see weather conditions and dates in Russian language

  Scenario: Handle invalid weather API response
    Given the weather API service is unavailable
    When I request weather data
    Then I should see an error message "Service temporarily unavailable"
    And no broken data should be displayed

  Scenario: Handle invalid user input
    Given I send an invalid request without JSON body
    When the system processes my request
    Then I should receive a "400 Bad Request" response
    And the response should include an error message "Invalid request: JSON body required"

  Scenario: Test forecast data integrity
    Given I request weather data for my IP
    When the system returns the forecast
    Then each forecast day should include
      | date | condition | avg_temp | min_temp | max_temp | rain |
