import requests
import allure
import pytest


@allure.feature('User Management')
@allure.suite('User Update Tests')
@allure.title('Update Existing User')
@allure.description('This test verifies that an existing user can be updated and the response contains the updated user data.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_update_user():
    user_id = 2
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(
        f"https://reqres.in/api/users/{user_id}",
        headers=headers,
        json=data
    )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    with allure.step('Verify "name" is present in response'):
        assert response_data.get("name") == "morpheus", 'Name in response is not as expected'

    with allure.step('Verify "job" is present in response'):
        assert response_data.get("job") == "zion resident", 'Job in response is not as expected'

    with allure.step('Verify "updatedAt" is present in response'):
        assert 'updatedAt' in response_data, 'Update timestamp not found in response'
