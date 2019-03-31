import random

class Generator(object):
    #Constructs unigram and bigram dicts
    def __init__(self, corpus):
        #Corpus should be a plain .txt file

        self.corpus = corpus
        self.parsed_corpus = None
        self.parse_corpus()
        self.generate_count()
        self.generate_seeds()

    def generate_seeds(self):
        #Generates 30 starting words from the corpus randomly
        #Words are accepted if first letter is capitalized
        seed = []
        while len(seed) < 30:
            starter = random.choice(self.parsed_corpus)
            if starter[0].isupper():
                seed.append(starter)

        self.seed = seed

    def parse_corpus(self):
        #Generates a list with the entire corpus in it.
        #No normalization.

        corp = open(self.corpus,'r',encoding = "ISO-8859-1")
        lines = corp.readlines()
        sentlist = [sent.split(' ') for sent in lines]
        words_flat = [word for sent in sentlist for word in sent]
        words_flat_polished = [w for w in words_flat if w != '']
        self.parsed_corpus = words_flat_polished

    def generate_count(self):
        #Generates two dictionaries: one for the bigrams probability
        #One for the unigrams probability, in order to compute the conditioned probability
        #with memory one
         
        #Counting dictionary, to be tranformed in probabilities
        unigram_dict = {}
        for w in self.parsed_corpus:
            if w not in unigram_dict:
                unigram_dict[w] = 1
            else:
                unigram_dict[w] += 1
     
        bigram_dict = {}
        for index in range(len(self.parsed_corpus)-1):
            if self.parsed_corpus[index] in bigram_dict:
                if self.parsed_corpus[index + 1] not in bigram_dict[self.parsed_corpus[index]]:
                    bigram_dict[self.parsed_corpus[index]][self.parsed_corpus[index+1]] = 1
                else:
                    bigram_dict[self.parsed_corpus[index]][self.parsed_corpus[index+1]] += 1      
            else:
                bigram_dict[self.parsed_corpus[index]] = {}
                if self.parsed_corpus[index + 1] not in bigram_dict[self.parsed_corpus[index]]:
                    bigram_dict[self.parsed_corpus[index]][self.parsed_corpus[index+1]] = 1
                else:
                    bigram_dict[self.parsed_corpus[index]][self.parsed_corpus[index+1]] += 1     
                  
        self.unigram_dict = unigram_dict
        self.bigram_dict = bigram_dict

    def generate_sentence(self):
        
        start = random.choice(self.seed)
        last_word = start
        sentence = start + ' '
        
        while last_word[-1] not in {'.','"', '?', '!', ';'} :
            sampling_dict = self.bigram_dict[last_word]
            sampling_list = []
            for w in sampling_dict:
                sampling_list = sampling_list + [w]*sampling_dict[w]
            last_word = random.choice(sampling_list)
            sentence +=last_word + ' '
        return sentence

if __name__ == '__main__':
    a = Generator('shake.txt')
    s = a.generate_sentence()
    print(s) 
