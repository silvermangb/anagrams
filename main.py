import array
import string
import copy

class HashHist(object):
    SYMBOL_COUNT = 256
    INT_ARRAY = array.array('b',SYMBOL_COUNT*[0])
    CHR_ARRAY = array.array('c',SYMBOL_COUNT*[' '])
    SYMBOL_COUNT_XRANGE = xrange(SYMBOL_COUNT)

    def __init__(self, p_word,p_arrays=None):
        int_hist = copy.copy(HashHist.INT_ARRAY)
        self.word = string.lower(p_word)
        for c in p_word:
            int_hist[ord(c)] += 1
        self.encoding = tuple(int_hist)
        self.hash = hash(self.encoding)
                
      

    def __repr__(self):
        s = '(%s\t,%s,% 010x)' % (self.word, str(self.encoding), self.hash)
        return s


words = open('english language dictionary.txt', 'r')
anagrams = {}
counts = {}

for i in words:
    i = i.strip()
    hh = HashHist(i)
    if hh.hash in anagrams:
        anagrams[hh.hash].append(hh.word)
    else:
        anagrams[hh.hash] = [hh.word]

for h in anagrams:
    a = anagrams[h]
    l = len(a)
    if l in counts:
        counts[l].add(h)
    else:
        counts[l] = set([h])

c = counts.keys()
c = sorted(c[:], reverse=True)
for i in c:
    if i == 1:
        continue
    hs = counts[i]
    for j in hs:
        a = anagrams[j]
        print len(a), len(a[0]), sorted(a)
