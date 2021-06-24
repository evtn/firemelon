# firemelon - a *simple password* generator

## Why?

Passwords don't have to be something like `GY/hyTJmw#B$E3,x`.    
Simple combinations like `sure,happy,95194,sad` or `2874;people;only;penguin` are also pretty strong (see below).    
But those are also easy to remember (and you can even turn it into some drawing to remember while still keeping it a secret)    

This module is doing exactly that - creating passwords using random words and, sometimes, numbers.    

### Is it really strong?

- It is pretty diverse:
    - With default settings (`complexity=4, sep=random`) you get `5687377896504960` different passwords
    - With one specific separator (or no separator at all) you get `975201971280` different passwords - significantly less, still many.
    - With one specific separator (or no separator at all) and `complexity=3` you get `2636311808` different passwords - still many.
- You definitely should use 2FA for important accounts, no matter how strong is your password.
- Decent services should have a cooldown for too many wrong password attempts
- Most passwords are stolen (e.g. with phishing), not brute-forced, those have nothing to do with password strength
- Use different passwords for different accounts (or at least don't use the same password everywhere), of course

## Installation

As simple as `python -m pip install firemelon`    

## Basic usage

```python
from firemelon import passgen

# complexity=4, sep=random, use_number=True
print(passgen()) # "hot_legal:498;goose"
```

## Into the deep

If you want to change generation options, pass `complexity` and `sep` params:

```python
from firemelon import passgen

print(passgen(complexity=2, sep=":", use_number=False)) # "idea:night"
```

Complexity just sets how much parts the result will have, and sep is a separator between parts.    
If you won't pass `sep`, every separator in password would be chosen at random.    
`use_number` is pretty straightforward.

### Generator

If you want to go even further and construct a password yourself, you'll need a `Generator`:    

```python
from firemelon import Generator as gen

password = "".join([gen.adjective(), " ", gen.noun(), gen.sep(), gen.number(3)]) # "pure fish,268"

print(password)
```

## Contributing

Why? It's finished. 