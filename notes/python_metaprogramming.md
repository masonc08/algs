# Python Metaprogramming
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

## Decorators
- Decorators can add functionality to existing code, making it a form of metaprogramming
- functions are methods are called __callable__ as they can be called
- actually functions and methods are just objects that implements `__call__()` magic method
- decorators are a callable that returns a callable

```python
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
```

- in the above example, `make_pretty` is a decorator as it wraps `func`, adding additional functionality to it
- if we run `decorated = make_pretty(ordinary)`, we decorate `ordinary` callable with `make_pretty` callable
  - `make_pretty` then returns the decorated function
- using `@` tags is a shorthand to doing this, where we use the `@make_pretty` tag instead of calling `make_pretty(f)`

```python
@make_pretty
def ordinary():
    print("I am ordinary")

# is equivalent to

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
```

- however, the above implementations does not accept parameters to be passed into the wrapped function
- `@` decorator tags will pass parameters of the enclosed function to the decorator's returned callable by default
- we can simply add parameters to the header of our enclosed function

```python
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)
```

- on this same principle, this means we can also just use `(*args, **kwargs)` as the enclosed function's header
  - this allows us to make the decorator more dynamic, and adapt to decorate different functions
- decorators can also be chained through a series of decorators, where the top decorator is the most outer wrapper

```python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
```

Results in

```
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
```