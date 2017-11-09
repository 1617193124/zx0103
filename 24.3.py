Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> import re
>>> string="abcdefg acbdgef abcdgef cadbgfe"
>>> string
'abcdefg acbdgef abcdgef cadbgfe'
>>> re.findall('\w',string)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'c', 'b', 'd', 'g', 'e', 'f', 'a', 'b', 'c', 'd', 'g', 'e', 'f', 'c', 'a', 'd', 'b', 'g', 'f', 'e']
>>> re.findall ('\w+',string)
['abcdefg', 'acbdgef', 'abcdgef', 'cadbgfe']
>>> 
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adf.com'
>>>  test_list = ['first', 'seconde']
 
  File "<pyshell#9>", line 2
    test_list = ['first', 'seconde']
    ^
IndentationError: unexpected indent
>>> test_list=['first','second']
>>> test_list
['first', 'second']
>>> test_list[0]
'first'
>>> test_list[1]
'second'
>>> for item in test_list:
	print item

	
first
second
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 



>>> 

>>> 

>>> 


>>> 

>>> 


>>> 



>>> 

>>> 


>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> y='tel:010-12345678 address:changanRoad'
>>> re.findall('\d',y)
['0', '1', '0', '1', '2', '3', '4', '5', '6', '7', '8']
>>> re.findall('\d+',y)
['010', '12345678']
>>> re.findall('\d+-',y)
['010-']
>>> re.findall('\d+-\d+',y)
['010-12345678']
>>> 
>>> 
