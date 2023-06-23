import pytest
from extensions.api_actions import APIActions
from utilities.common_ops import get_data
import allure

url = get_data('Api_Url')


class APIFlows:

    @staticmethod
    @allure.step('Bring all the students')
    def get_all_students():
        all_students = APIActions.get(url + 'student/list')
        return all_students.json()

    @staticmethod
    @allure.step('Get value from student list')
    def get_value_for_student(status, api_field, location):
        response = APIFlows.get_all_students()
        if int(status) == 201 or int(status) == 200:
            nodes = [location, api_field]
            return APIActions.extract_value_from_response(response, nodes)
        else:
            pytest.fail("The following email is already exist, the product wasn't added")

    @staticmethod
    @allure.step('Get value for last student')
    def get_value_for_last_student(status, api_field):
        return APIFlows.get_value_for_student(status, api_field, APIFlows.return_last_student_location())

    @staticmethod
    @allure.step('Create new student')
    def create_student(name, last_name, email, programme, courses):
        all_students = APIFlows.get_all_students()
        emails = []
        for student in all_students:
            emails.append(student['email'])

        # checking if the email already exist in the server
        if email in emails:
            pytest.fail("The following email is already exist: " + email + " Pls insert another")
        else:
            payload = {
                "firstName": name,
                "lastName": last_name,
                "email": email,
                "programme": programme,
                "courses": courses
            }
            status_code = APIActions.post(url + 'student', payload)
            return status_code

    @staticmethod
    @allure.step('Update student')
    def update_last_student_first_name(name):
        last_student = APIFlows.return_last_student_json()
        last_student_id = last_student['id']
        payload = {
            "firstName": name,
            "lastName": last_student['lastName'],
            "email": last_student['email'],
            "programme": last_student['programme'],
            "courses": last_student['courses']
        }
        status_code = APIActions.put(url + 'student/' + str(last_student_id), payload)
        return status_code

    @staticmethod
    @allure.step('Delete last student')
    def delete_last_student():
        last_student_id = APIFlows.return_last_student_json()['id']
        status_code = APIActions.delete(url + 'student/' + str(last_student_id))
        return status_code

    @staticmethod
    @allure.step('return the last student that was inserted')
    def return_last_student_json():
        amount_of_students = APIActions.get_list_size(APIFlows.get_all_students())
        last_student = APIFlows.get_all_students()[amount_of_students - 1]
        return last_student

    @staticmethod
    @allure.step('return the last student that was inserted')
    def return_last_student_location():
        amount_of_students = APIActions.get_list_size(APIFlows.get_all_students())
        location_in_list = amount_of_students-1
        return location_in_list

