import requests
import allure
import pytest
import time


@allure.feature('Network Behavior')
@allure.suite('Response Delay Tests')
@allure.title('Handle Delayed Response')
@allure.description('This test verifies that the system can handle a delayed response correctly.')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
def test_delayed_response():

    headers = {'Content-Type': 'application/json'}

    start_time = time.time()

    response = requests.get(
        "https://reqres.in/api/users?delay=4",
        headers=headers
    )

    end_time = time.time()

    response_data = response.json()

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    with allure.step('Verify response contains "page"'):
        assert 'page' in response_data, 'Page information is missing in response'

    with allure.step('Verify response contains "data"'):
        assert 'data' in response_data, 'Data information is missing in response'

    with allure.step('Verify response data contains at least one user'):
        assert len(response_data['data']) > 0, 'No user data found in response'

    # Optional: Verify that the delay is approximately as expected (4 seconds)
    delay_duration = end_time - start_time
    with allure.step('Verify response delay is approximately 4 seconds'):
        assert 2.5 < delay_duration < 5, f'Delay was {delay_duration:.2f} seconds, expected around 5 seconds'

