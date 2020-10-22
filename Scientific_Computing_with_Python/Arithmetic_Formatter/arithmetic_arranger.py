import re
import numpy as np

def arithmetic_arranger(problems, display=False):
    '''
    Args:
        problems (list): A list of strings describing arithmetic problems,
                         e.g. "32 + 8", with a maximum list length of 5
        
        display (bool): An indicator of whether or not to print the answer(s)
    
    Returns:
        arranged_problems (str): The problems formatted as learned in elementary school. E.g.
                                >> arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
                                       32      3801      45      123
                                    + 698    -    2    + 43    +  49
                                    -----    ------    ----    -----
    Notes:
        (1): 4 spaces between each problem
        (2): Numbers are to be right justified
        (3): Numbers must only contain digits
        (4): Each operand has a max of four digits in width
    '''
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # A regex to group the operands and operation
    rgx = r'(\W+|\w+)\s(\W)\s(\W+|\w+)'

    parsed_problems = []
    for i in problems:
        # parse the string and find the operands and operator
        parsed = re.findall(rgx, i)
        x, op, y = parsed[0]

        # Initial format screening
        if x.isdigit() != True or y.isdigit() != True:  
            return "Error: Numbers must only contain digits."
        elif len(x) > 4 or len(y) > 4: 
            return "Error: Numbers cannot be more than four digits."
        elif op not in ['+', '-']: 
            return "Error: Operator must be '+' or '-'."
        
        width = max(len(x), len(y)) + 2
        prob = [[x.rjust(width)], 
                [op + ' '*(width-len(y)-1) + y], 
                ['-' * width], 
                [str(int(x) + int(op+y)).rjust(width)]]
        parsed_problems.append(prob)

    arranged_problems = ''
    flipped = np.asarray(parsed_problems).transpose()
    for i in range(len(flipped[0])-1):
        arranged_problems += '    '.join(flipped[0][i]) + '\n'
    
    if display:
        arranged_problems += '    '.join(flipped[0][-1])
        return arranged_problems
    
    return arranged_problems[:-1]