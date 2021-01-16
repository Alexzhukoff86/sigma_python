from home_work.lesson7.task1.source.Sentence import Sentence


def test_sentence_iterator():
    sentence = Sentence("Test message  for you")
    assert next(sentence) == 'Test'
    assert next(sentence) == 'message'
    assert next(sentence) == 'for'
    assert next(sentence) == 'you'



