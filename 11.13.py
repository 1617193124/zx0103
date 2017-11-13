Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = {'abc':456}
>>> dict1
{'abc': 456}
>>> dict1['abc']
456
>>> dict1['ddd']

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dict1['ddd']
KeyError: 'ddd'
>>> dict1['abc']
456
>>> dick1['ddd']

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dick1['ddd']
NameError: name 'dick1' is not defined
>>> dict1['abc']
456
>>> dict1['abc']=678
>>> dict1['abc']
678
>>> del dict1['abc']
>>> dict1
{}
>>> users= {
	'A':{
	'first':'yu',
	'last':'lei',
	'location':'hs',
	},
	'B':{

		
        'last':'wei',
	'location':'hs',
	},
}
>>> 
>>> for username, userinfo in users.items():
	print("userid:"+username)
	print("userinfo:"+str(userinfo))

	
userid:A
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
userid:B
userinfo:{'last': 'wei', 'location': 'hs'}
>>> dict = {'Name': 'Zara', 'Age': 7}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>> for key in dick.keys():
	print key

	

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    for key in dick.keys():
NameError: name 'dick' is not defined
>>> for key in dict.keys():
	print key

	
Age
Name
>>> for key in dict.keys():
	print dict[key]

	
7
Zara
>>> 
