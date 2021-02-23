"""Small program demonstrating Sample function  """
def my_first_function():
    name = input("Please enter your name ")  # user input string
    age = int(input("Please enter your age "))  # user input int, possible ValueError
    print(name, " ", age, " years old. ")  # print statement, minial formatting


if __name__ == '__main__':
    try:
        my_first_function()
    except ValueError as err:
        print(err)    