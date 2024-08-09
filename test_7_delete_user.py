import requests
import allure
import pytest


@allure.feature('User Management')
@allure.suite('User Deletion Tests')
@allure.title('Delete Existing User')
@allure.description('This test verifies that an existing user can be deleted successfully and that a subsequent request to retrieve the user returns a 404 status code.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user():
    user_id = 2
    headers = {'Content-Type': 'application/json'}

    response = requests.delete(
        f"https://reqres.in/api/users/{user_id}",
        headers=headers
    )

    with allure.step('Verify response status code is 204'):
        assert response.status_code == 204, f'Expected status code 204 but got {response.status_code}'

    with allure.step('Verify response content is empty'):
        assert response.text == '', 'Response content should be empty for a successful DELETE request'

