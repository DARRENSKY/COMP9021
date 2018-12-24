import random

poker_dic = {'Ace':0, 'King':1, 'Queen':2, 'Jack':3, '10':4, '9':5}
hand_dic = {'Five of a kind':0, \
            'Four of a kind':1, \
            'Full house':2, \
            'Straight':3, \
            'Three of a kind':4, \
            'Two pair':5,\
            'One pair':6, \
            'Bust':7}

orders = ['second', 'third', 'forth', 'fifth']

def find_hand(dices):
    dic = {}
    for i in range(len(dices)):
        if dices[i] in dic.keys():
            dic[dices[i]] += 1
        else:
            dic[dices[i]] = 1

    l = list(dic.values())
    l.sort()
    if 5 in l:
        return hand_dic['Five of a kind']
    if 4 in l:
        return hand_dic['Four of a kind']
    if 3 in l and 2 in l:
        return hand_dic['Full house']
    c = 0
    if len(l) == 5:
        for i in range(1, len(dices)):
            if dices[i] - dices[i - 1] == 1:
                c += 1
    if c == 4:
        return hand_dic['Straight']
    if 3 in l:
        return hand_dic['Three of a kind']
    if len(l) == 3 and l[1] == 2 and l[2] == 2:
        return hand_dic['Two pair']
    if 2 in l:
        return hand_dic['One pair']
    return hand_dic['Bust']


def play():
    dices = []
    kepts = []
    order = 0
    while True:
        dices = kepts[:]
        if len(dices) == 5:
            print('Ok, done.')
            break
        for i in range(len(dices), 5):
            dices.append(random.randint(0, 5))
        dices.sort()
        print('The roll is:', end = '')
        for i in range(5):
            print(' ' + list(poker_dic.keys())[dices[i]], end='')
        print()
        hand = find_hand(dices)
        print('It is a ' + list(hand_dic.keys())[hand])
        flag = True
        if order >= 2:
            break
        while True:
            pstr = 'Which dice do you want to keep for the ' + orders[order] + ' roll? '
            kept_str = input(pstr)
            cur_kepts = []
            for i in kept_str.split(' '):
                if i != '':
                    if i == 'all' or i == 'All':
                        print('Ok, done.')
                        return
                    if i not in poker_dic.keys() or poker_dic[i] not in dices:
                        print('That is not possible, try again!')
                        break
                    cur_kepts.append(poker_dic[i])
            else:
                order += 1
                if len(kepts) == 5:
                    print('Ok, done.')
                    return
                kepts = cur_kepts[:]
                break


def simulate(n):
    nums = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(n):
        dices = []
        for j in range(5):
            dices.append(random.randint(0, 5))
        dices.sort()
        nums[find_hand(dices)] += 1
    for i in range(len(nums) - 1):
        print('%-15s: %.2f%%' % (list(hand_dic.keys())[i], nums[i] / sum(nums) * 100))

if __name__ == '__main__':
    random.seed(0)
    play()
    #simulate(100000)

