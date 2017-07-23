import sys
import array
import string

class HashHist(object):
    SYMBOL_COUNT = 100
    def __init__(self, p_word):
        int_hist = array.array('b',[0 for i in xrange(HashHist.SYMBOL_COUNT)])
        self.word = string.lower(p_word)
        for c in p_word:
            i = ord(c)-ord('a')
            int_hist[i] += 1
        chr_hist =[' ' for i in xrange(HashHist.SYMBOL_COUNT)]
        for i in xrange(HashHist.SYMBOL_COUNT):
            j = chr(ord('a')+int_hist[i])
            chr_hist[i] = j
        self.encoding = ''.join(chr_hist)
        self.hash = hash(self.encoding)
    def __repr__(self):
        s = '(%s\t,%s,% 010x)' % (self.word,self.encoding,self.hash)
        return s

words = open('english language dictionary.txt','r')
anagrams = {}
maxanagarams = []
counts = {}

for i in words:
    i = i.strip()
    hh = HashHist(i)
    if hh.hash in anagrams:
        anagrams[hh.hash].append(hh.word)
        l = anagrams[hh.hash]
        if len(l) > len(maxanagarams):
            maxanagarams = l
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
c = sorted(c[:],reverse=True)
for i in c:
    hs = counts[i]
    for j in hs:
        a = anagrams[j]
        print len(a),a



