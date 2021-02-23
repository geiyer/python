# Module 1
---
## Interpreter vs Compiler
* What is the difference between an Interpreter & Compiler? 

```html

```
* Python interpreter is installed in /usr/bin/python in mac
* The interpreter operates somewhat like the Unix shell. 
* It reads and executes commands interactively.
* when called with a file name argument, it reads and executes the script from that file.
```python
    python3 /Users/jqfe55e/Documents/python/Module1/math-operators.py
``` 
---

# Variables
Variables are reserved memory locations used to store infromation to be referenced and manipulates. A variable can hold single type of value. 

> # Unlike other languages, Python has no command for declaring a variable.

## Variable Name

It is a good practice to use description name for variable e.g age, total_due, first_name instead of x, y. 

Rules for Python Variables:
- A variable name must start with a letter or underscore character
- A variable name cannt start with a number
- Can only contain alpha-numberic characters and underscore
- Names are case sensitive

### Example
```python

#Legal Variable Name:

age = 25
AGE = 35
_age = 25
print(age)
#Output: 25
print(AGE)
#Output: 35
print(_age)
#Output: 25


#Illegal Variable Name:
1hello = "World"
hello$1 = "World"
hello 1 = "World"

Output: SyntaxError: invalid syntax
```

## Multiple Variables
Multiple variables can be asigned values in a single line:
### Example
```python
first_name, last_name, age = "Jill", "Jackson", 25

print(first_name)
#Output: Jill

print(last_name)
#Output: Jackson

print(age)
#Output: 25

```

### Exercise
Calculate the BMI. The formula for BMI is weight in kilograms divided by height in meters squared. If height has been measured in centimeters, divide by 100 to convert this to meters.

Formula: weight (kg) / [height (m)]2

```python

height = 1.8
weight = 72
bmi = weight/height ** 2
print(bmi)
#Output: 22.222
```
---

# Python Types
Python has the following built-in data types
 - Str : String/Text
 - int, float: To store Numeric data
 - bool: Boolean: true/false
 - list, tuple, range: Array
 - dict: Mapping: key/value

---

# Constants

* What is a constant? 









# How do I create a Constant in Python? 

* First, you cannot delare a variable as constant in Python.
* Python does not have a "read-only" variable. 

* Conventions to create constant 
    * Use Capital Letters
    * Create a seperate file to maintain teh constants. 
### Example
1. Create a constants file and declare 3 constants, PI, SALES_TAX, SHIPPING
2. Create a new file "using-constants.py"
3. Import the constants file using "import" statement and print the constants.

---

# Strongly Typed and Dymanic typing
Python is a stringly-typed language.

* Strong typing
    * Values will not change in ways you do not expect. 
    * A string will not turn into a number unless you explicitly covert it. 

* Dynamic typing 
    * Means the object at run time has a type. 

---

# Arithmetic Operators
### Number Formats
* int: Whole nubers(+/-), Zero
* float: Numbers containing floating decimal points. 
* complex numbers: Mathematical calculations, logarithmic calculations
    * e.g. 3 + 6j
    * Use additional modules like cmath, numpy etc.

    

```python

# Addition
2+7
# Subtraction
2-7
# Multiplication
2*7
# Division:
7/2
# Modulus
7 % 2
# Floor Division
7//2
# Exponent
2**3

```    
### What is the difference between Division & Floor Division? (Assignment)
---
# Type Casting
* Converting One data type to another
* Two Types of casting
    
    * Implicit
        * Convert integer to float e.g. 12 to 12.0
    * Explicit
        * Using predefined functions like
            * int()
            * float()
            * str()    
### Key points to Remember
1. Conversion of one data type to another
2. Implicit conversion is automatically done by the interpreter
3. Avoids loss of data 
4. Explicit type casting is done using predefined functions
5. In Explicit type casting, loss of data may occur.