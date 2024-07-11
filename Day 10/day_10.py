# Functions with outputs

def format_name(first_name, last_name):
    """Take first and last name, returns full name"""  # Docstring
    first_name = first_name.title()
    last_name = last_name.title()
    return first_name + " " + last_name


f_name = input("What's your first name?")
l_name = input("What's your last name?")
result = format_name(f_name, l_name)
print(result)

format_name()