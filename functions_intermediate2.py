x = [[5, 2, 3], [10, 8, 9]]

x[1][0] = 15
print(x)

print()

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'

print(sports_directory)

print()

z = [{'x': 10, 'y': 20}]

z[0]['y'] = 30
print(z)

print()

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

for students in students:
    for key in students:
        print(f"{key} - {students[key]}")

print()


def iterateDictionary(key, students):
    for s in students:
        print(s[key])


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary('first_name', students)

iterateDictionary('last_name', students)

print()


def printInfo(some_dict):

    print(len(some_dict['locations']), "LOCATIONS")

    for location in some_dict['locations']:

        print(location)

    print()

    print(len(some_dict['instructors']), "INSTRUCTORS")

    for location in some_dict['instructors']:

        print(location)


dojo = {

    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],

    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']

}

printInfo(dojo)
