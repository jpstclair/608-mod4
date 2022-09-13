def cube_list(values):
	for i in range(len(values)):
		values[i] **= 3

 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

student_tuple = ('John', 'Jacob', 'Jingleheimer')

student_tuple = ('Amanda', 'Johnson', [98, 85, 87])


first_names = ['Amanda', 'John', 'Kevin']

grades = [98, 85, 87]

print('\nStClairCreating a Bar Chart from numbers:')
print(f'{"First Name"}{"Value":>8}   Bar')

for index, value in enumerate(grades):
	print(f'{first_names:>5}{value:>8} {"*" * value}') 

{1, 3, 5}.issuperset({3, 5, 1})

set('abc def ghi jkl mno').issuperset('hi mom')

In [1]: a = [7, 28, 29, 30, 40, 2]

In [2]: b = [3, 9, 30, 64, 65, 13]

In [3]: c = [21, 23, 20, 46, 63, 26]

In [4]: c[0]
Out[4]: 21

In [5]: c[4]
Out[5]: 63

In [6]: len(c)
Out[6]: 6

In [7]: b(-1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [7], in <cell line: 1>()
----> 1 b(-1)

TypeError: 'list' object is not callable

In [8]: b[-1]
Out[8]: 13

In [9]: c[100]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Input In [9], in <cell line: 1>()
----> 1 c[100]

IndexError: list index out of range

In [10]: c[0]+c[1]+c[2]
Out[10]: 64

In [11]: a + c
Out[11]: [7, 28, 29, 30, 40, 2, 21, 23, 20, 46, 63, 26]

In [12]: characters = []

In [13]: characters += 'Birthday'

In [14]: characters
Out[14]: ['B', 'i', 'r', 't', 'h', 'd', 'a', 'y']

In [15]: def cube_list(values):
    ...:     for i in range(len(values)):
    ...:         values[i] **= 3
    ...:

In [16]: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

In [17]: cube_list(numbers)

In [18]: numbers
Out[18]: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

In [19]: James StClair
  Input In [19]
    James StClair
          ^
SyntaxError: invalid syntax


In [20]: from collections import Counter

In [21]: text = ('Its the circle of Life, and it moves us all '
    ...:         'Through despair and hope, through faith and love'
    ...:         'Til we find our place, on the path unwinding'
    ...:         'In the circle, the circle of life')

In [22]: counter = Counter(text.split())

In [23]: for word, count in sorted(counter.items()):
    ...:     print(f'{word:<12}{count}')
    ...:
Its         1
Life,       1
Through     1
all         1
and         3
circle      2
circle,     1
despair     1
faith       1
find        1
hope,       1
it          1
life        1
loveTil     1
moves       1
of          2
on          1
our         1
path        1
place,      1
the         4
through     1
unwindingIn 1
us          1
we          1

In [24]: {1, 3, 5} == {3, 5, 1}
Out[24]: True

In [25]: {1, 3, 5} != {3, 5, 1}
Out[25]: False

In [26]: {1, 3, 5} >= {3, 5, 1}
Out[26]: True

In [27]: {1, 3, 5}.issuperset({3, 5, 1})
Out[27]: True

In [28]: set(' abc def ghi jkl mno').issuperset('hi mom')
Out[28]: True

In [29]: def James_StClair
  Input In [29]
    def James_StClair
                     ^
SyntaxError: invalid syntax