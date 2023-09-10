def one_word_extractor(word, n):
    c: int = 0
    for i in word:
        c += 1
        if c == n:
            return i


def word_merger(word1, word2):
    output = ""
    if len(word1) > len(word2):
        s = len(word2)
        g = len(word1)
        yo = 1
    else:
        s = len(word1)
        g = len(word2)
        yo = 2

    for i in range(s):
        output = output + one_word_extractor(word1, i + 1) + one_word_extractor(word2, i + 1)
    o = ""
    if yo == 1:
        for j in range(s, g):
            o = o + one_word_extractor(word1, j + 1)
    else:
        for jo in range(s, g):
            o = o + one_word_extractor(word2, jo + 1)
    return output + o
