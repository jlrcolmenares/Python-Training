# Given a first_name and and a last_name. Print following a set of rules

def format_name(first_name, last_name):
    # You should print the tag 'Name:' only if first_name and last_name exist
    tag = 'Name:'*(bool(first_name ) or bool(last_name))
    # you only should print a comma only if both first_name and last_name exist
    coma = ','*(bool(first_name) and bool(last_name))
    # using format function return the string
    return f'{tag}{last_name}{coma}{first_name}'

if __name__ == "__main__":
    print( format_name('Ernest','Hemingway') )
    print( format_name('','Madonna') )
    print( format_name('Voltaire','') )
    print( format_name('','') )    
    
