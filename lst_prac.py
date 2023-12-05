print('----------sum of list items-----------')


lst=[1,2,3,4,5,6,7,8]

sm=0

for i in lst:
    sm+=i

print('sum of list items :',sm)

print('--------------Change enven to # using list comprihension---------------')

lst=[1,2,3,4,5,6,7,8]

lst1=['#' if i%2==0 else i for i in lst]

print(lst1)


print('----------------------Print only odd of a list using list comprehension---------------------------')


lst=[1,2,3,4,5,6,7,8]

lst1=[i for i in lst if i%2!=0]

print(lst1)

print('------------------------- program to multiply all the items in a list-------------------------')

lst=[1,2,3,4,5]

mul=1

for i in lst:
    mul*=i

print(mul)


print('-------------------------  program to get the largest number from a list-------------------------')


lst=[8,12,56,4,77,9,3,7]

large_no=lst[0]


for i in lst:
    if i>large_no:
        large_no=i

print(large_no)


print('-------------------------  program to get the smallest number from a list-------------------------')


lst=[8,12,56,4,77,9,3,7]

smallest_no=lst[0]

for i in lst:
    if i<smallest_no:
        smallest_no=i


print(smallest_no)


print('-------------------------  program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same -------------------------')



lst=['abja', 'xyz', 'aba', '1221']

ctr=0

for i in lst:
    if len(i)>0 and i[0] == i[-1]:
        ctr+=1

print(ctr)

print('---------------------------------------------------------')

lst=[[1,1,1],[1,0,1],[1,1,1]]



for i in range(len(lst)):
    if i==0:
        lst[i]=lst[i+1]
        lst[i+2]=lst[i+1]
        lst[i+1]=[0]*3

for i in lst:
    print(i)
    
#print(lst)


print('-----Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples-------')


'''
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n):
    return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

print(sort_list_last(lst))




print('------Python program to remove duplicates from a list------')

lst=['shankar','satyam','aman','akshat','rahul','sanjeev','shankar','rahul','satyam']

lst1=list(dict.fromkeys(lst))

print(lst1)


print('------Python program to check if a list is empty or not------')

def checklst(lst):
    if len(lst)==0:
        return 'Your List is empty'
    else:
        return 'Your List is not empty'



CheckList=checklst([0,1,2])
print(CheckList)

print('------Python program to clone or copy a list------')


original_list = [10, 22, 44, 23, 4]


new_list = list(original_list)


print(id(original_list))
print(original_list)

print(id(new_list))
print(new_list)


print('------Python program to find the list of words that are longer than n from a given list of words------')


lst=['shankar','satyam','aman','akshat','rahul','sanjeev','shankar','rahul','satyam']

n=6

for i in lst:
    if len(i)>n:
        print(i)



print('------Python function that takes two lists and returns True if they have at least one common member------')

def common_data(list1, list2):
    result = False

    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

# Call the 'common_data' function with two lists and print the result
print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
# Call the 'common_data' function with two lists and print the result
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9])) 


print('------Python program to print a specified list after removing the 0th, 4th and 5th elements------')

'''
 Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''

lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print(lst)

lst = [x for (i, x) in enumerate(lst) if i not in (0, 4, 5)]


print(lst)


print('------Python program to generate a 3*4*6 3D array whose each element is *------')


Array = [[['*' for col in range(6)]for col in range(4)]for rows in range(3)]

print(Array)



print('------Python program to print the numbers of a specified list after removing even numbers from it------')

lst=[1,2,3,4,5,6,7,8,9]

lst=[i for i in lst if i%2!=0]
print(lst)

print('------Python program to shuffle and print a specified list------')

from random import shuffle

lst=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(lst)

print(lst)


print('------Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included)-----')

n=30

lst=[i**2 for i in range(1,n+1)]

print(lst[:5])
print(lst[-5:])    


print('------Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False-----')



# Define a function named 'test' that takes a list 'nums' as a parameter
def test(nums):
    # Use a generator expression to check if each number in 'nums' is prime, and return True if all are prime
    return all(is_prime(i) for i in nums)

# Define a function named 'is_prime' that checks if a number 'n' is prime
def is_prime(n):
    # Check if 'n' is equal to 1; if so, it's not prime
    if (n == 1):
        return False
    # Check if 'n' is equal to 2; if so, it's prime
    elif (n == 2):
        return True
    else:
        # Iterate through numbers from 2 to 'n' - 1
        for x in range(2, n):
            # If 'n' is divisible by 'x', it's not prime; return False
            if (n % x == 0):
                return False
        # If no divisors were found, 'n' is prime; return True
        return True

# Define a list 'nums' containing a sequence of numbers
nums = [0, 3, 4, 7, 9]
# Print the original list of numbers
print("Original list of numbers:")
print(nums)
# Check if each number in 'nums' is prime and print the result
print("Check if each number is prime in the said list of numbers:")
print(test(nums))

# Reassign 'nums' with a different list of numbers
nums = [3, 5, 7, 13]
# Print the original list of numbers
print("\nOriginal list of numbers:")
print(nums)
# Check if each number in the new 'nums' list is prime and print the result
print("Check if each number is prime in the said list of numbers:")
print(test(nums))

# Reassign 'nums' with another list of numbers
nums = [1, 5, 3]
# Print the original list of numbers
print("\nOriginal list of numbers:")
print(nums)
# Check if each number in the new 'nums' list is prime and print the result
print("Check if each number is prime in the said list of numbers:")
print(test(nums)) 




print('------Python program to generate all permutations of a list in Python-----')

import itertools

lst=[1, 5, 3]

a=itertools.permutations(lst)

print(list(a))



print('------Python program to calculate the difference between the two lists-----')


list1 = [1, 3, 5, 7, 9]


list2 = [1, 2, 4, 6, 7, 8]


diff_list1_list2 = list(set(list1) - set(list2))


diff_list2_list1 = list(set(list2) - set(list1))


total_diff = diff_list1_list2 + diff_list2_list1


print(total_diff)




print('------Python program to access the index of a list-----')


lst = [1, 2, 4, 6, 7, 8]

for index,value in enumerate(lst):
    print(index,value)




print('------Python program to convert a list of characters into a string-----')

lst=['p','y','t','o','n']

strng=''.join(lst)

print(strng)





print('------Python program to find the index of an item in a specified list-----')


lst=['aman','akshat','sanjeev','shankar','rahul','satyam']

for i in range(len(lst)):
    if lst[i]=='shankar':
        print('Index of shankar is =',i)


#Second way

print('Index of satyam is =',lst.index('satyam'))




print('------Python program to flatten a shallow list-----')

import itertools

# Define a list 'original_list' containing nested sublists
original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# Use 'itertools.chain' and the unpacking operator (*) to merge the sublists into a single flat list
new_merged_list = list(itertools.chain(*original_list))

# Print the newly merged list 'new_merged_list'
print(new_merged_list)


print('------Python program to append a list to the second list-----')



lst=[5,8,7,9,4,6,]
lst1=['Red','Green','White','Black','Yellow']

for i in lst1:
    lst.append(i)
print(lst)


#second way


lst=[5,8,7,9,4,6,]
lst1=['Red','Green','White','Black','Yellow']

lst2=lst+lst1

print(lst2)



print('------Python program to select an item randomly from a list-----')


import random
# Define a list 'color_list' containing various colors
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']

# Use the 'random.choice' function to select and print a random color from the 'color_list'
print(random.choice(color_list))



print('------Python program to check whether two lists are circularly identical-----')

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

# Compare list1 and list2
print('Compare list1 and list2')

# Check if the string representation of list2 is present in the string representation of list1 repeated twice
# The result will be True if list2 is a subsequence of list1 repeated twice, otherwise False
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))

# Compare list1 and list3
print('Compare list1 and list3')

# Check if the string representation of list3 is present in the string representation of list1 repeated twice
# The result will be True if list3 is a subsequence of list1 repeated twice, otherwise False
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2))) 

# Compare list2 and list3
print('Compare list2 and list3')

# Check if the string representation of list3 is present in the string representation of list1 repeated twice
# The result will be True if list3 is a subsequence of list1 repeated twice, otherwise False
print(' '.join(map(str, list3)) in ' '.join(map(str, list2 * 2))) 



print('------Python program to find the second smallest number in a list-----')

lst=[10,8,12,56,4,77,9,3,7]

min=lst[0]
second_min=0


for i in lst:
    if i < min:
        min = i
    elif i>min:
        second_min=i


print(second_min)


print('------Python program to find the second largest number in a list-----')

lst=[10,8,12,56,4,77,9,3,7]

max=lst[0]
second_max=lst[0]


for i in lst:
    if i > max:
        max = i

for i in lst:
    if i>second_max and i!=max:
        second_max=i


print(second_max)


print('------Python program to get unique values from a list-----')



lst=[10, 20, 30, 40, 20, 50, 60, 40]

lst1=list(dict.fromkeys(lst))


print(lst1)



print('------ Python program to get the frequency of elements in a list-----')

# Import the 'collections' module, which provides specialized container data types
import collections

# Define a list 'my_list' containing multiple numbers, including duplicates
my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

# Print the original list 'my_list'
print("Original List : ", my_list)

# Use the 'collections.Counter' function to count the frequency of each element in 'my_list' and store it in 'ctr'
ctr = collections.Counter(my_list)

# Print the frequency of the elements in the list, as provided by the 'ctr' object
print("Frequency of the elements in the List : ", ctr) 



print('####--Second Way--####')

lst=[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
lst=[str(i) for i in lst]

strng = ' '.join(lst)

lst1=list(dict.fromkeys(lst))

lst2=[]

for i in lst1:
    lst2.append(strng.count(i))

d1=(dict(zip(lst1,lst2)))

print('Frequency of the elements in the List :',d1)
    


print('------ Python program to count the number of elements in a list within a specified range-----')


def count_range_in_list(li, min, max):
    ctr = 0
    for x in li:
        if min <= x <= max:
            ctr += 1
    return ctr

list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]

print(count_range_in_list(list1, 40, 100))

list2 = ['a', 'b', 'c', 'd', 'e', 'f']

print(count_range_in_list(list2, 'a', 'e')) 




#Second Way


li = [10, 20, 30, 40, 40, 40, 70, 80, 99]

ctr = 0
for x in li:
    if 40 <= x <= 100:
        ctr += 1


print(ctr)






print('------Python program to check whether a list contains a sublist-----')


def is_Sublist(l, s):
    sub_set = False  

    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                # If 'n' equals the length of 's', 's' is a sublist of 'l
                if n == len(s):
                    sub_set = True
    return sub_set

# Define list 'a,' 'b,' and 'c'
a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]

# Check if 'b' is a sublist of 'a' and print the result
print(is_Sublist(a, b))

# Check if 'c' is a sublist of 'a' and print the result
print(is_Sublist(a, c)) 

print('----##Second way##----')

lst=[1,2,4,8,9,3]
lst1=[8,9]
lst2=[9,8]



for i in lst:
    if i==lst2[0]:
        if [lst[j+(lst.index(i))] for j in range(len(lst2))]==lst2:
            print('Given list is availble inside existing list')
        else:
            print('Given list is NOT availble inside existing list')


print('------Python program to generate all sublists of a list-----')

from itertools import combinations

def sub_lists(my_list):
    subs = []
    for i in range(0, len(my_list) + 1):
        temp = [list(x) for x in combinations(my_list, i)]
        if len(temp) > 0:
            subs.extend(temp)

    return subs


l1 = [10, 20, 30, 40]

l2 = ['X', 'Y', 'Z']

print("Original list:")
print(l1)
print("Sublists of the said list:")
print(sub_lists(l1))

print("\nOriginal list:")
print(l2)

print("Sublists of the said list:")
print(sub_lists(l2))


print('------Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number-----')

'''
 Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
'''

# Define a function named 'prime_eratosthenes' that generates prime numbers using the Sieve of Eratosthenes algorithm
def prime_eratosthenes(n):
    prime_list = []  # Create an empty list to store prime numbers
    # Iterate through the numbers from 2 to 'n'
    for i in range(2, n+1):
        if i not in prime_list:
            # If 'i' is not in the 'prime_list,' it's a prime number; print it
            print(i)

            # Mark all multiples of 'i' as non-prime by adding them to 'prime_list'
            for j in range(i*i, n+1, i):
                prime_list.append(j)

# Call the 'prime_eratosthenes' function with 'n' set to 100 to generate prime numbers
# The function does not have a return value, so it prints the prime numbers directly
prime_eratosthenes(100)

print('------Python program to create a list by concatenating a given list with a range from 1 to n-----')

'''
Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''


lst=['p','q']
n=5
lst1=[]
for i in range(1,n+1):
    for j in lst:
        lst1.append(j+str(i))


print(lst1)


print('------Python program to get a variable with an identification number or string-----')


x = 100

print(format(id(x), 'x'))

s = 'w3resource'


print(format(id(s), 'x'))


print('------Python program to find common items in two lists----')

lst=["Red", "Green", "Orange", "White"]

lst1=["Black", "Green", "White", "Pink"]

print(set(lst) & set(lst1))


print('------Python program to change the position of every n-th value to the (n+1)th in a list----')

'''
Write a Python program to change the position of every n-th value to the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]
'''



from itertools import zip_longest, chain, tee

def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0, 1, 2, 3, 4, 5]

print(replace2copy(n)) 


#Second Way

#lst=[0,1,2,3,4,5] 


print('------Python program to convert a list of multiple integers into a single integer----')

'''
Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350
'''

lst=[11, 33, 50]
strng=''
for i in lst:
    strng+=str(i)

print(strng)


print('------Python program to split a list based on the first character of a word----')

from itertools import groupby
from operator import itemgetter

word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']


for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)


print('------Python program to create multiple lists----')



obj = {}


for i in range(1, 21):
    obj[str(i)] = []


print(obj) 


print('------Python program to find missing and additional values in two lists----')

'''
Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h
'''



list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']

missing_values = set(list1).difference(list2)


print('Missing values in the second list: ', ','.join(missing_values))


additional_values = set(list2).difference(list1)


print('Additional values in the second list: ', ','.join(additional_values))



print('------Python program to split a list into different variables----')



color = [
    ("Black", "#000000", "rgb(0, 0, 0)"),
    ("Red", "#FF0000", "rgb(255, 0, 0)"),
    ("Yellow", "#FFFF00", "rgb(255, 255, 0)")
]


var1, var2, var3 = color

print(var1)


print(var2)


print(var3)


print('------Python program to generate groups of five consecutive numbers in a list----')



lst=[[5*i + j for j in range(1, 6)] for i in range(5)]

print(lst)


print('------Python program to convert a pair of values into a sorted unique array----')



L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]


print("Original List: ", L)

print("Sorted Unique Data:", sorted(set().union(*L)))


print('--#Second way#--')

L1 = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]

L2=list(dict.fromkeys(L1))

L3=[]
for i in L2:
    for j in i:
        L3.append(j) 

print("Original List: ", L1)

print("Sorted Unique Data:", L3)


print('------Python program to select the odd items from a list----')


lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]

lst=[i for i in lst if i%2!=0]

print(lst)



print('------Python program to insert an element before each element of a list----')



color = ['Red', 'Green', 'Black']


print("Original List: ", color)


color = [v for elt in color for v in ('c', elt)]

print("Updated List: ", color)




print('------Python program to print nested lists (each list on a new line) using the print() function----')


colors = [['Red'], ['Green'], ['Black']]

print('\n'.join([str(i) for i in  colors]))



print('------Python program to convert a list to a list of dictionaries----')

'''
Write a Python program to convert a list to a list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
'''


lst=["Black", "Red", "Maroon", "Yellow"]
lst1=["#000000", "#FF0000", "#800000", "#FFFF00"]


d1=dict(zip(lst,lst1))

print(d1)



print('------Python program to sort a list of nested dictionaries----')


my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

print("Original List: ")
print(my_list)

my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted List: ")
print(my_list) 



print('------Python program to split a list every Nth element----')




C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']


def list_slice(S, step):
    return [S[i::step] for i in range(step)]

print(list_slice(C, 3))


print('------Python program to compute the difference between two lists----')

'''
Write a Python program to compute the difference between two lists.
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
'''

from collections import Counter

lst1=["red", "orange", "green", "blue", "white"]
lst2=["black", "yellow", "green", "blue"]


counter1=Counter(lst1)
counter2=Counter(lst2)

print(list(counter1-counter2))

print(list(counter2-counter1))

#second way
lst3=[]

for i in lst1:
    if i not in lst2:
        lst3.append(i)

print(lst3)

#Third way

lst4=[i for i in lst2 if i not in lst1]

print(lst4)

print('------Python program to create a list with infinite elements----')



import itertools
c=itertools.count()

print(next(c))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print('------Python program to concatenate elements of a list----')


color = ['red', 'green', 'orange']


print('-'.join(color))

print(''.join(color)) 


print('------Python program to remove key-value pairs from a list of dictionaries----')


original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]


print("Original List: ")
print(original_list)


new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]


print("New List: ")
print(new_list)


print('------Python program to convert a string to a list----')

strng='Lists are one of 4 built-in data types in Python used to store collections of data the other 3 are Tuple Set and Dictionary all with different qualities and usage'

lst=strng.split()

print(lst)



print('------Python program to check if all items in a given list of strings are equal to a given string----')


color1 = ["green", "orange", "black", "white"]


color2 = ["green", "green", "green", "green"]

print(all(c == 'blue' for c in color1))

print(all(c == 'green' for c in color2)) 


print('------Python program to replace the last element in a list with another list----')


'''
 Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''

lst1=[1, 3, 5, 7, 9, 10]
lst2=[2, 4, 6, 8]

lst1.pop(-1)

lst1.extend(lst2)

print(lst1)



#Second way



num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]

num1[-1:] = num2

print(num1)


print('------Python program to check whether the n-th element exists in a given list----')

x = [1, 2, 3, 4, 5, 6]

xlen = len(x) - 1

print(x[xlen])


print('------Python program to find a tuple, the smallest second index value from a list of tuples----')


lst=[(4, 1), (1, 2), (6, 0)]

#print(min(lst, key=lambda n: (n[1], -n[0])))

print('------Python program to create a list of empty dictionaries----')

n=5

l=[{} for _ in range(n)]
print(l)




print('------Python program to print a list of space-separated elements----')

num = [1, 2, 3, 4, 5]

print(*num)


print('------Python program to insert a given string at the beginning of all items in a list----')

'''
Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
'''
lst=[1,2,3,4]
strng='emp'

lst1=[strng+str(i) for i in lst]

print(lst1)

print('------Python program to iterate over two lists simultaneously----')


lst1 = [1, 2, 3]
lst2 = ['red', 'white', 'black']

for a,b in zip(lst1,lst2):
    print(a,b)


print('------Python program to move all zero digits to the end of a given list of numbers----')


'''
Write a Python program to move all zero digits to the end of a given list of numbers.
Expected output:
Original list:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Move all zero digits to end of the said list of numbers:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

lst=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
lst1=[]
lst2=[]

for i in lst:
    if i!=0:
        lst1.append(i)
    else:
        lst2.append(i)

lst3=lst1+lst2

print(lst3)



#Second Way



def test(lst):
    result = sorted(lst, key=lambda x: not x) 
    return result


nums = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]


print("\nOriginal list:")
print(nums)

print("\nMove all zero digits to the end of the said list of numbers:")


print(test(nums))


print('------Python program to find the list in a list of lists whose sum of elements is the highest----')

'''
Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
'''

lst=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

#print(max(lst, key=sum))

#second way

lst1=[]

for i in range(len(lst)):
    lst1.append(sum(lst[i]))
    sm=lst1[0]
    for j in lst1:
        if j>sm:
            sm=j

for k in range(len(lst)):
    if sm==sum(lst[k]):
        print(lst[k])

print('------Python program to find all the values in a list that are greater than a specified number----')



list1 = [220, 330, 500]
list2 = [12, 17, 21]


print(all(x >= 200 for x in list1))


print(all(x >= 25 for x in list2))


print('------ Python program to extend a list without appending----')

'''
Write a Python program to extend a list without appending.
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]
'''

lst1=[10, 20, 30]

lst2=[40, 50, 60]
lst2.extend(lst1)
print(lst2)




print('------- Python program to remove duplicates from a list of lists -------')
'''
Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''

# Import the 'itertools' module for working with iterators and grouping
import itertools

# Define a list 'num' containing sublists with integers
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# Print a message indicating the purpose of the following output
print("Original List", num)

# Sort the list 'num', which sorts the sublists lexicographically
num.sort()

# Use 'itertools.groupby' to group similar sublists and retain the first occurrence of each group
new_num = list(num for num, _ in itertools.groupby(num))

# Print a message indicating the purpose of the following output
print("New List", new_num)


print('------- Python program to find items starting with a specific character from a list -------')

'''
Write a Python program to find items starting with a specific character from a list.
Expected Output:
Original list:
['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
Items start with a from the said list:
['abcd', 'abc', 'acjd']
Items start with d from the said list:
['dagfa']
Items start with w from the said list:
[]

'''


lst=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

#chrr=str(input('Which character do you want to start print list :'))

lst1=[]
lst2=[]
lst3=[]
for i in lst:
    if i[0]=='a':
        lst1.append(i)
    elif i[0]=='d':
        lst2.append(i)
    elif i[0]=='w':
        lst3.append(i)
        
print('Original list:')
print(lst)
print('Items start with a from the said list:')        
print(lst1)
print('Items start with d from the said list:')
print(lst2)
print('Items start with w from the said list:')
print(lst3)




print('------- Python program to flatten a given nested list structure -------')

'''
Write a Python program to flatten a given nested list structure.
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

'''

# Define a function 'flatten_list' that takes a nested list 'n_list' as input
def flatten_list(n_list):
    # Initialize an empty list 'result_list' to store the flattened elements
    result_list = []

    # Check if 'n_list' is empty; if so, return an empty result list
    if not n_list:
        return result_list

    # Create a stack to keep track of nested lists; start with 'n_list' as the initial item in the stack
    stack = [list(n_list)]

    # Iterate while the stack is not empty
    while stack:
        # Pop the current list 'c_num' from the stack
        c_num = stack.pop()

        # Pop the next item from 'c_num'
        next = c_num.pop()

        # If 'c_num' is not empty, push it back onto the stack
        if c_num:
            stack.append(c_num)

        # Check if 'next' is a list
        if isinstance(next, list):
            # If 'next' is a non-empty list, push it onto the stack
            if next:
                stack.append(list(next))
        else:
            # If 'next' is not a list, add it to 'result_list'
            result_list.append(next)

    # Reverse 'result_list' to maintain the original order of elements
    result_list.reverse()

    # Return the flattened list
    return result_list

# Define a nested list 'n_list' with various sublists
n_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

# Print a message indicating the purpose of the following output
print("Original list:")

# Print the original nested list 'n_list'
print(n_list)

# Print a message indicating the purpose of the following output
print("\nFlatten list:")

# Call the 'flatten_list' function with 'n_list' as an argument and print the flattened result
print(flatten_list(n_list)) 





print('\nSecond Way----------------->\n')
lst=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
lst1=[]
for i in lst:
    if type(i)==int:
        lst1.append(i)
    else:
        lst1.extend(i)

print('Original list:')
print(lst)
print('\nFlatten list:')
print(lst1)



print('------- Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list -------')


'''
Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

'''




from itertools import groupby

def compress(l_nums):
    return [key for key, group in groupby(l_nums)] 

n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

print("Original list:") 

print(n_list)

print("\nAfter removing consecutive duplicates:")

print(compress(n_list))


print('\nSecond Way----------------->\n')
lst=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

for i in range(len(lst)):
    print(lst[i])







































































 


























