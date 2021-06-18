msg = "Hello World"
print(msg)

msg
msg.capitalize()
msg.split()

def foo(x):
    if x == 0:
        bar()
        baz()
    else:
        qux(x)
        foo(x - 1)


# My first comment 
name = "BeCode" # Name of school

"""
This is a multiline
comment.
"""


word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
print(word)
print(sentence)
print(paragraph)

2name = "James"
-name = "Bond"
My name = "Bond"

name = "Bond"
print("Your name is", name)

last_name = "Bond"
first_name = "James"
text = "My name is {}, {} {}.".format(last_name, first_name, last_name)
print(text)


age = "26"
first_name ="Maureen"
text = "Hello, my name is {} and i am {}".format(first_name, age)
print(text)

first_name = "James" # String
last_name = "Bond"  # String
age = 39  # Integer
weigth = 81.56 # Float
double_agent = True # Boolean
login = "007" # String
agent = [first_name, last_name, age, weigth, double_agent, login] # List
print(agent)


print(first_name, type(first_name))
print(last_name, type(last_name))
print(age, type(age))
print(weigth, type(weigth))
print(agent, type(agent))

#Exercices

#1 Create a variable name that contains the value "Alan Turing"

first_name = "Alan"

last_name = "Turing"

mathematician = [first_name , last_name]

print (mathematician)

number = "42"