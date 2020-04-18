# Import hello module
import hello

# Call function
print(hello.world())

# Print variable
print("---------->", hello.ant)

# Call class
the_machine = hello.Car("Ford Mustang", "1967 Fastback", "night blue")
the_machine.tell_me_about_the_car()
print(the_machine.color)

