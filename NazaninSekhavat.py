#1-solve me first

def solveMeFirst(a,b):
    return a+b
    
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


#2-simple array sum


import os
import sys

def simpleArraySum(ar):
    result = 0
    for i in ar:
        result = result+i
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#3-compare the trplets


import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    score = [0,0]
    for i in range(len(a)):
        if (a[i] > b[i]):
            score[0] = score[0] + 1
        elif(a[i] < b[i]):
            score[1] = score[1] + 1
        else:
            pass
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


#4-a very big sum


import os

def aVeryBigSum(ar):
    result = 0
    for i in range(len(ar)):
        result = result + ar[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#5-plus minus


import math
import os
import random
import re
import sys

def plusMinus(arr):
    plus = 0
    minus = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            plus = plus + 1
        elif arr[i] < 0:
            minus = minus + 1
        else:
            zero = zero + 1 
    print("{0:.6f}".format(plus/len(arr)))
    print("{0:.6f}".format(minus/len(arr)))
    print("{0:.6f}".format(zero/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


#6-staircase


import math
import os
import random
import re
import sys

def staircase(n):
   for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)

if __name__ == '__main__':
    n = int(input())

    staircase(n)


#7-birthday candles


import math
import os
import random
import collections
import re
import sys

def birthdayCakeCandles(ar):
    return (max(collections.Counter(ar).values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#8-time conversion


import os
import sys

def timeConversion(s):
    #
    # Write your code here.
    #
    print(str(s))
    time = (s.split(":"))
    ampm = time[2][2:4]
    if ampm == "PM":
        if time[0] != "12":
            time[0]=int(int(time[0])+12)
            time[0] = str(time[0])
    elif ampm == "AM":
        if time[0] == "12":
            time[0] = "00"
        
    ntime = ':'.join(time)
    print(str(ntime))
    return str(ntime[:-2])
    
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()


#9-big sorting


import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):
    return sorted(unsorted,key=lambda x: (len(x), x))
    # temp = list(map(str, temp))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()


#10-super reduced string


import re
s = input()
for i in range(50):
  s = re.sub(r'(.)\1', '', s)
print(s if s else 'Empty String')


#11-inserstion sort-part 1

def insertionSort1(n, arr):
    tmp = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > tmp:
            arr[i+1] = arr[i]
            print(' '.join(map(str, arr)))
        else:
            arr[i+1] = tmp
            print(' '.join(map(str, arr)))
            return

    arr[0] = tmp
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#12-two charecters

import re
import itertools
import string
_, s = input(), input()
result = 0
for pair in itertools.combinations(string.ascii_lowercase, 2):
  t = ''.join(c for c in s if c in pair)
  if not re.search(r'(.)\1', t) and len(t) >= 2:
    result = max(result, len(t))
print(result)


#13-quicksort 1-partition

import sys

def quickSort(arr):
    left = [i for i in arr if i < arr[0]]
    right = [i for i in arr if i > arr[0]]
    equal = [i for i in arr if i == arr[0]]
    return left + equal + right
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))


#14-counting sort 1

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    mx = max(arr)
    l = [0 for i in range(100)]
    for a in arr:
        l[a] += 1
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


#15-counting sort 2

import os

def countingSort(arr):
    s = [0 for _ in range(100)]
    ret = []

    for i in arr:
        s[i] += 1

    for i in range(len(s)):
        for j in range(s[i]):
            ret.append(i)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.close()


#16-beautiful binary string


import re
n, B = int(input()), input()
count = 0
for match in re.finditer(r'0((10)+)', B):
  count += (len(match.group(1)) + 2) // 4
print(count)


#17-closest numbers

import sys

def closestNumbers(arr):
    output = []
    arr = sorted(arr)
    nowmin = 10**9
    
    for ind in range(1, len(arr)):
        diff = abs(arr[ind-1] - arr[ind])
        
        if diff < nowmin:
            output = [(arr[ind-1], arr[ind])]
            nowmin = diff
        elif diff == nowmin:
            output.append((arr[ind-1], arr[ind]))
            
    flat_list = [item for sublist in output for item in sublist]
        
    return flat_list
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))


#18-find the median

import sys

def findMedian(arr):
    arr = sorted(arr)
    return arr[len(arr)//2]

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr)
    print(result)


#19-insertion sort advanced analysis

def merge(v, start, end):
    if end - start <= 1:
        return 0

    if end - start == 2:
        if v[start] > v[start + 1]:
            tmp = v[start]
            v[start] = v[start + 1]
            v[start + 1] = tmp
            return 1

        return 0

    # print(str(start) + ', ' + str(end))

    mid = start + (end - start) // 2
    count = merge(v, start, mid) + merge(v, mid, end)

    v1 = v[start:mid]
    index = start
    i, j = 0, mid
    while i < len(v1) and j < end:
        if v1[i] <= v[j]:
            v[index] = v1[i]
            i += 1
        elif v1[i] > v[j]:
            v[index] = v[j]
            count += mid - start - i
            j += 1

        index += 1

    while i < len(v1):
        v[index] = v1[i]
        index += 1
        i += 1

    while j < end:
        v[index] = v[j]
        index += 1
        j += 1

    #print('count = ' + str(count))
    return count

nn = int(input())
for ni in range(0, nn):
    n = int(input())
    vec = list(map(int, input().split()))
    print(merge(vec, 0, len(vec)))


#20-fraudulent activity notifications

import os

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    count_array = [0] * 201

    for i in range(d):
        count_array[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        if expenditure[i] >= getMedianVal(count_array, d) * 2:
            count += 1
        count_array[expenditure[i - d]] -= 1
        count_array[expenditure[i]] += 1

    return count

def getMedianVal(count_arr, d):
    is_length_even = d % 2 == 0
    total_count = 0

    for i, count in enumerate(count_arr):
        total_count += count

        if is_length_even:
            if total_count == d // 2:
                for j in range(i + 1, len(count_arr)):
                    if count_arr[j] > 0:
                        return (i + j) / 2
            elif total_count > d // 2:
                return i
        else:
            if total_count >= d // 2 + 1:
                return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    EXPENDITURE = list(map(int, input().rstrip().split()))
    RESULT = activityNotifications(EXPENDITURE, d)

    fptr.write(str(RESULT) + '\n')
    fptr.close()


#21-anagram


from collections import Counter
for case in range(int(input())):
  s = input()
  if len(s) % 2:
    print(-1)
  else:
    c = Counter(s[:len(s)//2]) - Counter(s[len(s)//2:])
    print(sum(x for x in c.values() if x > 0))
#22-lily’s homework

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def lilysHomework(arr):
    return min(minNoOfSwapsAsc(arr), minNoOfSwapsDesc(arr))

def minNoOfSwapsDesc(arr):
    positions = [x[0] for x in sorted(enumerate(arr), key=lambda x: x[1], reverse=True)]
    
    n = len(arr)
    visited = [False for _ in range(n)]
    ans = 0
    for i in range(n):
        if visited[i] or positions[i] == i:
            continue
        
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = positions[j]
            cycle_size += 1
        
        if cycle_size > 0:
            ans += (cycle_size - 1)
    
    return ans

def minNoOfSwapsAsc(arr):
    positions = [x[0] for x in sorted(enumerate(arr), key=lambda x: x[1], reverse=False)]
    
    n = len(arr)
    visited = [False for _ in range(n)]
    ans = 0
    for i in range(n):
        if visited[i] or positions[i] == i:
            continue
        
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = positions[j]
            cycle_size += 1
        
        if cycle_size > 0:
            ans += (cycle_size - 1)
    
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


#23-two strings

for case in range(int(input())):
  a, b = input(), input()
  print('YES' if set(a).intersection(set(b)) else 'NO')


#24-mini max sum

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    x = sum(map(int,arr))
    print ((x-(max(arr))), (x-(min(arr))))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


#25-diagnal differences

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    
    primary=0
    secondary=0 
    n = len(arr)
    print(n)
    for i in range(n):
         for j in range(n):
             if i==j:
                 primary = primary + arr[i][j]
             if i==n-j-1:
                 secondary = secondary + arr[i][j]
    return abs(primary-secondary)
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

