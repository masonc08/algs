# Python Metaprogramming and Decorators
- metagprogramming is code that modifes another part of the program at compile time

## Closures
- source: https://www.programiz.com/python-programming/decorator
- A function defined inside another function is called a nested function
  - nested functions can access variables inside of the function that contains it
  - these variables are called nonlocal variables
- Closure is when you attach function parameters to another function

```python
def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()
```

- the above code actually outputs "Hello", as the function parameter was stored in the function object returned
- The function is stored independently of the defining function, it will exist even if the function definition is deleted from the current namespace

```python
>>> del print_msg
>>> another()
Hello
>>> print_msg("Hello")
Traceback (most recent call last):
...
NameError: name 'print_msg' is not defined
```

- closures can be used when there is a nested function, that nested function refers to a value defined in the enclosing function, and the enclosing function returns the nested function
- closures allow for factory functions that can return dynamically defined functions

```python
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)
```

- parameters of closure functions can still be accessed by using `.__closure__`

```python
>>> make_multiplier_of.__closure__
>>> times3.__closure__
(<cell at 0x0000000002D155B8: int object at 0x000000001E39B6E0>,)
>>> times3.__closure__[0].cell_contents
3
>>> times5.__closure__[0].cell_contents
5
```
