import requests
import allure
import pytest


@allure.feature('User Management')
@allure.suite('User Creation Tests')
@allure.title('Create New User')
@allure.description('This test verifies that a new user can be created and the response contains the correct user data.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_create_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        "https://reqres.in/api/users",
        headers=headers,
        json=data
    )

    with allure.step('Verify response status code is 201'):
        assert response.status_code == 201, f'Expected status code 201 but got {response.status_code}'

    with allure.step('Verify "name" is present in response'):
        assert response.json().get("name") == "morpheus", 'Name in response is not as expected'

    with allure.step('Verify "job" is present in response'):
        assert response.json().get("job") == "leader", 'Job in response is not as expected'

    with allure.step('Verify "id" is present in response'):
        assert "id" is not None, 'ID not found in response'

    with allure.step('Verify "createdAt" is present in response'):
        assert 'createdAt' in response.json(), 'Creation timestamp not found in response'







