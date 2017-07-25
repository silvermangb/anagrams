import array
import string


class HashHist(object):
    SYMBOL_COUNT = 100
    ORD_A = ord('a')

    def __init__(self, p_word):
        self.word = p_word
        self.hash= hash(''.join(sorted(self.word)))


    def __repr__(self):
        s = '(%s\t, % 010x)' % (self.word, self.hash)
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
