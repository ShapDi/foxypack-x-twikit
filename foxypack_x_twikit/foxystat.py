import asyncio
from datetime import datetime

from foxy_entities import EntitiesController
from foxypack import (
    FoxyStat,
    InternalCollectionException,
    AnswersAnalysis,
)
from twikitminifix import Client, User, Tweet
from typing_extensions import override

from foxypack_x_twikit.answers import (
    TwitterEnum,
    TwitterTweetAnswersStatistics,
    TwitterProfileAnswersStatistics,
)
from foxypack_x_twikit.entities import TwitterAccount
from foxypack_x_twikit.utils import as_twitter_analysis


class FoxyTwitterStat(FoxyStat):
    def __init__(self, entities_controller: EntitiesController | None = None):
        self._entities_controller = entities_controller

    def _get_account(self) -> TwitterAccount:
        if self._entities_controller is None:
            raise InternalCollectionException

        return self._entities_controller.get_entity(TwitterAccount)

    async def _get_client(self) -> Client:
        account = self._get_account()
        client = Client("en-US")

        try:
            client.load_cookies(account.cookies_file)
        except FileNotFoundError:
            await client.login(
                auth_info_1=account.username,
                auth_info_2=account.email,
                password=account.password,
            )
            client.save_cookies(account.cookies_file)

        if self._entities_controller is not None:
            self._entities_controller.add_entity(account)

        return client

    @staticmethod
    def _profile_from_user(user: User, analysis: AnswersAnalysis) -> TwitterProfileAnswersStatistics:
        return TwitterProfileAnswersStatistics(
            title=user.name,
            user_id=user.id,
            username=user.screen_name,
            screen_name=user.name,
            subscribers=user.followers_count,
            following_count=user.following_count,
            tweet_count=user.statuses_count,
            listed_count=user.listed_count,
            favourites_count=user.favourites_count,
            verified=user.verified,
            description=user.description,
            location=user.location,
            profile_image_url=user.profile_image_url,
            creation_date=datetime.strptime(
                user.created_at, "%a %b %d %H:%M:%S %z %Y"
            ).date(),
            system_id=user.id,
            analysis_status=analysis,
        )

    @staticmethod
    def _tweet_from_tweet(tweet: Tweet, analysis: AnswersAnalysis) -> TwitterTweetAnswersStatistics:
        return TwitterTweetAnswersStatistics(
            title=tweet.text[:50],
            tweet_id=tweet.id,
            user_id=tweet.user.id,
            username=tweet.user.screen_name,
            text=tweet.text,
            views=tweet.view_count,
            like_count=tweet.favorite_count,
            retweet_count=tweet.retweet_count,
            reply_count=tweet.reply_count,
            quote_count=tweet.quote_count,
            bookmark_count=tweet.bookmark_count,
            language=tweet.lang,
            publish_date=tweet.created_at_datetime.date(),
            system_id=tweet.id,
            analysis_status=analysis,
        )

    async def _get_statistics_async_internal(
        self, analysis: AnswersAnalysis
    ) -> TwitterProfileAnswersStatistics | TwitterTweetAnswersStatistics:

        if analysis.social_platform != "twitter":
            raise InternalCollectionException

        analysis = as_twitter_analysis(analysis)

        client = await self._get_client()

        if analysis.type_content == TwitterEnum.profile.value:
            user = await client.get_user_by_screen_name(analysis.code)
            return self._profile_from_user(user, analysis)

        if analysis.type_content == TwitterEnum.tweet.value:
            tweet = await client.get_tweet_by_id(analysis.code)
            return self._tweet_from_tweet(tweet, analysis)

        raise ValueError(f"Unsupported twitter content type: {analysis.type_content}")

    @override
    def get_statistics(
        self, analysis: AnswersAnalysis
    ) -> TwitterProfileAnswersStatistics | TwitterTweetAnswersStatistics:
        return asyncio.run(self._get_statistics_async_internal(analysis))

    @override
    async def get_statistics_async(
        self, analysis: AnswersAnalysis
    ) -> TwitterProfileAnswersStatistics | TwitterTweetAnswersStatistics:
        return await self._get_statistics_async_internal(analysis)
