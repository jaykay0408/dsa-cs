def say_hello():
    print("Hello World!")

say_hello()

def count_vowels(words):
    vowels = "aeiou"
    count = 0
    for letter in words.lower():
        if letter in vowels:
            count = count + 1
    return count

cnt = count_vowels('awesome')
print("Vowels counted: %s" % cnt)
