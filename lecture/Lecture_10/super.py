'''
while True:
    switch=input("Do you want to switch?")
    if switch in {'yes','Yes','y','Y'}:
        switch=True
        break
    elif switch  in {'no','No','n','N'}:
        switch=False
        break
    else:
        print("incorret input, try again")
'''
#import random
'''
print(dir(random))
for x in dir(random):
    if not x.startswith('_'):
        print(x)
'''
'''
print([x for x in dir(random) if not x.startswith('_')])
while True:
    help(random.choice)
    n=random.choice(['A','B','C'])
    print(n)
'''
'''
for _ in range(5):
    print(1+1)
'''
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*(n-1)

def power(a,n):
    if n==0:
        return 1
    else:
        return a*power(a,n-1)
def gcdone(a,b):
    if a==0:
        return b
    else:
        return gcdone(b%a,a)
'''
'''
import math
def perfect_square(n):
    for i in range(123456789,n):
        c=math.sqrt(i)
        d=int(c)
        s=str(i)
        a=[]
        if c==d:
            for e in s:
                a.append(str(e))
            a.sort()
            if a==['1','2','3','4','5','6','7','8','9']:
                print(i)
'''           
'''

        a=[]
        for e in s:
            a.append(str(e))
        a.sort()
        if a==['1','2','3','4','5','6','7','8','9']:
            if c==d:
                print(i)
        '''
'''                    
perfect_square(999999999)
'''
'''
def eratosthenes(n):
    P = [i for i in range(2, n+1)]
    #print(P)
    p = 0
    while True:
        for i in P[p + 1:]:
            if i % P[p] == 0:
                P.remove(i)
        #print(P[p]**2)
        #if P[p]**2 >= P[-1]:
#            break
        if p>n:
            break
        p += 1
    return P

if __name__ == "__main__":
    print (eratosthenes(100000000))
'''
'''
operator={'+':lambda x ,y:x+y}
print(operator[+](2,3))
'''
'''
import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)

list(d.items())
'''
'''
class Python:
    def selfDemo(notself):
        print('Python,why self?')
i=1
j=1
for a, b in {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}:
    print(a,b)
'''
'''
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
                
if __name__=="__main__":
    T=Solution()
    print(T.twoSum([2,7,11,15],17))
'''
class BinaryTree:
    def __init__(self, value = None):
        self.value = value
        if self.value is not None:
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
        else:
            self.left_node = None
            self.right_node = None
    def height(self):
        if self.value is None:
            return 0
        return max(self.left_node._height(), self.right_node._height())
    def _height(self):
        if self.value is None:
            return 0
        return max(self.left_node._height()+1, self.right_node._height()+1)
    def size(self):
        if self.value is None:
            return 0
        return self.left_node.size()+self.right_node.size()+1
    def occurs_in_tree(self, value):
        print(self.value)
        print(value)
        if self.value is None:
            return False
        if self.value == value:
            return True
        return self.left_node.occurs_in_tree(value) or self.right_node.occurs_in_tree(value)
    def insert_in_bst(self, value):
        if self.value is None:
            self.value = value
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
            return True
        if self.value == value:
            return False
        if value < self.value:
            return self.left_node.insert_in_bst(value)
        return self.right_node.insert_in_bst(value)
    def print_binary_tree(self):
        if self.value is None:
            return
        self._print_binary_tree(0, self.height())
    def _print_binary_tree(self, n, height):
        if n > height:
            return
        if self.value is None:
            print('\n' * (2 ** (height - n + 1) - 1), end = '')
        else:
            self.left_node._print_binary_tree(n + 1, height)
            print('      ' * n, self.value, sep = '')
            self.right_node._print_binary_tree(n + 1, height)



t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
t.left_node = t_L; t_L.left_node = t_LL
t.right_node = t_R; t_R.left_node = t_RL; t_RL.right_node = t_RLR ; t_R.right_node = t_RR
t.height()

    

    
