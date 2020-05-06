from wordtools import test

def cleanword(word):
    clean = ""
    for char in word:
        if char in '0123456789!;:,?.@#$%¨&*()_-+=^~':
            char = ""
        if char == "'":
            char = ""
        clean = clean + char
    return clean

def has_dashdash(word):
    for i in range(0, len(word) - 1):
        if word[i] == '-' and word[i + 1] == '-':
            return True
    return False

def extract_words(frase):
    new = []
    word = str()
    for i in range(0, len(frase)):
        if frase[i] not in '0123456789!;:,?.@#$%¨&*()_-+=^~"" ':
            if frase[i] != "'":
                word = word + frase[i].lower()
        else:
            if len(word) > 0:
                new.append(word)
                word = ""
    if i == len(frase) - 1:
        if len(word) > 0:
            new.append(word)
    return new

def wordcount(word, lista):
    saida = 0
    for palavra in lista:
        if palavra == word:
            saida += 1
    return saida

def wordset(lista):
    set = []
    aux = 0
    for i in range(0, len(lista)):
        if len(set) > 0:
            achou = 0
            for j in range(0, len(set)):
                if set[j] == lista[i]:
                    achou = 1
            if achou == 0:
                set.append(lista[i])
        else:
            set.append(lista[i])


    return sorted(set)

def longestword(lista):
    max = 0
    for word in lista:
        if len(word) > max:
            max = len(word)

    return max


def test_suite():

    test(cleanword("what?") == "what")

    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") == "word")
    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))
    test(extract_words("Now is the time! 'Now', is the time? Yes, now. ") ==
         ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") ==
         ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
         )
    test(wordcount("now",
                   ["now", "is", "time", "is", "now", "is", "is"]) == 2)
    test(wordcount("is",
                   ["now", "is", "time", "is", "now", "the", "is"]) == 3)
    test(wordcount("time",
                   ["now", "is", "time", "is", "now", "is", "is"]) == 1)
    test(wordcount("frog",
                   ["now", "is", "time", "is", "now", "is", "is"]) == 0)
    test(wordset(["now", "is", "time", "is", "now", "is",
                  "is"]) ==
         ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"])
         ==
         ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but",
                  "am"]) ==
         ["a", "am", "are", "be", "but", "is", "or"])
    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
    test(longestword([]) == 0)


test_suite()

