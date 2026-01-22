# Data types

So far in the unit, we have been thinking of a value as just a number. In programming, values are much more broad than this - a value could represent something non-numeric like the text "Hello world!" or could represent a sequence of numbers like [1, 2, 3, 4, 5]. These different values each fall under a particular data type. In python, you can find the data type of a value using the type function:

```python
type(value)
```

For example, the type of the value 5 is an integer.

```python
type(5)
```

```plaintext {.output}
int
```

Of course, this can be used with variables too.

```python
my_lucky_number = 7
type(my_lucky_number)
```

```plaintext {.output}
int
```

***

# Simple data types

The table below summarises some simple data types we would expect you to use at this point of the unit. As you progress, you will be introduced to many more data types.

| Data type | Description | Examples |
| --- | --- | --- |
| `int` | An integer value | `5, -2, 0` |
| `float` | A real number described as a decimal | `4.3, -7.9, 5.0` |
| `complex` | A complex number | `3 + 4i, 7 - 2j, 2 + 0j` |
| `str` | A string. This is a sequence of characters that form a piece of text. | `"Hello world"`, `"500"` |

***

# Why is data type important?

Data types determine how objects interact with operators and functions. They also effect methods and attributes of an object (you will learn about these next week). For example, consider the + operator. 

If we use the + operator with numeric values, it will add them together.

```python
5 + 1
```

```plaintext {.output}
6
```
 

If we use the + operators with strings, it will concatenate (join them) together.

```python
'5' + '1'
```

```plaintext {.output}
'51'
```

If we have mixed data types, Python will often return a type error.

```python
5 + '1'
```

```python {.error}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[11], line 1
----> 1 5 + '1'

  TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Thankfully, Python supports arithmetic with mixed data types if they are all numeric.

```python
5 + 10.1
```

```plaintext {.output}
15.1
```
 
As you learn about different data types, it is important to understand their unique properties.

***

# Converting data types

In Python, most data types will have a function that shares the same name as the data type that will attempt to convert a value into that type. For example, consider the have the number 5.0 which is a float. Some example type conversions are below.

```python
# convert to an integer
int(5.0)
```

```plaintext {.output}
5
```

```python
# convert to a complex number
complex(5.0)
```

```plaintext {.output}
(5+0j)
```

```python
# convert to a string
str(5.0)
```

```plaintext {.output}
'5.0'
```

***

# Everything is an object!

One useful characteristic of Python is that everything is an object, and so has a data type associated with it. Blocks of code such as functions and modules have data types. Even the representation of nothing has a data type (None). 

---

# Video Recap

Watch the video below for a recap and demonstration of the above concepts.