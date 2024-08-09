import requests
import allure
import pytest


@allure.feature('User Authentication')
@allure.suite('Login Tests')
@allure.title('Successful Login Test')
@allure.description('Tests a successful login attempt and checks for the presence and validity of the token.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_login_successful():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
            'https://reqres.in/api/login',
            headers=headers,
            json=data
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    with allure.step('Verify "token" is present in response'):
        assert 'token' in response.json(), 'Token not found in response'

    with allure.step('Verify "token" length is greater than 0'):
        assert len(response.json().get('token')) > 0, 'Token length is 0'


@allure.feature('User Authentication')
@allure.suite('Login Tests')
@allure.title('Unsuccessful Login Test')
@allure.description('Tests an unsuccessful login attempt due to missing password and verifies error messages.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_login_unsuccessful():
    data = {
        "email": "peter@klaven"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/login',
        headers=headers,
        json=data
    )

    with allure.step('Verify response status code is 400'):
        assert response.status_code == 400, f'Expected status code 400 but got {response.status_code}'

    with allure.step('Verify "error" is present in response'):
        assert 'error' in response.json(), 'Error message not found in response'

    with allure.step('Verify "error" message is "Missing password"'):
        assert response.json()["error"] == "Missing password", 'Error message is not as expected'

    with allure.step('Verify no token is present in response'):
        assert 'token' not in response.json(), 'Token should not be present in response'

