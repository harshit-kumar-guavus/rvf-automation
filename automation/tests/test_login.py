import pytest

from actions.login_action import LoginActions


class TestLogin(object):

    @pytest.mark.sanity
    def test_login_logout(self, selenium):
        """Testcase Title.
            Verify Login Operation.
        """
        self.login_actions = LoginActions(driver=selenium)
        self.login_actions.open_browser()
        self.login_actions.login("usr01", "usr01@123")
        assert 'Dashboard Builder' in selenium.title

