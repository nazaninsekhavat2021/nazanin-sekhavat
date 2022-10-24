#1. List comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final_list =[]
    for i in range(1+x):
        for j in range(y+1):
            for k in range(1+z):
                if i+j+k!=n:
                    temp=[i,j,k]
                    final_list.append(temp)
                else:
                    continue
    print(final_list)      

#2.nested list
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

#3.finding the perecetage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        j = student_marks.get(i)
        if i==query_name:
            result = 0
            for k in j:
                result+= float(k)
            print("{:.2f}".format((result/len(j))))
            break
        else:
            continue


#4.list
if __name__ == '__main__':
    lst = []
    N = int(input())
    for i in range(N):
        mn= list(input("").split(" "))
        
        if mn[0]=="insert":
            a , b = map(int , (mn[1],mn[2]))
            lst.insert(a,b)
            
        elif mn[0]=="print":
            print(lst)
            
        elif mn[0]=="remove":
                lst.remove(int(mn[1]))

        elif mn[0]=="append":
            lst.append(int(mn[1]))
            
        elif mn[0]=="sort":
            lst.sort()
        
        elif mn[0]=="pop":
            
            lst.pop()
        elif mn[0]=="reverse":
            lst.reverse()
#5.tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))

#6.sWAP Case 
def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#7.string split and join

def split_and_join(line):
    return line.replace(' ','-')
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#8.mutations
def mutate_string(string, position, character):
    return string[:position]+character + string[(position+1):]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#9.find a string
def count_substring(string, sub_string):
    return
def count_substring(string, sub_string):
    len_SubString= len(sub_string)
    result = 0
    for i in range(len(string)+1-len_SubString):
        if string[i:i+len_SubString]==sub_string:
            result+=1
        else:
            continue
    
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#10.Iterotools.product
 import itertools as it
a = list(map(int , input("").split(' ')))
b = list(map(int , input("").split(' ')))
lst = list(x for x in it.product(a,b))
for i in lst:
    print(i, end = ' ' )
 

#11.collection counter 
x = int(input())
shoe_size = list(map(int,input().split()))
n = int(input())
sell = 0
for i in range(n):
    s, p = map(int,input().split())
    if s in shoe_size:
        sell = sell + p
        shoe_size.remove(s)
print(sell)
    

#12.itertools.permutation
import itertools as it
itere , n =input("").split(" ")
lst1 =(list(i for i in itere))
str(lst1.sort())
n=int(n)
lst = list( x for x in it.permutations(lst1 , n))
for i in lst:
    m = ""
    for j in i:
        m+=j
    print(m)

#13.polar coordinates
import cmath
m=complex(input())
print(abs(complex(m.real,m.imag)),'\n',cmath.phase(complex(m.real,m.imag)))

#14.introduction to set
def average(array):
    return (sum(set(array))/len(set(array)))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#15.DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
n,m=map(int,input().split())
for i in range(n):
    w = input()
    d[w].append(str(i+1))
for j in range(m):
    w = input()
    print(' '.join(d[w]) or -1)



#16.collection.namedtuple
n = int(input())
col_list = list(input().split())
marks_col = col_list.index("MARKS")
marks_list = []
for i in range(n):
    info_list = list(input().split())
    marks_list.append(float(info_list[marks_col]))
print(sum(marks_list)/n)


#17.collection.orderedDict
import collections, re
n = int(input())
item_od = collections.OrderedDict()
for i in range(n):
    record_list = re.split(r'(\d+)$',input().strip())
    item_name = record_list[0]
    item_price = int(record_list[1])
    if item_name not in item_od:
        item_od[item_name]=item_price
    else:
        item_od[item_name]=item_od[item_name]+item_price
            
for i in item_od:
    print(i+str(item_od[i]))

#18.itertools.combinations
import itertools as it
iterr ,n = input().split(" ")
lst1= list(i for i in iterr)
str(lst1.sort())
result = []
for i in range(1,int(n)+1):
    x = list(m for m in it.combinations(lst1, i))
    result.append(x)
for m in range(len(result)):
    for j in result[m]:
        for k in j:
            print(k, end ="" )
        print()

#19.set.add()
n=int(input(""))
s = set()
for i in range(n):
    m=input("")
    s.add(m)

print(len(s))


#20.intertools combination with replacement
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
lst , n = input("").split(" ")
n= int(n)
lst1 = list(x for x in lst)
lst1.sort()
lst = ''
for j in lst1:
    lst+=j
final = list(m for m in combinations_with_replacement(lst,n))
for x in final:
    s=''
    for i in x:
        s+=i
    print(s)


#21.set.discard(). Remove()&pop()
n = int(input())
s = set(map(int, input().split(" ")))
m = int(input())
for i in range(0,m):
    x=list(input().split(" "))
    if x[0]=="pop":
        s.pop()
    elif x[0]=="remove":
        j = int(x[1])
        s.remove(j)
    elif x[0]=="discard":
        j = int(x[1])
        s.discard(j)
print(sum(s))

#22.set.union Operation
n1 = int(input(""))
ls1=set(map(int , input("").split(" ")))
n2 = int(input(""))
ls2=set(map(int , input("").split(" ")))
ma = set(ls1.union(ls2))
output =0
for i in ma:
    output+=1

output = str(output)
print(output)

#23.mod divmod
a = int(input(""))
b = int(input(""))
print('{}\n{}\n{}'.format((a//b),(a%b),divmod(a,b)))

#24.power mod power
a = int(input(""))
b = int(input(""))
c = int(input(""))
print(a**b)
print(a**b%c)

#25.integer come in all size
a = int(input(""))
b = int(input(""))
c = int(input(""))
d = int(input(""))
print(a**b+c**d)

