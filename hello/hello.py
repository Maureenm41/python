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

#2name = "James"
#-name = "Bond"
#My name = "Bond"

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

prof = [first_name , last_name]

print (prof)

age = "42"


job = "mathematicien"

txt = f"Hello, my name is {first_name} {last_name} and i am {age} years old and i am a {job}"
print(txt)


# ex 2
a = 10
b = 20

add = a+b
print (add)

sub = b- a
print (sub)

multi = a * b

print(multi)

div = b / a
print(div)

floorDiv = b // a
print(floorDiv)

modulus = b % a
print("modulus :" , modulus)
modulus2 = 21 % 2
print("mudulus2 :", modulus2)

exp = a**2
print(exp)

# ex2 p2

a = 10
b = 20
print(a==b)
print(a==10)

print(a!=b)
print(a!=10)

#print(a<>b)
#print(a<>10)

print(a>b)
print(b>a)

print(a>=b)
print(b>=a)

print(a<b)
print(b<a)

print(a<=b)
print(b<=a)

# ex2 p3

a = 10
name = "Alan Turing"

print(a)
print(name)

a += 10
name += "is a good mathematician"

print(a)
print(name)

#name += a ; # same as "name = name + a"
#a += name ; # same as "a = a + name"

a = 20
a -= 10
print(a)

#name -="Alan Turing"

a = 10
a *= 10
print(a)

text = "Alan Turing"
text *=10
print(text)

a = 100
a /= 10
print(text)

a = 100
a %=3
print(a)

a = 2
a **=3
print(a)

a = 20
a //= 3
print(a)

# drill ex

age = 42
add = age + 10
print(add)

age = 42
age /= 7
print(divAge)

textDiv = age + "divided by 7 is equal" + age /= ;
print(textDiv)