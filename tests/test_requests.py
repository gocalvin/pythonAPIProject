import pytest
import requests
from configparser import ConfigParser
from conf.resources import *
from conf.credentials import *
from requests_oauthlib import OAuth1
import json

pytestmark = pytest.mark.smoke


@pytest.fixture(scope='module')  # scope=module to execute my_setup only once
def my_setup():
    config = ConfigParser()

    config.read("conf/properties.ini")
 #   import pdb; pdb.set_trace()
    return config

wc_creds = get_env_credentials();
auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

def test_getresp(my_setup):
    config = my_setup
    url = config['API']['endpoint'] + APIRequests.getReq
    params = {'AuthorName': "John Doe"}

    get_resp = requests.get(url, params=params)
    print("New change")

    assert get_resp.status_code == 200, \
        f'Expected status code is 200 but actual status code is {get_resp.status_code}'


def test_postrequest(my_setup):
    with open("data/body.json") as f:
        body = f.read()
    url = "http://216.10.245.166//Library/Addbook.php"

    headers = {'Content-Type': 'Application/json'}

    post_resp = requests.post(url, body, headers)

    assert post_resp.status_code == 200
