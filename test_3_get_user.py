import requests
import allure
import pytest


@allure.feature('User Management')
@allure.suite('User List Tests')
@allure.title('Get List of Users')
@allure.description('This test retrieves a list of users from page 2 and verifies the response structure and content.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_list_users():
    url = 'https://reqres.in/api/users?page=2'
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send request to get users on page 2'):
        response = requests.get(url, headers=headers)

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "page"'):
        assert 'page' in response_data, "The response does not contain 'page'"

    with allure.step('Verify the response contains "per_page"'):
        assert 'per_page' in response_data, "The response does not contain 'per_page'"

    with allure.step('Verify the response contains "total"'):
        assert 'total' in response_data, "The response does not contain 'total'"

    with allure.step('Verify the response contains "total_pages"'):
        assert 'total_pages' in response_data, "The response does not contain 'total_pages'"

    with allure.step('Verify the response contains "data"'):
        assert 'data' in response_data, "The response does not contain 'data'"

    with allure.step('Verify the response contains "support"'):
        assert 'support' in response_data, "The response does not contain 'support'"

    with allure.step('Verify the "data" field is a list'):
        assert isinstance(response_data['data'], list), "The 'data' field is not a list"

    for user in response_data['data']:
        with allure.step(f'Verify user data: {user["id"]}'):
            assert 'id' in user, "User data does not contain 'id'"
            assert 'email' in user, "User data does not contain 'email'"
            assert 'first_name' in user, "User data does not contain 'first_name'"
            assert 'last_name' in user, "User data does not contain 'last_name'"
            assert 'avatar' in user, "User data does not contain 'avatar'"

    with allure.step('Verify the "support" field contains "url"'):
        assert 'url' in response_data['support'], "The 'support' field does not contain 'url'"

    with allure.step('Verify the "support" field contains "text"'):
        assert 'text' in response_data['support'], "The 'support' field does not contain 'text'"


@allure.feature('User Management')
@allure.suite('User Detail Tests')
@allure.title('Get Single User Details')
@allure.description('This test retrieves details of a single user by ID and verifies the response structure')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_single_user():
    single_user_id = 2
    with allure.step('Send request to get user by ID'):
        response = requests.get(f'https://reqres.in/api/users/{single_user_id}')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "first_name"'):
        assert 'first_name' in response_data['data'], "The response does not contain 'first_name'"

    with allure.step('Verify the response contains "last_name"'):
        assert 'last_name' in response_data['data'], "The response does not contain 'last_name'"

    with allure.step('Verify the response contains "email"'):
        assert 'email' in response_data['data'], "The response does not contain 'email'"

    with allure.step('Verify the response contains "id"'):
        assert 'id' in response_data['data'], "The response does not contain 'id'"

    with allure.step('Verify the response contains "support"'):
        assert 'support' in response_data, "The response does not contain 'support'"

    with allure.step('Verify the response contains "url"'):
        assert 'url' in response_data['support'], "The response does not contain 'url'"

    with allure.step('Verify the response contains "text"'):
        assert 'text' in response_data['support'], "The response does not contain 'text'"


@allure.feature('User Management')
@allure.suite('Error Handling Tests')
@allure.title('Single User Not Found')
@allure.description('This test verifies the response when attempting to retrieve a user that does not exist.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_single_user_not_found():
    single_user_id = 23
    url = f'https://reqres.in/api/users/{single_user_id}'
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send request to get user by ID'):
        response = requests.get(url, headers=headers)

    with allure.step('Verify response status code is 404'):
        assert response.status_code == 404, f'Expected Status Code 404, but got {response.status_code}'

    with allure.step('Verify response body is empty'):
        assert response.text == '{}', "The response body is not empty"
