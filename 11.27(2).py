Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  L = [4,5,6]
 
  File "<pyshell#0>", line 2
    L = [4,5,6]
    ^
IndentationError: unexpected indent
>>> L = [4,5,6]
>>> I = L.__iter__()
>>> L.__next__()

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    L.__next__()
AttributeError: 'list' object has no attribute '__next__'
>>> I.__next__()

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    I.__next__()
AttributeError: 'listiterator' object has no attribute '__next__'
>>> I.__next__()

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    I.__next__()
AttributeError: 'listiterator' object has no attribute '__next__'
>>> from collections import Iterator, Iterable
>>> isinstance(L, Iterable)
True
>>> isinstance(L, Iterator)
False
>>> isinstance(I, Iterable)
True
>>> isinstance(I, Iterator)
True
>>> [x**2 for x in I]
[16, 25, 36]
>>> 
