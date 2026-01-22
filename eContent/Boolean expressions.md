# Boolean expressions

Boolean, named after the mathematician [George Boole](https://en.wikipedia.org/wiki/George_Boole), is a data type that can only have one of two values: `True` or `False`. They are also referred to as **logical** values.

In Python, the `bool` type is used to represent boolean values.

Like any other data type, boolean values can be assigned to variables.

```python
first_logic = True
second_logic = False
first_logic, second_logic # Display both values
```

```plaintext {.output}
(True, False)
```

---

# Relational operators

Boolean values are often not assigned directly, but are often the result of a truth test (i.e., a comparison, or the combination of multiple comparisons). In Python, the following **relational operators** are used to compare values.

| Operator | Example Expression | Meaning |
|----------|---------|---------|
| `==` | `x == y` | Is `x` equal to `y`? **Not to be confused with the assignment operator `=`.** |
| `!=` | `x != y` | Is `x` not equal to `y`? |
| `<` | `x < y` | Is `x` less than `y`? |
| `>` | `x > y` | Is `x` greater than `y`? |
| `<=` | `x <= y` | Is `x` less than or equal to `y`? |
| `>=` | `x >= y` | Is `x` greater than or equal to `y`? |

The result of a relational operator is a boolean value. For example:

```python
small_number = 5
medium_number = 10
large_number = 15
```

Then the following expressions all evaluate to `True`:

```python
small_number < medium_number
medium_number > small_number
medium_number != large_number
small_number <= 200
```

And the following expressions all evaluate to `False`:

```python
small_number > 8
medium_number < small_number
medium_number == large_number
small_number >= large_number
```

Similar to arithmetic operators like `+` and `-`, relational operators (except for `==` and `!=`) are mostly not defined for mixed data types. For example, the following expressions are invalid:

```python
5 < "5"
```

```python {.error}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[12], line 1
----> 1 5 < "5"

TypeError: '<' not supported between instances of 'int' and 'str'
```

```python
False < "False"
```

```python {.error}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[17], line 1
----> 1 False < "False"

TypeError: '<' not supported between instances of 'bool' and 'str'
```

But the following expressions are valid:

```python
5 < 5.0
```

```plaintext {.output}
False
```

```python
5 != "5"
```

```plaintext {.output}
True
```

```python
0 < True # Yes, this is valid, since True is equivalent to 1, and False is 0
```

```plaintext {.output}
True
```

---

# Logical operators

**Logical operators** are used to combine multiple boolean values or expressions into a single boolean value. The following logical operators are used in Python:

| Operator | Example Expression | Meaning |
|----------|---------|---------|
| `and` | `x and y` | Are `x` **and** `y` both `True`? |
| `or` | `x or y` | Is `x` **or** `y` `True`? |
| `not` | `not x` | Is `x` `False`? |

For example, consider how each of the above operators work in some engineering problems:

#### **Example 1 (Safe Motor Conditions)**: We have a motor that only operate safely **if both the temperature is below 100 degrees and the pressure is below 200 psi**. We can use the `and` operator to check if both conditions are met.

```python
temperature = 90
pressure = 150
is_safe = temperature < 100 and pressure < 200
is_safe
```

```plaintext {.output}
True
```

If we change the temperature to 110, the result will be `False`, as the temperature is now above 100.

```python
temperature = 110
pressure = 150
is_safe = temperature < 100 and pressure < 200
is_safe
```

```plaintext {.output}
False
```

#### **Example 2 (Circuit Malfunction)**: We have an electric circuit that will malfunction if **either the voltage is above 10 V or the current is above 5 A**. We can use the `or` operator to check if either condition is met.

```python
voltage = 12
current = 4
is_malfunction = voltage > 10 or current > 5
is_malfunction
```

```plaintext {.output}
True
```

The circuit will **NOT** malfunction if both the voltage and current are below the threshold.

```python
voltage = 9
current = 4
is_malfunction = voltage > 10 or current > 5
is_malfunction
```

```plaintext {.output}
False
```

#### **Example 3 (Full Water Tank)**: We have a sensor that can detect the water level in a tank that is 100 meters tall. We want to know if the tank is **not full**. We can use the `not` operator to check if the tank is not full.

```python
water_level = 80
is_not_full = not water_level >= 100
is_not_full
```

```plaintext {.output}
True
```

If the water level is 100, the result will be `False`.

```python
water_level = 100
is_not_full = not water_level >= 100
is_not_full
```

```plaintext {.output}
False
```

---

# Video Recap

Watch the video below for a recap and demonstration of the above concepts.