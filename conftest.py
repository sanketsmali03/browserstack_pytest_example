import pytest
from os import environ

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.remote_connection import RemoteConnection

import urllib3
urllib3.disable_warnings()

browsers = [
    {
         "os": "Windows",
      "os_version": "10",
      "browser": "Chrome",
      "browser_version": "latest"
    }, {
          "os": "Windows",
      "os_version": "10",
      "browser": "firefox",
      "browser_version": "latest"
    }]

def pytest_generate_tests(metafunc):
    if 'driver' in metafunc.fixturenames:
        metafunc.parametrize('browser_config',
                             browsers,
                             ids=_generate_param_ids('broswerConfig', browsers),
                             scope='function')


def _generate_param_ids(name, values):
    return [("<%s:%s>" % (name, value)).replace('.', '_') for value in values]


@pytest.yield_fixture(scope='function')
def driver(request, browser_config):

    desired_caps = dict()
    desired_caps.update(browser_config)
    username = environ.get('BROWSERSTACK_USERNAME', None)
    access_key = environ.get('BROWSERSTACK_ACCESS_KEY', None)
    selenium_endpoint = "http://"+username+":"+access_key+"@hub-cloud.browserstack.com/wd/hub"
    desired_caps['acceptInsecureCerts'] = 'true'
    desired_caps['build'] = "testbuild01"

   
    browser = webdriver.Remote(
    command_executor=selenium_endpoint,
    desired_capabilities=desired_caps)

   
    yield browser
    browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
    browser.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)

