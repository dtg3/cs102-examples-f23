# While we have been writing all of our code in one file
#	it can be very useful to break up our code into multiple
#	separate files. Many developers (including the creators
#	of Python) include extra features within different files
#	or packages called "Modules". In this example, we will
#	use the random module in this example.

# To use code modules you need to import them. The book shows
#	many different way to import modules, and to even give them
#	aliases, but for now, this is sufficient.
import random

print("RANDOMNESS")
# The random module provides us with the ability to generate
#	pseudorandom numbers. We call them pseudorandom because they are
#	generated by an algorithm to appear random. This algorithmic approach
#	to random number generation usually leads to a distribution of
#	potential values. This means with enough samples, it may be possible
#	to guess the next number in a sequence. Pseudorandom numbers are good
#	enough for games, simulations, or other lower stake applications.

# "True" random numbers requires and external source of randomness. Things
#	like current position of the mouse at a given point in time, solar
#	radiation partical bombardment, etc. Events that cannot be predicted. 


# Psuedorandom number generators usually require the algorithm to be "seeded"
#	with a value to being the random generation. Many modern games like Minecraft,
#	Terraria or other titles that use randomness allow the generator to be provided
#	a seed value. If two people use the same seed, the random number generator
#	will create the same set of random output. In Python, if you do not seed the
#	random number generator, it will simply use the current system time on your computer.

# To use the random module, we have to first use the name of the module we
#	imported, and then we can use functions within that module using a similar
#	notation to calling methods.

# The call to the random() function from the random module
#	gives a random float between 0.0 and 1.0
print(random.random())

# The call to the randrange() function from the random module
#	gives a number between a given range where the start is inclusive
#	and the end is exclusive (just like range)
print(random.randrange(3, 27)) # Possible values 3 to 26
print(random.randrange(-10, 11)) # Possible values -10 to 10
print(random.randrange(10, -11, -1)) # Possible values 10 to -10 (Note the step -1)

# The call to the randint() function from the random module
#	gives a number between a given range where BOTH the start and
#	end are inclusive
print(random.randint(3, 27)) # Possible values 3 to 27
print(random.randint(-10, 11)) # Possible values -10 to 11

# You can also have random help you support picking random items from collections
#	like lists, strings, tuples, etc.
friends = ['joy', 'ted', 'joe', 'sarah', 'parker']

# Maybe you'd like to give a gift to a random friend...
print(f"A gift for: {random.choice(friends)}")
# Now you don't have to feel guilty....the computer did it :)

# Maybe you want to draw names out of a digital "hat". Your can have
#	Python reorder your list randomly.
random.shuffle(friends)
print(friends)
# NOTE: This randomizes the original list...why?