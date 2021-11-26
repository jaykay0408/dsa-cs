# Option1 : Create variables for all short and full names
state1 = 'New York'
abbv1 = 'NY'
state2 = 'California'
abbv2 = 'CA'
print(abbv2, "is short for", state2)

# Option2 : Create a list for short-full names
labeled_states = ['NY: New York', 'CA: California', 'TX: Texas']
print(labeled_states[1])

# Option3 : Create two lists for short list and full list
states = ['New York', 'California', 'Texas']
abbvs = ['NY', 'CA', 'TX']
print(abbvs[1] + "is short for" + states[1])

# Option4 : Create list for short, full, short, full …. 
abbvs_and_states = ['NY', 'New York', 'CA', 'California', 'TX', 'Texas']
print(abbvs_and_states[2] + "is short for" + abbvs_and_states[3])

# Use { } and separate elements using comma ,
states = {"NY": "New York", "CA": "California", "TX": "Texas"}
states = {
  "NY": "New York",
  "CA": "California",
  "TX": "Texan"
}

# Using [key], use, change and specify the value for the key
print(states["NY"])  # prints "New York”
states["TX"] = "Texas"
print(states)

# Looping Dictionary
states = {
  "NY": "New York",
  "CA": "California",
  "TX": "Texas"
}
for state in states:
    print(state)

#Display State name
for state in states:
    print(state + " is short for " + states[state])

# Dictionary as data
pet = {
  "name": "Ein",
  "animal": "dog",
  "species": "Corgi",
  "age": 5
}
# Change  pet’s age into 10
# Add “personality” : “mild”
# Create 2 dictionaries pet1, pet2
#Create students dictionary including at least five keys (e.g., name, id, address, grade …)

# Nested Dictionary
pets = [
  {  "name": "Scooby",
    "animal": "dog",
    "age": 5
  },
  { "name": "Klaus",
    "animal": "fish",
    "age": 1
  },
  { "name": "Garfield",
    "animal": "cat",
    "age": 3
  }
]

print(pets[1]["species"])
print(pets[2]["animal"])
print(pets["species"][2])

# [Exercise]
# Display the name of last pet
# Add a new cat “kitty”  (age 1)
# Code a program that can add a new pet  (use loop and  input() function)

# Assymetric Dictionary
# Example of using complex dictionary
user1 = {
  "name": "SpongeBob Squarepants",
  "username": "PattyFlipper1999",
  "animal": "sponge",
  "favorite classes": ["cooking", "jellyfishing", "programming"],
  "credentials": {
    "boating license": False,
    "chef license": True,
    "jellyfishing license": True
  },
  "age": 5
}

#Practice to print each value
