def sentence_function_generator(sentence):
    while len(sentence) > 0:
        sentence = sentence.strip(' ')
        word = sentence.split(' ')[0]
        sentence = sentence.replace(word, '')
        yield word


def sentence_generator_comprehension(sentence):
    sentence_generator = (x for x in sentence.split(' '))
    return sentence_generator