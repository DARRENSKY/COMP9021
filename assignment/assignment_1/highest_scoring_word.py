from itertools import combinations, permutations

dic = {'a':2, 'b':5, 'c':4, 'd':4, 'e':1, 'f':6, 'g':5, 'h':5, 'i':1, 'j':7,\
       'k':6, 'l':3, 'm':5, 'n':2, 'o':3, 'p':5, 'q':7, 'r':2, 's':1, 't':2,\
       'u':4, 'v':6, 'w':6, 'x':7, 'y':5, 'z':7}

#list(permutations([1, 2, 3], 2))


def get_score(word):
    score = 0
    for i in word:
        score += dic[i]
    return score

def sort_str(word):
    l = list(word)
    l.sort()
    return ''.join(l)

if __name__ == "__main__":
    s = input("Enter between 3 and 10 lowercase letters: ")
    l = []
    for i in s.split(' '):
        if i == '':
            continue
        for j in i:
            if j not in dic:
                print('Incorrect input, giving up...')
                exit(-1)
            else:
                l.append(j)

    if len(l) < 3 or len(l) > 10:
        print('Incorrect input, giving up...')
        exit(-1)

    f = open("wordsEn.txt", "r")
    lines = f.readlines()
    words = {}
    sorted_words = {}
    for i in lines:
        i = i.strip('\n')
        words[i] = 1
        word = sort_str(i)
        sorted_words[word] = 1
        #print(sorted_words)
    score_words = []
    score = 0
    for i in range(len(l), 0, -1):
        for j in list(combinations(l, i)):
            word = ''.join(j)
            print(word)
            word = sort_str(word)
            cur_score = get_score(word)
            print(cur_score)
            print(score)
            if score > cur_score:
                continue
            if word in sorted_words:
                if score == cur_score and word not in score_words:
                    score_words.append(word)
                    #print(score_words)
                elif score < cur_score:
                    score_words = [word]
                    #print(score_words)
                    score = cur_score

    r = []

    for i in list(words.keys()):
        word = sort_str(i)
        #print(word)
        if word in score_words:
            r.append(i)

    score_words = r[:]

    if len(score_words) == 0:
        print('No word is built from some of those letters.')
    elif len(score_words) == 1:
        print('The highest score is %d.' % score)
        print('The highest scoring word is %s' % score_words[0])
    else:
        print('The highest score is %d.' % score)
        print('The highest scoring words are, in alphabetical order:')
        score_words.sort()
        for i in score_words:
            print('    %s' % i)

