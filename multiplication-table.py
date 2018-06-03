# Assignment: Multiplication Table (optional)
# Karen Clark
# 2018-06-03

# Optional Assignment: Multiplication Table
# Create a program that prints a multiplication table in your console

def multiplication_table():
    table_maker = []

    # The first char in the top corner is supposed to 
    # be an 'x' but I can't figure that out so 
    # I'm not doing that. :(

    # create header row
    for h in range(1, 13):
        table_maker.append(h)

    # fill in table
    multiplier = 1
    row_header = 1
    for x in range(1, 13):
        # row header
        table_maker.append(row_header)
        # multiplication table contents
        for j in range(1, 13):
            table_maker.append(j * multiplier)
        row_header += 1
        multiplier += 1

    # now we need to make this list of integers into 
    # strings so we cna split them nicely
    table_maker = map(str, table_maker)
    # create new lists of strings for each 12 values, and
    # do some special junk for the fact we have header row
    table_itself = [table_maker[x: x + 12 ] for x in range(0, len(table_maker), 13)]
    # now print the table to the terminal
    for q in range(0, 13):
        print table_itself[q]

multiplication_table()