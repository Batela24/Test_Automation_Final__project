import allure
import requests


header = {'Content-Type': 'application/json'}


class APIActions:

    @staticmethod
    @allure.step('Get Request')
    def get(path: str):
        response = requests.get(path)
        return response

    @staticmethod
    @allure.step('Extract value from response')
    def extract_value_from_response(response_json, nodes):
        extracted_value = None
        if len(nodes) == 1:
            extracted_value = response_json[nodes[0]]
        elif len(nodes) == 2:
            extracted_value = response_json[(nodes[0])][(nodes[1])]
        return extracted_value

    @staticmethod
    @allure.step('POST Request')
    def post(path: str, payload):
        response = requests.post(path, json=payload, headers=header)
        return response.status_code

    @staticmethod
    @allure.step('PUT Request')
    def put(path: str, payload):
        response = requests.put(path, json=payload, headers=header)
        return response.status_code

    @staticmethod
    @allure.step('DELETE Request')
    def delete(path: str):
        response = requests.delete(path)
        return response.status_code

    @staticmethod
    @allure.step('return list size')
    def get_list_size(options_list: list):
        return len(options_list)
