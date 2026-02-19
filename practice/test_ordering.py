import pytest


@pytest.mark.order(before = "test_login_gmail")
def test_facebook_gmail():
    print("facebook login")

@pytest.mark.order
def test_login_gmail():
    print("gmail login")
