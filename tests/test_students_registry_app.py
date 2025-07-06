from tests.pages.home_page import HomePage


class TestStudentsRegistryApp:

    def test_home_page_heading_and_top_links(self, driver):
        home_page = HomePage(driver)
        home_page.open()

        assert home_page.get_page_title() == 'MVC Example'
        assert home_page.get_page_heading() == "Students Registry"

        home_page.go_to_view_students_page()