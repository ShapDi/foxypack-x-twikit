import re
import urllib.parse
from typing_extensions import override

from foxypack import FoxyAnalysis, DenialAnalyticsException
from foxypack_x_twikit.answers import TwitterAnswersAnalysis, TwitterEnum


class FoxyTwitterAnalysis(FoxyAnalysis):
    @staticmethod
    def get_code(link: str) -> str:
        tweet_match = re.search(r"/status/(\d+)", link)
        if tweet_match:
            return tweet_match.group(1)

        profile_match = re.search(r"(?:twitter\.com|x\.com)/([^/?]+)/?$", link)
        if profile_match:
            return profile_match.group(1)

        return ''

    @staticmethod
    def clean_link(link: str) -> str:
        parsed = urllib.parse.urlparse(link)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    @staticmethod
    def get_type_content(link: str) -> str | None:
        if "/status/" in link:
            return TwitterEnum.tweet.value
        if re.match(r"https?://(?:twitter\.com|x\.com)/[^/?]+/?$", link):
            return TwitterEnum.profile.value
        return None

    @override
    def get_analysis(self, url: str) -> TwitterAnswersAnalysis:
        type_content = self.get_type_content(url)
        if type_content is None:
            raise DenialAnalyticsException(url)

        return TwitterAnswersAnalysis(
            url=self.clean_link(url),
            social_platform="twitter",
            type_content=type_content,
            code=self.get_code(url),
        )
