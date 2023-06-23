import allure
import pytest
from extensions.verifications import Verifications
from workflows.api_flows import APIFlows

firstName = "Batel3"
lastName = "ham"
email1 = "batelaa1@gmaill.com"
email2 = "ofer221@gmaill.com"
programme = "Software"
courses = ["Java Course", "Math"]


class Test_API:

    @allure.title('Test01: Create Student & Verify Status Code')
    @allure.description('this test creates new student & verify status code')
    def test_create_student_and_verify_status(self):
        actual = APIFlows.create_student(firstName, lastName, email1, programme, courses)
        Verifications.verify_equals(actual, 201)

    @allure.title('Test02: Create Student & Verify New Student Details')
    @allure.description('this test creates new student & verify the value')
    @pytest.mark.skip(reason="Testing the Adding student is being tested on the first test. This is another option")
    def test_create_and_verify_added_student_by_name(self):
        # adding the new student
        actual_status = APIFlows.create_student(firstName, lastName, email2, programme, courses)
        # returning the first name of the last added student
        actual = APIFlows.get_value_for_last_student(actual_status, 'firstName')
        Verifications.verify_equals(actual, firstName)

    @allure.title('Test03: Update Student & Verify Status Code')
    @allure.description('this test update the last student & verify status code')
    def test_update_name_and_verify_status(self):
        actual = APIFlows.update_last_student_first_name(firstName + 'updated')
        Verifications.verify_equals(actual, 200)

    @allure.title('Test04: Update Student & Verify Student Details')
    @allure.description('this test update the last student & verify the value')
    @pytest.mark.skip(reason="Testing the Update student is being tested on the previous test. This is another option")
    def test_update_name_and_verify_student_updated_name(self):
        # updating the last student
        actual_status = APIFlows.update_last_student_first_name(firstName + 'updated')
        # returning the updated first name of the last added student
        actual = APIFlows.get_value_for_last_student(actual_status, 'firstName')
        Verifications.verify_equals(actual, firstName+'updated')

    @allure.title('Test05: Delete Student & Verify Status Code')
    @allure.description('this test delete last student & verify status code')
    def test_delete_last_student_and_verify(self):
        actual = APIFlows.delete_last_student()
        Verifications.verify_equals(actual, 204)

