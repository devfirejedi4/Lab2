# Create a welcome message.
# Input: a name as a string.
# Result: a string.
def welcome_message(name: str) -> str:
    message = "Hello, " + name + "!"
    return message


message = welcome_message("ebatiste@calpoly.edu")
print(message)
