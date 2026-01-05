from ej6c1 import sentiment_analysis


def test_sentiment_analysis():
    text = "I love this product!"
    assert sentiment_analysis(text) == "Positive", "The sentiment does not match with the input text, which was " + text

    text = "This product is terrible."
    assert sentiment_analysis(text) == "Negative", "The sentiment does not match with the input text, which was " + text

    text = "This product is okay."
    assert sentiment_analysis(text) == "Positive", "The sentiment does not match with the input text, which was " + text

    text = "I don't know what to think about this product."
    assert sentiment_analysis(text) == "Neutral", "The sentiment does not match with the input text, which was " + text
