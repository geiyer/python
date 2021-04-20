# Introduction
* Check the grades & review feedback in rubrick
* Developer Survey
---

# Strings
* Built-in string class named str
* String literals can be enclosed in either double quotes or single quotes

```python

    print("Hello World")
    print('Hello World')
    print('I\'m doing good') # backslash escapes
    print('This is a paragrah \
        that I want to be printed \
            in three lines')
```    
* Strings are "immutable" which means they cannot be changed once created
* When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.


```python
x = 'Hello'
y = 'World'
#What do you expect? 
x+y
#What is the result?
```

# Class Work:

### Which of this expression with throw an error? 
### Why? 

```python
"I can add integers, like " + str(5) + " to strings."
"I said " + ("Hello " * 2) + "World!"
"I can add 2 to this string  " + 2
True + False
```

## String Methods:
1. lower(), capitalize()
2. upper()
3. startswith('hello') ; endswith('world')
4. replace('hello', 'new')
5. len()

```python
s = 'hello World'
print(s.lower())
print(s.capitalize())
print(s.upper())
print(s.startswith('hello'))
print(s.startswith('Hello')) #What happened? 
print(s.endswith('world'))
print(s.replace('hello', 'new'))
print(len(s))


```
# Format Strings
3 ways to format
* % formatting
* format
    * improvement on % formattting
    * Format by positions
    * Format by names
    * Align Text
    * Number formatting
* Improved way: 
    * F-string

```python
    name = 'Gopi'
    'hello %s. ' % name
    # format method
    'My name is {0}, zip code: {1}; state : {2}'.format('Gopi', '11111','IA')
    'My name is {name}, zip code: {zip}; state : {state}'.format(name = 'Gopi', zip = '11111', state = 'IA')
    '{:<20}'.format('left')
    '{:>20}'.format('right')
    '{:^20}'.format('center')
    '{:*^20}'.format('center') #fill the space with *

    '{:+f}; {:+f}'.format(10, -10)# Display + or - always
    '{: f}; {: f}'.format(10, -10)# Display space for + numbers
    '{:-f}; {:-f}'.format(10, -10)# Show only the negative sign
    '{:,}'.format(10000)# Comma seperator
    '{:.2%}'.format(10.2285/100)# Show %
    #f-Strings
    my_variable = 'some text'
    my_other_var = 'specific location'
    
    print(f'F-strings allow you to output {my_variable} in a {my_other_var} easily')
    my_number = 10000
    print(f'{my_number:,}') # Comma seperator

```

---
## Recap:
float - real numbers
int - integer numbers
str - string, text
bool - True, False






---
# List

* Measure the store the name of all students in this class
* There are many data points
```python
student1 = 'Matt'
student2 = 'Rodd'
student3 = 'Gopi'
#And many more; upto 15+ more variable.
```
* Inconvient
* Instead, store them in a list

* It is a way to give Single Name for a collection of values
* Contain any type
* Contain different type
* List can contain lists too

|   0          |  1         |  2         |
| :----------- | :--------: | ---------: |
| 'Gopi'       | 'Rodd'     | 'Matt'     |


```python
['Gopi', 'Rodd' ,'Matt']
['Gopi', 123, 'Rodd', 234, 'Matt', 262]

course1 = ['Gopi', 123, 'Rodd', 234, 'Matt', 262]
course2 = [['gopi', 123], ['Rodd', 234], ['Matt', 262]]
type(course1)
type(course2)
print(course1[0])
print(course1[1])

```

## Methods
```python
states = ['IA', 'CA', 'IL']
states.append('NY') # Adds to the end of the list
states.insert(1, 'GA') # Adds at the first index
states.index('GA')
states.sort()
states.reverse()
states.pop(1)
```
# Inputs 
age = input("Enter your age: ")


---
# Classroom Work:

* Interest Calculator:
    * Current Principal (P): 100
    * Rate of Interest (r) : 10 % = 0.1
    * Number of Years (t): 3
    * Simple Interest Formula: 
        * Future Value = P*(1+rt)
    * Compound Interest Formula: 
        * Future Value = P(1+r)^t (power)
* Question: Which is better ? 
* Print "If you start with ${Principle}, you should have ${future value} in ${Years}. "



