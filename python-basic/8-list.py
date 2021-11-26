# List
student1 = input("Enter name for student #1: ")
student2 = input("Enter name for student #2: ")
student3 = input("Enter name for student #3: ")
print("The three students are:")
print(student1 + "\n" + student2 + "\n" + student3)

# Defining List
students = ["Alice", "Javi", "Damien"]
print(students)
print(students[2])

# Example of List
my_list = [1, 2, 3]
reals = [4.7, -6.0, 0.22, 1.6]
strs = ['lots', 'of', 'strings', 'in', 'list']
mix = [4, 'hello', -3.2, True, 6]
empty_list = [] 

# Accessing Element
students = ["Alice", "Javi", "Damien"]
print("The three students are:")
print(students[0] + "\n" + students[1] + "\n" + students[2])
print(students[0])
print(students[1])
print(students[2])
print(students[3]) # error

# Setting Element
students = ["Alice", "Javi", "Damien"]
print(students)
# change one student
students[1] = "Delilah"
print(students)

# append()
vegetables = ["lettuce", "cauliflower", "pizza"]
vegetables.append("string bean")
print(vegetables) 

# insert()
vegetables = ["lettuce", "cauliflower", "pizza"]
vegetables.insert(1, "string bean")
print(vegetables)

# remove()
vegetables = ["lettuce", "cauliflower", "pizza"]
vegetables.remove("pizza")
print(vegetables)
vegetables.remove("potatoes") # Error!

# len()
vegetables = ["lettuce", "cauliflower", "pizza"]
print(len(vegetables))

# List interation by elements
smith_siblings = ["Emily", "Monique", "Giovanni"]
for name in smith_siblings:
    print(name + " Smith")

# List interation by index
smith_siblings = ["Emily", "Monique", "Giovanni", "Brianna", "Javi"]
for index in range(len(smith_siblings)):
    smith_siblings[index] = smith_siblings[index] + " Smith"
print(smith_siblings)

# Example 1
names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
for i in range(len(names)):
    if names[i] == "Jon":
        names[i] = names[i] + " Snow"
    else:
        names[i] = names[i] + " Stark"
print(names)

# Example 2
names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
for i in range(len(names)):
    if names[i] == "Jon":
        names[i] += " Snow"
    else:
        names[i] += " Stark"
print(names)

# Checking List membership
superheroes = ["Captain Marvel", "Wonder Woman", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
demoted_hero = str(input("What superhero do you want to eliminate from the top 5?"))
if demoted_hero in superheroes:
    superheroes.remove(demoted_hero)
    print("Top 5 heroes:", superheores)
else:
    print("Hero not found.")

# Slicing
names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
# Slice starting at index 2:
names[2::] # => ["Arya", "Sansa", "Jon", "Robb"], [2:]
# Slice until (not including) index 4:
names[:4:] # => ["Rickon", "Bran", "Arya", "Sansa"], [:4]
# Slice starting at index 2 and until index 4:
names[2:4:] # => ["Arya", "Sansa"], [2:4]
# Slice including only every second name:
names[::2] # => ["Rickon", "Arya", "Jon"]

