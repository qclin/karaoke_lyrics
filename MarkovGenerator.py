#  info: http://www.decontextualize.com/teaching/dwwp/topics-n-grams-and-markov-chains/
import sys
import markov

generator = markov.MarkovGenerator(n=3, max=500)

for line in sys.stdin:
    line = line.strip()
    generator.feed(line)


for i in range(5):
    print generator.generate()


def feed(self, text):
    tokens = self.tokenize(text)

    # discard if line is too short
    if len(tokens) < self.n:
        return

    #store the first ngram of this line
    beginning = tuple(tokens[:self.n])
    self.beginnings.append(beginning)

    for i in range(len(tokens) - self.n):
        gram = tuple(tokens[i: i+self.n])
        next = tokens[i+self.n] # get the element after the gram

        if gram in self.ngrams:
            self.ngrams[gram].append(next)
        else:
            self.ngrams[gram] = [next]

def generate(self):
    from random import choice
    current = choice(self.beginnings)
    output = list(current)
    for i in range(self.max):
        if current in self.ngrams:
            possible_next = self.ngrams[current]
            next = choice(possible_next)
            output.append(next)

            current = tuple(output[-self.n:])
        else:
            break
    output_str = self.concatenate(output)
    return output_str
