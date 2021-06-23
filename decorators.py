from functools import wraps
from datetime import date
import sys

GREEN = '\033[0;32m'
RESET = '\033[0;0m'
WARNING = '\033[93m'

def new_decorator(func):
    @wraps(func)
    def decorate(input):
        write_color = WARNING if func.__name__ == "print_warning" else GREEN
        sys.stdout.write(write_color)
        print("="*len(input))
        func(input)
        print("="*len(input))
        sys.stdout.write(RESET)
        today = date.today()
        today = today.strftime("%d/%m/%Y")
        log = f"{func.__name__}-({today}): {input}"
        with open('out.log', 'a') as opened_file:
            opened_file.write(log + '\n')
    return decorate

@new_decorator
def print_decorated(input):
    print(input)

@new_decorator
def print_warning(input):
    print(input)

to_output = input("Type something to be decorated: ")
print("\nDecorated print:\n")

while True:
    opt = input("Warning or Successfull? [W/S]: ")
    if opt == 'W':
        print_warning(to_output)
        break
    if opt == 'S':
        print_decorated(to_output)
        break
