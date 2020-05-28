# Given a number, print all the even numbers, starting from 2, until the given number.
# On the contrary. Print void

def even_numbers(maximum):
    return_string = "" # print void
    # print loop: range(start, end, step)
    for x in range(2,maximum+1,2):
        return_string += str(x) + " " # transform number to string, add a space
    
    return return_string 

if __name__ == "__main__":
    print(even_numbers(6))
    print(even_numbers(12))
    print(even_numbers(1))
    print(even_numbers(3))
    print(even_numbers(0))
