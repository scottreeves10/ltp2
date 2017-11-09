Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
CashRegister: $2 ($1x2, $2x0, $5x0, $10x0, $20x0)
CashRegister: $2 ($1x0, $2x1, $5x0, $10x0, $20x0)
True
False
>>> ================================ RESTART ================================
>>> 
Neil Young, Harvest Moon (5:03)
Serena Ryder, Stompa (3:15)
>>> ================================ RESTART ================================
>>> 
Canadian Artists (10:35)
1. Neil Young, Harvest Moon (5:03)
2. Serena Ryder, Stompa (3:15)
3. Stompin' Tom Connors, The Hockey Song (2:17)
>>> ================================ RESTART ================================
>>> 
[DEBUG ON]
>>> ================================ RESTART ================================
[DEBUG ON]
>>> 
[DEBUG ON]
>>> ================================ RESTART ================================
[DEBUG ON]
>>> 
Traceback (most recent call last):
  File "C:/Python34/mymods/ltp2/week4/wk4ex1.py", line 21, in <module>
    contact = Contact()
TypeError: __init__() missing 3 required positional arguments: 'first_name', 'last_name', and 'email_address'
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/mymods/ltp2/week4/wk4ex1.py", line 30, in <module>
    paul = Contact()
TypeError: __init__() missing 3 required positional arguments: 'first_name', 'last_name', and 'email_address'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/mymods/ltp2/week4/wk4ex1.py", line 44, in <module>
    paul = Contact(info)
TypeError: __init__() missing 2 required positional arguments: 'last_name' and 'email_address'
>>> ================================ RESTART ================================
>>> 
>>> paulTypeError: __init__() missing 2 required positional arguments: 'last_name' and 'email_address'
SyntaxError: invalid syntax
>>> paul.email
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    paul.email
AttributeError: 'Contact' object has no attribute 'email'
>>> paul.email_address
'paul@example.com'
>>> jen = Contact('Jen', 'Smith', 'jen@example.com')
>>> jen
<__main__.Contact object at 0x0465BA30>
>>> print(jen[2])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(jen[2])
TypeError: 'Contact' object does not support indexing
>>> print(jen.self.email_address)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(jen.self.email_address)
AttributeError: 'Contact' object has no attribute 'self'
>>> print(self.email_address)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(self.email_address)
NameError: name 'self' is not defined
>>> print(jen.email_address)
jen@example.com
>>> ================================ RESTART ================================
>>> 
>>> khaled = Contact('Kahled', 'Jones', 'khaled@example.com')
>>> khaled.first_name
'Kahled'
>>> khaled.add_phone_number(khaled, '555-1111')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    khaled.add_phone_number(khaled, '555-1111')
AttributeError: 'Contact' object has no attribute 'add_phone_number'
>>> khaled.add_phone_number('555-1111')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    khaled.add_phone_number('555-1111')
AttributeError: 'Contact' object has no attribute 'add_phone_number'
>>> ================================ RESTART ================================
>>> 
>>> khaled = Contact('Kahled', 'Jones', 'khaled@example.com')
>>> khaled.add_phone_number(khaled, '555-1111')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    khaled.add_phone_number(khaled, '555-1111')
AttributeError: 'Contact' object has no attribute 'add_phone_number'
>>> haled.add_phone_number('555-1111')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    haled.add_phone_number('555-1111')
NameError: name 'haled' is not defined
>>> dd_phone_number(khaled, '555-1111')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dd_phone_number(khaled, '555-1111')
NameError: name 'dd_phone_number' is not defined
>>> khaled.add_phone_number() = '555-1111'
SyntaxError: can't assign to function call
>>> khaled.first_name
'Kahled'
>>> khaled.add_phone_number(khaled, '555-1111')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    khaled.add_phone_number(khaled, '555-1111')
AttributeError: 'Contact' object has no attribute 'add_phone_number'
>>> khaled.add_phone_number('555-1111')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    khaled.add_phone_number('555-1111')
AttributeError: 'Contact' object has no attribute 'add_phone_number'
>>> add_phone_number(khaled, '555-1111')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    add_phone_number(khaled, '555-1111')
NameError: name 'add_phone_number' is not defined
>>> khaled.add_phone_number() = '555-1111'
SyntaxError: can't assign to function call
>>> 
KeyboardInterrupt
>>> khaled.add_phone_number('555-1111')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    khaled.add_phone_number('555-1111')
AttributeError: 'Contact' object has no attribute 'add_phone_number'
>>> ================================ RESTART ================================
>>> 
>>> khaled.add_phone_number('555-1111')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    khaled.add_phone_number('555-1111')
NameError: name 'khaled' is not defined
>>> khaled = Contact('Kahled', 'Jones', 'khaled@example.com')
>>> khaled.add_phone_number('555-1111')
>>> khaled.phone_number
'555-1111'
>>> khaled.add_phone_number(khaled, '555-1111')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    khaled.add_phone_number(khaled, '555-1111')
TypeError: add_phone_number() takes 2 positional arguments but 3 were given
>>> add_phone_number(khaled, '555-1111')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    add_phone_number(khaled, '555-1111')
NameError: name 'add_phone_number' is not defined
>>> khaled.add_phone_number() = '555-1111'
SyntaxError: can't assign to function call
>>> dir(float)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
>>> help(float.as_integer_ratio)
Help on method_descriptor:

as_integer_ratio(...)
    float.as_integer_ratio() -> (int, int)
    
    Return a pair of integers, whose ratio is exactly equal to the original
    float and with a positive denominator.
    Raise OverflowError on infinities and a ValueError on NaNs.
    
    >>> (10.0).as_integer_ratio()
    (10, 1)
    >>> (0.0).as_integer_ratio()
    (0, 1)
    >>> (-.25).as_integer_ratio()
    (-1, 4)

>>> (0.6).as_integer_ratio()
(5404319552844595, 9007199254740992)
>>> float.as_integer_ratio(float, 0.6)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float.as_integer_ratio(float, 0.6)
TypeError: descriptor 'as_integer_ratio' requires a 'float' object but received a 'type'
>>> Contact.add_phone_number(khaled, '555-1212')
>>> khaled.phone_number
'555-1212'
>>> print(khaled)
<__main__.Contact object at 0x0525DD30>
>>> khaled.last_name
'Jones'
>>> help(list.index)
Help on method_descriptor:

index(...)
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> L = [5, 10, 15, 1, 2, 3]
>>> L.index(3)
5
>>> list.index(3)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    list.index(3)
TypeError: descriptor 'index' requires a 'list' object but received a 'int'
>>> help(str.replace)
Help on method_descriptor:

replace(...)
    S.replace(old, new[, count]) -> str
    
    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.

>>> 'abc 123'.replace('123', '246')
'abc 246'
>>> str.replace('abc 123', '123', '246')
'abc 246'
>>> rorik = Contact('Rorik', 'Henrikson', 'rorik@example.com')
>>> str(rorik)
'<__main__.Contact object at 0x0526F610>'
>>> ================================ RESTART ================================
>>> 
>>> rorik = Contact('Rorik', 'Henrikson', 'rorik@example.com')
>>> str(rorik)
'Rorik Henrikson <rorik@example.com>'
>>> print(rorik)
Rorik Henrikson <rorik@example.com>
>>> ================================ RESTART ================================
>>> 
>>> student1 = Contact('Hugh', 'Z.', 'hugh@fakedomain.com')

student2 = Contact('Kathryn', 'Z.', 'kathryn@fakedomain.com')

student3 = Contact('Karin', 'Z.', 'karin@fakedomain.com')

students = [student1, student2, student3]

subject = 'LTP2: E4 is posted!'

body = 'Hello,\nE4 is posted. Good luck!\n Paul and Jen'

new_email = Email(students, subject, body)
SyntaxError: multiple statements found while compiling a single statement
>>> student1 = Contact('Hugh', 'Z.', 'hugh@fakedomain.com')
>>> student2 = Contact('Kathryn', 'Z.', 'kathryn@fakedomain.com')
>>> student3 = Contact('Karin', 'Z.', 'karin@fakedomain.com')
>>> students = [student1, student2, student3]
>>> subject = 'LTP2: E4 is posted!'
>>> body = 'Hello,\nE4 is posted. Good luck!\n Paul and Jen'
>>> new_email = Email(students, subject, body)
>>> new_email.recipients
[<__main__.Contact object at 0x0461DF10>, <__main__.Contact object at 0x0487B9D0>, <__main__.Contact object at 0x0487B910>]
>>> new_email.recipients[0]
<__main__.Contact object at 0x0461DF10>
>>> print(new_email.recipients)
[<__main__.Contact object at 0x0461DF10>, <__main__.Contact object at 0x0487B9D0>, <__main__.Contact object at 0x0487B910>]
>>> ================================ RESTART ================================
>>> 
>>> new_email = Email([Contact('Kathryn', 'Z.', 'kathryn@fakedomain.com')], 'Hello', 'Hi there!\n Bye for now.')
>>> ================================ RESTART ================================
>>> 
>>> new_email = Email('Hello', 'Hi there!\n Bye for now.')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    new_email = Email('Hello', 'Hi there!\n Bye for now.')
TypeError: __init__() missing 1 required positional argument: 'body'
>>> new_email = Email()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    new_email = Email()
TypeError: __init__() missing 3 required positional arguments: 'recipients', 'subject', and 'body'
>>> ================================ RESTART ================================
>>> 
>>> message = Email([Contact('Paul', 'Gries', 'paul@example.com'), Contact('Jen', 'Campbell', 'jen@example.com')], '2nd MOOC', 'Hi!\nI hope your 2nd MOOC is going well!\nBye :-)')
>>> print(message)
To: Paul Gries <paul@example.com>, Jen Campbell <jen@example.com>, 
Subject: 2nd MOOC
Hi!
I hope your 2nd MOOC is going well!
Bye :-)
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> 
