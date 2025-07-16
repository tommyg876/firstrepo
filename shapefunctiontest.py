def finance_bro (f):
     f()
     f()

def print_two(val):
    finance_bro (val)
    finance_bro (val)

#here you create the inital pattern for line 1
def long_line():
    print ('+----', end="")

#here you create the inital pattern for line 2 through 5
def short_line():
    print ('|    ', end="")

#here you call something that returns pattern twice and prints extra + 
def excel_one():
    print_two (long_line)
    print ("+")

#here you call something that returns pattern twice and prints extra + 
def excel_two():
    print_two (short_line)
    print ("|")dd

def grid_one():
    excel_one()
    print_two(excel_two)

def ultimate_finance_bro ():
    finance_bro(grid_one)

def four_grid ():
    finance_bro(ultimate_finance_bro)
    excel_one ()

four_grid()