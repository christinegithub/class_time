# Both the instructor and the student have names.
# We know that instructors and students are both people.
# Create a parent Person class that contains the attribute name
# and an __init__() method to set the name.


class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print("Hi, my name is {}.".format(self.name))


# Let's start by creating two classes: one called Student and another
# called Instructor.


class Student(Person):

    # The student class has an instance method called learn
    # that returns "I get it!".

    def learn(self):
        print("I get it!")


class Instructor(Person):

    # The instructor class has an instance method called teach that returns
    # "An object is an instance of a class".

    def teach(self):
        print("An object is an instance of a class.")


# Both the instructor and the student should also be able to do a greeting,
# like "Hi, my name is so-and-so". Where's the best place to
# put this common method?

# Create an instance of instructor whose name is "Nadia" and call their
# greeting.

instructor1 = Instructor("Nadia")
print(instructor1.greeting())

# Create an instance of student whose name is "Chris" and call their greeting.

student1 = Student("Chris")
print(student1.greeting())

# Call the teach method on your instructor instance and call the learn method
# on your student. Next, call the teach method on your student instance.
# Why doesn't that work? Leave a comment in your program explaining why.

print(instructor1.teach())
print(student1.learn())

print(student1.teach())  # Doesn't work because the student class does not
# inherit the teacher class
