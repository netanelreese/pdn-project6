from mrjob.job import MRJob


class MRLongestWord(MRJob):

    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield word[0], word

    def reducer(self, initial_char, words):
        longest_word = ''
        longest_words = []
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
                longest_words = [word]
            elif len(word) == len(longest_word):
                longest_words.append(word)
        yield initial_char, longest_words

if __name__ == '__main__':
    MRLongestWord.run()