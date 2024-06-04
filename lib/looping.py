def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")



def fizzbuzz(num):
     for number in range(1 , 101):
        if number % 3 == 0 and number % 5 == 0:
            print( "FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

def reverse_string(str):
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

def square_integers(int_list):
    return [num ** 2 for num in int_list]