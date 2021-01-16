from home_work.lesson7.task2.source.sentence_generators import sentence_function_generator, \
    sentence_generator_comprehension


def test_sentence_function_generator():
    sentence = "Test message for you"
    sentence_gen = sentence_function_generator(sentence)
    assert next(sentence_gen) == 'Test'
    assert next(sentence_gen) == 'message'
    assert next(sentence_gen) == 'for'
    assert next(sentence_gen) == "you"


def test_sentence_generator_comprehension():
    sentence = "Test message for you"
    sentence_gen = sentence_generator_comprehension(sentence)
    assert next(sentence_gen) == 'Test'
    assert next(sentence_gen) == 'message'
    assert next(sentence_gen) == 'for'
    assert next(sentence_gen) == "you"
