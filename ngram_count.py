# tuple (ngram: number of occurances)

class NGramCounter(object):
    #n = order (length) of desired ngram
    def __init__(self, n):
        self.n = n
        self.ngrams = dict()
    # break up given string into units
    def tokenize(self, text):
        return text.split(" ")

    def feed(self, text):
        tokens = self.tokenize(text)

        for i in range(len(tokens) - self.n+1):
            gram = tuple(tokens[i: i+self.n])
            if gram in self.ngrams:
                self.ngrams[gram] += 1
            else:
                self.ngrams[gram] = 1
    def get_ngrams(self):
        return self.ngrams

if __name__ == '__main__':
    import sys

    # create NGramCounter object and feed data to it
    ngram_counter = NGramCounter(4)
    for line in sys.stdin:
        line = line.strip()
        ngram_counter.feed(line)

    #get ngrams from ngram counter; iterate over keys
    ngrams = ngram_counter.get_ngrams()
    for ngram in ngrams.keys():
        count = ngrams[ngram]
        if count > 4:
            n_gram_count = ' '.join(ngram) + ": "+str(count) + '\n'
            with open("text/n_gram_count.txt", "a") as text_file:
                text_file.write(n_gram_count)
