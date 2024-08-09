import requests
import allure
import pytest


@allure.feature('User Registration')
@allure.suite('Registration Tests')
@allure.title('Successful Registration Test')
@allure.description('This test verifies successful registration with valid email and password.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_register_successful():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send request to register user'):
        response = requests.post(
            'https://reqres.in/api/register',
            headers=headers,
            json=data
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    with allure.step('Verify "id" is present in response'):
        assert 'id' in response.json(), 'ID not found in response'

    with allure.step('Verify "token" is present in response'):
        assert 'token' in response.json(), 'Token not found in response'

    with allure.step('Verify "token" length is greater than 0'):
        assert len(response.json().get('token', '')) > 0, 'Token length is 0'


@allure.feature('User Registration')
@allure.suite('Registration Tests')
@allure.title('Unsuccessful Registration Test')
@allure.description('This test verifies unsuccessful registration with missing password.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_register_unsuccessful():
    data = {
        "email": "eve.holt@reqres.in"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/register',
        headers=headers,
        json=data
    )

    with allure.step('Verify response status code is 400'):
        assert response.status_code == 400, f'Expected status code 400 but got {response.status_code}'

    with allure.step('Verify "error" message is "Missing password"'):
        assert response.json()["error"] == "Missing password", 'Error message is not as expected'

    with allure.step('Verify no "token" is present in response'):
        assert 'token' not in response.json(), 'Token should not be present in response'

    with allure.step('Verify no "id" is present in response'):
        assert 'id' not in response.json(), 'ID should not be present in response'








