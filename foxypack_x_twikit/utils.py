from foxypack import AnswersAnalysis

from foxypack_x_twikit.answers import TwitterAnswersAnalysis


def as_twitter_analysis(
    analysis: AnswersAnalysis,
) -> TwitterAnswersAnalysis:
    if not isinstance(analysis, TwitterAnswersAnalysis):
        raise TypeError(
            "Analysis is not TwitterAnswersAnalysis"
        )

    return analysis