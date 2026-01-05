from foxy_entities import EntitiesController

from foxypack_x_twikit import FoxyTwitterAnalysis, FoxyTwitterStat


def test_get_statistics_tweet(test_account):
    controller = EntitiesController()
    controller.add_entity(test_account)

    twitter_stat = FoxyTwitterStat(entities_controller=controller)
    twitter_stat_two = FoxyTwitterStat(entities_controller=controller)

    analysis = FoxyTwitterAnalysis().get_analysis(
        "https://x.com/elonmusk/status/2000078735622721927"
    )

    stat_one = twitter_stat.get_statistics(analysis)
    stat_two = twitter_stat_two.get_statistics(analysis)

    assert stat_one.answer_id != stat_two.answer_id
    assert stat_one.tweet_id == stat_two.tweet_id
    assert stat_one.text == stat_two.text
    assert stat_one.analysis_status == stat_two.analysis_status


def test_get_statistics_profile(test_account):
    controller = EntitiesController()
    controller.add_entity(test_account)

    twitter_stat = FoxyTwitterStat(entities_controller=controller)
    twitter_stat_two = FoxyTwitterStat(entities_controller=controller)

    analysis = FoxyTwitterAnalysis().get_analysis("https://x.com/elonmusk")

    stat_one = twitter_stat.get_statistics(analysis)
    stat_two = twitter_stat_two.get_statistics(analysis)

    assert stat_one.answer_id != stat_two.answer_id
    assert stat_one.user_id == stat_two.user_id
    assert stat_one.username == stat_two.username
    assert stat_one.analysis_status == stat_two.analysis_status
