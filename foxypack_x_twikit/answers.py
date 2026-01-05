from enum import Enum
from foxypack.foxypack_abc.answers import (
    AnswersAnalysis,
    AnswersSocialContent,
    AnswersSocialContainer,
)


class TwitterEnum(Enum):
    tweet = "tweet"
    profile = "profile"


class TwitterAnswersAnalysis(AnswersAnalysis):
    code: str


class TwitterTweetAnswersStatistics(AnswersSocialContent):
    tweet_id: str
    user_id: str
    username: str
    text: str
    like_count: int
    retweet_count: int
    reply_count: int
    quote_count: int
    bookmark_count: int
    language: str


class TwitterProfileAnswersStatistics(AnswersSocialContainer):
    user_id: str
    username: str
    screen_name: str
    following_count: int
    tweet_count: int
    listed_count: int
    favourites_count: int
    verified: bool
    description: str
    location: str
    profile_image_url: str
