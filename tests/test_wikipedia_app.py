import allure
from allure_commons.types import Severity
from selene import have
from wikipedia_app.models.controls.page_search_results import results_wiki
from wikipedia_app.models.controls.search import search_wiki
from wikipedia_app.data.search_info import search_data
from wikipedia_app.data.user import user
from wikipedia_app.models import app


@allure.tag("UI mobile test")
@allure.severity(Severity.CRITICAL)
@allure.story("Wikipedia app")
@allure.label("owner", "OAO")
@allure.title('Test search')
def test_search():
    with allure.step('Search "Browser stack"'):
        search_wiki().type('BrowserStack')

    with allure.step('Check results'):
        results_wiki().should(have.size_greater_than(0))


@allure.tag("UI mobile test")
@allure.severity(Severity.NORMAL)
@allure.story("Wikipedia app")
@allure.label("owner", "OAO")
@allure.title('Test empty search')
def test_empty_search():
    with allure.step('Add empty field'):
        search_wiki().type('')

    with allure.step('Check results'):
        results_wiki().should(have.size(0))


@allure.tag("UI mobile test")
@allure.severity(Severity.NORMAL)
@allure.story("Wikipedia app")
@allure.label("owner", "OAO")
@allure.title('Test search numbers')
def test_search_numbers():
    with allure.step('Search numbers'):
        search_wiki().type('123')

    with allure.step('Check results'):
        results_wiki().should(have.size_greater_than(0))


@allure.tag("UI mobile test")
@allure.severity(Severity.NORMAL)
@allure.story("Wikipedia app")
@allure.label("owner", "OAO")
@allure.title('Test search special symbols')
def test_search_special_symbols():
    with allure.step('Search symbols'):
        search_wiki().type('#%')

    with allure.step('Check results'):
        results_wiki().should(have.size(0))


@allure.tag("UI mobile test")
@allure.severity(Severity.NORMAL)
@allure.story("Wikipedia app")
@allure.label("owner", "OAO")
@allure.title('Test search html tag')
def test_search_html_tag():
    with allure.step('Search tag'):
        search_wiki().type('<div>')

    with allure.step('Check results'):
        results_wiki().should(have.size_greater_than(0))


@allure.tag("UI mobile test")
@allure.severity(Severity.CRITICAL)
@allure.story("Wikipedia app")
@allure.label("owner", "OAO")
@allure.title('Test search')
def test_search_successfully():
    app.given_opened()

    with allure.step('Make search request'):
        app.open_search_page()
        app.wikipedia_search(text=search_data.search_text)
        app.check_wikipedia_search(text=search_data.expected_search_text)


@allure.tag("UI mobile test")
@allure.severity(Severity.BLOCKER)
@allure.story("Wikipedia app")
@allure.label("owner", "OAO")
@allure.title('Test open article')
def test_open_article():
    app.given_opened()

    with allure.step('Search for Python article'):
        app.wikipedia_search(text=search_data.search_text)
        app.check_wikipedia_search(text=search_data.expected_search_text)

    with allure.step('Open first article'):
        app.article_open(article_number=0)
        app.check_article_open(text=search_data.expected_article_description)


@allure.tag("UI mobile test")
@allure.severity(Severity.BLOCKER)
@allure.story("Wikipedia app")
@allure.label("owner", "OAO")
@allure.title('Test open article categories')
def test_open_article_categories():
    app.given_opened()

    with allure.step('Search for Python article'):
        app.wikipedia_search(text=search_data.search_text)
        app.check_wikipedia_search(text=search_data.expected_search_text)

    with allure.step('Open second article'):
        app.article_open(article_number=1)

    with allure.step('Open article categories'):
        app.open_article_categories()
        app.check_categories_title()


@allure.tag("UI mobile test")
@allure.severity(Severity.CRITICAL)
@allure.story("Wikipedia app")
@allure.label('owner', 'OAO')
@allure.title('Test login with incorrect data')
def test_login_with_invalid_data():
    app.given_opened()

    with allure.step('Open saved page'):
        app.open_saved_page()
        app.check_page_title(text='Saved')

    with allure.step('Login with incorrect data'):
        app.open_login_form()
        app.fill_login_form(
            username=user.user.fake_username,
            password=user.user.fake_password
        )
        app.submit_form()

    with allure.step('Check for login with incorrect data'):
        app.check_login_with_incorrect_data()


@allure.tag("UI mobile test")
@allure.severity(Severity.CRITICAL)
@allure.story("Wikipedia app")
@allure.label("owner", "OAO")
@allure.title('Test login successfully')
def test_login_successfully():
    app.given_opened()

    with allure.step('Open saved page'):
        app.open_saved_page()
        app.check_page_title(text='Saved')

    with allure.step('Login with correct data'):
        app.open_login_form()
        app.fill_login_form(
            username=user.username,
            password=user.password
        )
        app.submit_form()

    with allure.step('Check user has been logged'):
        app.check_saved_articles_after_login()
