from foxy_entities import SocialMediaEntity

class TwitterAccount(SocialMediaEntity):
    username: str
    email: str
    password: str
    cookies_file: str = "twitter_cookies.json"
