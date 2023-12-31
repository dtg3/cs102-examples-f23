# In Python, any line that begins with a # (hashtag, pound sign,
#	or octothorpe) is considered a comment and will be ignored by
#	the Python interpreter. It is not necessary to comment every
#	single line of a program (as it makes it harder to read), but
#	we use comments to explain parts of the code that might not be
#	obvious to someone else or just as reminders to ourselves.

# When we type specific values into our code (usually strings or numbers)
#	these are referred to a literals. The name makes sense as they are
#	"literally" the value being stored or used. In the example below, "hello" is a
#	string literal.
print("hello")

# Above we used a function called print() to display the string literal: hello
#	A function is some kind of operation or action that we can do with our code
#	functions can have zero or more inputs (arguments) to them contained within the parenthesis.
#	In our example print is taking one argument which is the string "hello".
#	All of the following are equivalent ways to create and print a string literal.
print('hello')
print('''hello''')
print("""hello""")

# The triple quoted strings support multiple lines so you can so something like this
print('''Hello everyone,
I hope you are having fun today''')

# The following creates a variable and assigns it to the string: hello
#	In Python, a variable is simply a name that acts as a label so we
#	can refer to some kind of data we need. By convention, when we create
#	a variable, we name it using snake_case. That is all lower case letters
# with underscores in between.
my_variable = "hello"

my_other_variable = my_variable

# In the code above, my_other_variable and my_variable both refer to the
#	same string: hello
#	This is not an instance of using a literal as my_variable could refer
#	anything at all, but it just happens to reference "hello".

# What do you think will happen if I change my_variable to a different string?
my_variable = "goodbye"

# My variable is now refers to the string: goodbye
#	but what about my_other_variable. Let's display the value and find out!
print(my_other_variable)

# Is it strange that it says "hello"? We'll talk more about this as class
#	goes on, but for now, a way to think of it is we that didn't change "hello" to "goodbye",
#	we only changed what the label my_variable references. "hello" still exists, and
#	my_other_variable wasn't told to refer to something else, so it stays right where it is. 

# When creating variable, make sure you follow the rules outlined in the book to ensure that
#	it is a valid name. Variables:
#		* cannot start with numbers
#		* can only contain letters, underscores, and numbers (NO SPACES)
#		* should not be named after existing Python functions or keywords
#		* need to have concise and descriptive names

# SPELLING AND CASE ARE IMPORTANT! The variable Message is not the same as message!

# Our strings in Python support a variety of actions that can be performed on the data.
my_new_string = "objects aRE coOL"
print(my_new_string.upper())
print(my_new_string.lower())
print(my_new_string.swapcase())
print(my_new_string.replace("o", "i")) # Note case senstive ("o" is not "O")
print(my_new_string.replace("objects", "sandwiches"))
print(my_new_string.title())
print(my_new_string.removeprefix("obj"))
print(my_new_string.removesuffix("coOL"))
print(my_new_string.find("a")) # Why do we get a number....we'll talk more about that later

#One important thing to note is that ALL of these functions create a brand new string. None
#	of them change the original string. This is because strings are immutable (unable to be
#	changed).

# So far we have just printed out one variable or literal. What if we wanted to print more?
#	The print function can output multiple pieces of data in a single statement. By default it
#	puts a space in between each piece of data (or argument) and then follows it up with a newline.
print("What", "about", "this?")

# This seems a little awkward...what if I wanted to do something like print my name in a sentence.
my_name = "drew"
print("Hello, my name is", my_name.title(), ", nice to meet you!")

# Yuck, and I can't get the second comma to appear properly as well. Luckily, I don't have to do
# this. We can insert variables anywhere in a string using an f-string (format string).

greeting = f"Hello, my name is {my_name.title()}, nice to meet you!"
print(greeting)

# This is much better! The leading "f" informs Python that it will need to look for curly braces {}
#	and run any of the code within them. When it's done, the result is a string with the data inserted
#	at the location of the braces. Isn't that neat!
