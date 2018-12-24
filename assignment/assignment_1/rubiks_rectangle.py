

label = "12348765"

def right_circular_shift(s):
    a = s[3] + s[0:3] + s[7] + s[4:7]
    return a

def row_exchange(s):
    a = s[4:] + s[0:4]
    return a

def middle_clockwise_rotation(s):
    a = s[0] + s[5] + s[1] + s[3] + s[4] + s[6] + s[2] + s[7]
    return a

if __name__ == "__main__":
    final = input("Input final configuration: ")
    s = ''
    for i in final.split(' '):
        if i == '':
            continue
        s += i
        print(type(s))
    flag = True
    for i in s:
        #if s[i] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        if i not in '12345678':
            print('Incorrect configuration, giving up...')
            flag = False
    if flag:
        final = s[0:4] + s[7] + s[6] + s[5] + s[4]
        s = '12348765'
        checked = {}
        q = [s]
        print(q[0])
        qc = [0]
        #print(qc)
        v = None
        c = 0
        while len(q) > 0:
            v = q[0]
            q.remove(q[0])
            c = qc[0]
            qc.remove(qc[0])
            if v == final:
                break
            checked[v] = 1
            print(checked)
            s1 = right_circular_shift(v)
            if s1 == final:
                c += 1
                break
            if s1 not in checked:
                q.append(s1)
                qc.append(c + 1)
            s2 = row_exchange(v)
            if s2 == final:
                c += 1
                break
            if s2 not in checked:
                q.append(s2)
                qc.append(c + 1)
            s3 = middle_clockwise_rotation(v)
            if s3 == final:
                c += 1
                break
            if s3 not in checked:
                q.append(s3)
                qc.append(c + 1)
        if c <= 1:
            print('%d step is needed to reach the final configuration.' % c)
        else:
            print('%d steps are needed to reach the final configuration.' % c)

