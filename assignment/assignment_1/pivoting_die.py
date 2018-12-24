
def right(t, n):
    for i in range(n):
        a = [t[3]] + t[:3] + t[4:]
        t = a[:]
    return t[:]

def left(t, n):
    for i in range(n):
        a = t[1:4] + [t[0]] + t[4:]
        t = a[:]
    return t[:]

def front(t, n):
    for i in range(n):
        a = t[:]
        a[0] = t[5]
        a[2] = t[4]
        a[4] = t[0]
        a[5] = t[2]
        t = a[:]
    return t[:]

def back(t, n):
    for i in range(n):
        a = t[:]
        a[0] = t[4]
        a[2] = t[5]
        a[4] = t[2]
        a[5] = t[0]
        t = a[:]
    return t[:]

if __name__ == "__main__":
    while True:
        num = input("Enter the desired goal cell number: ")
        if not num.isdigit() or num == '':
            print('Incorrect value, try again')
            continue

        num = int(num)
        if num < 1:
            print('Incorrect value, try again')
            continue
        break
    a = [3, 1, 4, 6, 2, 5]
    duration = 1
    cur = 1
    while True:
        if cur + duration <= num:
            a = right(a, duration)
            cur += duration
        else:
            a = right(a, num - cur)
            break
        if cur + duration <= num:
            a = front(a, duration)
            cur += duration
        else:
            a = front(a, num - cur)
            break
        duration += 1
        if cur + duration <= num:
            a = left(a, duration)
            cur += duration
        else:
            a = left(a, num - cur)
            break
        if cur + duration <= num:
            a = back(a, duration)
            cur += duration
        else:
            a = back(a, num - cur)
            break
        duration += 1
    print("On cell %d, %d is at the top, %d at the front, and %d on the right." % \
          (num, a[0], a[4], a[1]))
