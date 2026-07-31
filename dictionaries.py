student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print (student['name'])
print (student['courses'])
student = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print (student[1])
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print (student.get('name'))
print (student.get('phone'))
print (student.get('phone', 'not found'))
student = ('name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'])
student ['phone'] = '555-5555'
print (student.get('phone', 'not found'))
student {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student ['phone':] = '555-5555'
student ['name'] = 'Jane'
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print (student)
student = ('name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'])
age = student.pop('age')
print (student)
print (age)
student = ('name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'])
print (len(student))
print (student.keys())
print (student.values())
print (student.items())
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
for key, value in student.items():
    print (key, value)

