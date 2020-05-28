# Given the names and grades for each student in a Physics class of  students
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    nested_list = [] # We created a list where tha values have to be stored
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #print(name,score)
        nested_list.append([name,score]) # add values to the nested list

    # we could use the sort function to organice the array
    nested_list.sort(key = lambda x : x[1])
    # using lambda functions we could set the conditions
    #print(nested_list)
    # at this point we have an organized list

    # BUT WAIT, I THINK THAT WE DON'T HAVE TO DO THIS
    