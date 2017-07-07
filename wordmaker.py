import enchant as ec
import itertools as it
from math import fabs

d = ec.Dict('en-US')

def makewords(data, start):

    if start <= len(data):
        data = [j for j in data]
        meaningfulwords = []
        for i in range(start, len(data)+1):
            L = list(it.combinations(data, i))

            for tup in L:
                permut = list(it.permutations(tup))

                for t in permut:
                    word = ''.join(t)

                    if d.check(word):
                        if word not in meaningfulwords:
                            meaningfulwords.append(word)

        return meaningfulwords

    else:
        print "Cannot make words of length "+str(start)+" from provided alphabets."
        return None


def wordoflength(data, length):

    words = makewords(data, length)

    if words != None:
        required = []
        for word in words:
            if len(word) == length:
                required.append(word)
        return required

    else:
        return words

def removecommons(data, word):
    data = [i for i in data]

    for i in word:
        if i in data:
            data.remove(i)

    return ''.join(data)

def complementary(data, length):

    lengthoffirstword = length
    lengthofsecondword = int(fabs(len(data) - length))

    possibles = {}
    
    words1 = wordoflength(data, lengthoffirstword)

    for word in words1:
        words2 = wordoflength(removecommons(data, word), lengthofsecondword)
        if words2 != []:
            possibles.update({word:words2})

    return possibles

def prettify(data):

    if type(data) == type({}):
        for i in data:
            print i, ':', data[i]

    elif type(data) == type([]):
        for i in data:
            print i
