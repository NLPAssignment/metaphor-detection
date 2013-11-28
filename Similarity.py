from nltk.corpus import wordnet as wn
from GetDependencyParse import dependency_parse

def detect_metaphor(sentence):
    """ Accepts a sentence and outputs similarity of noun-noun pairs related by nsubj
    """

    dep_parse_output, noun_list = dependency_parse(sentence)

    nsubj_pairs = [ns_parse[1:] for ns_parse in filter(lambda dp: dp[0] == "nsubj" and dp[1] in noun_list and dp[2] in noun_list, dep_parse_output)]

    for pair in nsubj_pairs:
        print "\nInvestigating metaphor for pair {0}".format(pair)

        syn_pair = []

        for word in pair:

            synsets = wn.synsets(word)
            print "What sense of '{0}' would you like to use?".format(word)
            for i, synset in enumerate(synsets):
                print "{0}: {1}".format(i, synset.definition)
            chosen_id = int(raw_input("Enter number corresponding to sense: "))

            syn_pair.append(synsets[chosen_id])

        similarity_measure = similarity(syn_pair[0], syn_pair[1])
        print "Similarity is {0}".format(similarity_measure)

def similarity(synset1, synset2):
    """ Accepts 2 synsets and returns the similarity
    """

    return synset1.path_similarity(synset2)

if __name__ == "__main__":
    sentence = raw_input("Enter a sentence: ")

    detect_metaphor(sentence)

# word1 = wn.synsets('children')
# word2 = wn.synsets('babies')
# max_sim = 0
# max_sim_w1=""
# max_sim_w2=""
# for w1 in word1:
#     for w2 in word2:
#         sim = w1.path_similarity(w2)
# 	#sim = w1.lch_similarity(w2)
# 	#sim = w1.wup_similarity(w2)
# 	#sim = w1.res_similarity(w2,corpus)
# 	#sim = w1.jcn_similarity(w2,corpus)
# 	#sim = w1.lin_similarity(w2,corpus)
		
# 	if max_sim < sim:
#             max_sim = sim
# 	    max_sim_w1=w1
# 	    max_sim_w2=w2

# print max_sim
# print max_sim_w1
# print max_sim_w2

