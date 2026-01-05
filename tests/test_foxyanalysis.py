import pytest

from foxypack_x_twikit import FoxyTwitterAnalysis


@pytest.mark.analysis
def test_twitter_tweet_link():
    content_analyzer = FoxyTwitterAnalysis()
    analysis = content_analyzer.get_analysis(
        "https://x.com/elonmusk/status/2000078735622721927"
    )
    analysis_two = content_analyzer.get_analysis(
        "https://x.com/elonmusk/status/2000078735622721927"
    )

    assert analysis.answer_id != analysis_two.answer_id
    assert analysis.url == "https://x.com/elonmusk/status/2000078735622721927"
    assert analysis.social_platform == "twitter"
    assert analysis.type_content == "tweet"
    assert analysis.code == "2000078735622721927"


@pytest.mark.analysis
def test_twitter_profile_link():
    content_analyzer = FoxyTwitterAnalysis()
    analysis = content_analyzer.get_analysis("https://x.com/elonmusk")
    analysis_two = content_analyzer.get_analysis("https://x.com/elonmusk")

    assert analysis.answer_id != analysis_two.answer_id
    assert analysis.url == "https://x.com/elonmusk"
    assert analysis.social_platform == "twitter"
    assert analysis.type_content == "profile"
    assert analysis.code == "elonmusk"
