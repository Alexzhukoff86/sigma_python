class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.sentence) > 0:
            self.sentence = self.sentence.strip(' ')
            word = self.sentence.split(' ')[0]
            self.sentence = self.sentence.replace(word, '')
            return word
        else:
            raise StopIteration
