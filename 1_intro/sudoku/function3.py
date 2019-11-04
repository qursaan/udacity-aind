from utils import *

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for digit in '123456789':
            # get digit position in unit
            dplaces = [box for box in unit if digit in values[box]]
            # only one place for number and digit not only in place
            if len(dplaces) == 1 and len(values[dplaces[0]])>1:
                # print("change from" , values[dplaces[0]], " to " ,digit)
                values[dplaces[0]] = digit
    return values
