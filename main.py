import array
import string
import copy

class HashHist(object):
    SYMBOL_COUNT = 100
    ORD_A = ord('a')
    INT_ARRAY = array.array('b',SYMBOL_COUNT*[0])
    CHR_ARRAY = array.array('c',SYMBOL_COUNT*[' '])

    def __init__(self, p_word,p_arrays=None):
        int_hist = copy.copy(HashHist.INT_ARRAY)
        chr_hist = copy.copy(HashHist.CHR_ARRAY)
        self.word = string.lower(p_word)
        for c in p_word:
            i = ord(c) - HashHist.ORD_A
            int_hist[i] += 1
        for i in xrange(HashHist.SYMBOL_COUNT):
            j = chr(HashHist.ORD_A + int_hist[i])
            chr_hist[i] = j
        self.encoding = tuple(chr_hist)
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
