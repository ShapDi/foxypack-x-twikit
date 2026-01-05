import os

import pytest
from dotenv import load_dotenv

from foxypack_x_twikit import TwitterAccount

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="session")
def test_account():
    return TwitterAccount(
        username=os.getenv("TWITTER_USERNAME"),
        email=os.getenv("TWITTER_EMAIL"),
        password=os.getenv("TWITTER_PASSWORD"),
        cookies_file=os.getenv("TWITTER_COOKIES_FILE"),
    )
