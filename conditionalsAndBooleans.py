if True:
    print ('conditional was true')
if False:
    print ('conditional was true')
language = 'python'
if language == 'python':
    print ('conditional was true')
language = 'python'
if language == 'python':
    print ('language is python')
else:
    print ('No match')
language = 'python'
if language == 'java':
    print ('language is python')
else:
    print ('No match')
language = 'java'
if language == 'python':
    print ('language is python')
elif  language == 'java':
    print ('language is java')
else:
    print ('No match')
language = 'java'
if language == 'python':
    print ('language is python')
elif  language == 'javaScript':
    print ('language is javaScript')
else:
    print ('No match')
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print ('Admin page')
else:
    print ('Bad creds')
user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print ('Admin page')
else:
    print ('Bad creds')
user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print ('Admin page')
else:
    print ('Bad creds')
user = 'Admin'
logged_in = False
if not logged_in:
    print ('please log in')
else:
    print ('welcome')
a = [1, 2, 3]
b = [1, 2, 3]
print (a == b)
a = [1, 2, 3]
b = [1, 2, 3]
print (a is b)
a = [1, 2, 3]
b = [1, 2, 3]
print (id(a))
print (id(b))
print (a is b)
a = [1, 2, 3]
b = a
print (id(a))
print (id(b))
print (a is b)
a = [1, 2, 3]
b = a
print (id(a))
print (id(b))
print (a == b)
condition = False
if condition:
    print ('Evaluated to True')
else:
    print ('Evaluated to False')
condition = None
if condition:
    print ('Evaluated to True')
else:
    print ('Evaluated to False')
condition = 0
if condition:
    print ('Evaluated to True')
else:
    print ('Evaluated to False')    
condition = 10
if condition:
    print ('Evaluated to True')
else:
    print ('Evaluated to False')
condition = []
if condition:
    print ('Evaluated to True')
else:
    print ('Evaluated to False')
condition = ''
if condition:
    print ('Evaluated to True')
else:
    print ('Evaluated to False')
condition = {}
if condition:
    print ('Evaluated to True')
else:
    print ('Evaluated to False')
condition = 'test'
if condition:
    print ('Evaluated to True')
else:
    print ('Evaluated to False')    
