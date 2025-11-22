def test_login(browser):
    browser.get("https://www.google.com")
    assert 4 == 5


# pytest -v --html=report.html
