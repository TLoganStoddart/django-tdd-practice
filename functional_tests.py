from selenium import webdriver


def test_title_is_correct():
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')

    assert 'Congratulations' in browser.title
