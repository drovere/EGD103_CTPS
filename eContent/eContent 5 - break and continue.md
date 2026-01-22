# `break`
`break` is a Python key word that can be used within loops (eg. for loop, while loop). `break` will exit out of the current loop when executed.


```python
# example - finding the first vowel in a piece of text
text = 'Welcome everybody'
first_vowel = None
for char in text:
    if char in 'aeiou':
        first_vowel = char
        break # exits out of the loop as soon as we find the first vowel
first_vowel
```

```plaintext {.output}
'e'
```



# `continue`
`continue` is a Python key word that can be used within loops. `continue` will skip to the next iteration of the current loop when executed.


```python
# example - removing vowels from a piece of text
text = 'Welcome everybody'
new_text = ''
for char in text:
    if char in 'aeiou':
        continue # skip to the next iteration of the loop, since it is a vowel
    new_text = new_text + char
new_text            
```

```plaintext {.output}
'Wlcm vrybdy'
```


    

