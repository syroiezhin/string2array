# <p id="UP">Want to create an array of numbers from a row?</p>

## <p align="center">Give thanks : <u>5168 7450 1701 5535</u> <a href="https://en.privatbank.ua/all-ways-to-receive-send-an-international-transfer"><img src="https://upload.wikimedia.org/wikipedia/uk/f/ff/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%8224.png" width = "25" alt="Privat Bank UA"> </a></p>

<br>

***To solve this problem we need:***
1. Variable `str` with numbers separated by spaces and/or other characters;
2. The variable `symbol = str[enumerator]`, which will acquire the value of one character from the __str__ variable;
3. Variable `enumerator`, which will count the number __symbol__ in the string __str__;
4. Variable `overwriting += symbol`, which will be filled with numbers with the __symbol__ variable that have been filtered.
5. The `result` variable, which is an array of the desired numbers.

<br>

***Let's start parsing the code:***
> Condition for exiting the work program.
```python
while enumerator < len(str)
```
> Condition, to filter each __symbol__ in string __str__.
```python
while '0' <= symbol <= '9' or symbol == '.':
    overwriting += symbol
    enumerator += 1
    if enumerator < len(str): symbol = str[enumerator]
```

> From now on, we determine if we could find at least some number that was written to the __overwriting__ variable:
```python
if overwriting != ''
```
> In this block of the program, the process of editing the received data from unnecessary characters occurs, which leads to a failure.

> 1. First, we need to make sure that there are no extra signs after the first comma in the decimal fraction.
> To do this, we rewrite our fraction backwards `overwriting[::-1]`. Let's find all the extra points `.split(".", n-1)` in the amount of __n-1__ to replace them with an empty value `''.join(...)`. To find out how many points in the variable "overwriting" use this `.count('.')`. To assign a value from the comparison formula to the variable __n__, we use the Walrus operator `n := overwriting.count('.')`.
```python 
if ( n:=overwriting.count('.') ) > 1: 
    overwriting = (''.join(overwriting[::-1].split(".", n-1)))[::-1] 
```
> 2. We also need to make sure that the __overwriting__ variable stores any characters other than the dot. ***If it turns out that the variable consists of a single dot, then we will assign the value zero to the parameter.***
```python 
if overwriting == '.' or float(overwriting) == 0: 
    overwriting = '0'
```
> 3. But if we make sure that our symbol does not consist of zeros or one dot, then we get to the last block of code. In this block, we will remove all extra zeros at the beginning of the number and extra zeros after the decimal point at the end of the number. It is also worth considering the case that the number can begin with a dot, in which case we will put zero before the dot!
```python 
else:                 
    while overwriting[0] == '0': 
        overwriting = overwriting[1:]
    while overwriting[0] == '.': 
        overwriting = (overwriting[::-1] + "0")[::-1]
    while overwriting[-1] == '0': 
        overwriting = overwriting[:-1]
```

[⇪](#UP)
