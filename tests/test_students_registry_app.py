from tests.pages.add_student_page import AddStudentPage
from tests.pages.home_page import HomePage
from tests.pages.view_students_page import ViewStudentsPage
from datetime import datetime


class TestStudentsRegistryApp:

    def test_home_page_heading_and_top_links(self, driver):
        home_page = HomePage(driver)
        home_page.open()

        assert home_page.get_page_title() == 'MVC Example'
        assert home_page.get_page_heading() == "Students Registry"

        home_page.go_to_view_students_page()  # Go to the students page
        students_page = ViewStudentsPage(driver)

        assert students_page.is_currently_open is True
        driver.back()  # Return back to the home page

        home_page.go_to_add_students_page()  # Go to the add students page
        add_student_page = AddStudentPage(driver)

        assert add_student_page.is_currently_open is True
        driver.back()  # return back to the home page

        assert home_page.is_currently_open is True

    def test_view_student_page_heading_and_top_links(self, driver):
        view_students_page = ViewStudentsPage(driver)
        view_students_page.open()

        assert view_students_page.get_page_title() == "Students"
        assert view_students_page.get_page_heading() == "Registered Students"

        view_students_page.go_to_home_page()
        home_page = HomePage(driver)

        assert home_page.is_currently_open is True
        driver.back()

        view_students_page.go_to_add_students_page()
        add_student_page = AddStudentPage(driver)

        assert add_student_page.is_currently_open is True
        driver.back()

        assert view_students_page.is_currently_open is True

    def test_view_students_page(self, driver):
        view_students_page = ViewStudentsPage(driver)
        view_students_page.open()

        assert len(view_students_page.get_students_list()) > 0

    def test_add_student_page_heading_and_top_links(self, driver):
        add_student_page = AddStudentPage(driver)
        add_student_page.open()

        assert add_student_page.get_page_title() == "Add Student"
        assert add_student_page.get_page_heading() == "Register New Student"

        add_student_page.go_to_home_page()
        home_page = HomePage(driver)

        assert home_page.is_currently_open is True
        driver.back()

        add_student_page.go_to_view_students_page()
        view_student_page = ViewStudentsPage(driver)

        assert view_student_page.is_currently_open is True
        driver.back()

        assert add_student_page.is_currently_open is True

    def test_student_page_valid_data(self, driver):
        now_time = datetime.now()
        str_time = now_time.strftime('%Y-%m-%d-%H-%M-%S')

        add_student_page = AddStudentPage(driver)
        add_student_page.open()

        new_name = 'New student' + str_time
        new_email = str_time + '@email.com'

        add_student_page.add_student(new_name, new_email)

        students_page = ViewStudentsPage(driver)
        assert students_page.is_currently_open is True

        last_added_student = students_page.get_students_list()[-1].text
        assert last_added_student == f"{new_name} ({new_email})"

    def test_add_student_invalid_data(self, driver):
        add_student_page = AddStudentPage(driver)
        add_student_page.open()

        add_student_page.add_student(' ', 'Invalid@email')
        assert add_student_page.is_currently_open is True
        assert add_student_page.get_error_msg() == 'Cannot add student. Name and email fields are required!'
