# 1
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# 1.1
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15

# 1.2
students[0]['last_name'] = 'Bryant'

# 1.3
sports_directory['soccer'][0] = 'Andres'

# 1.4
z[0]['y'] = 30

# 2
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def loopDict(x):
    for i in range(0, len(students)):
        print(
            f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")

loopDict(students)

# 3
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary2(key, someDict):
    for i in range(0,len(someDict)):
      print(someDict[i][key])

iterateDictionary2('first_name', students)

#4

