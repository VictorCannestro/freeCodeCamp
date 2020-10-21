import copy
import random
from collections import Counter

class Hat:
    '''
    The class should take a variable number of arguments that specify the number of balls 
    of each color that are in the hat. For example, a class object could be created in 
    any of these ways:

    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

    Notes:
        (1) A hat will always be created with at least one ball. 
    
        (2) The arguments passed into the hat object upon creation should be converted 
            to a contents instance variable. 
  
        (3) contents should be a list of strings containing one item for each ball in the hat. 
  
        (4) Each item in the list should be a color name representing a single ball of that 
            color. For example, if your hat is {"red": 2, "blue": 1}, contents should be 
            ["red", "red", "blue"].
    '''
    
    def __init__(self, **kwargs):
        if len(kwargs) == 0:
            raise TypeError('A hat must always have at least 1 ball. Cannot be empty.')
        self.contents = [[key]*arg for key,arg in kwargs.items()]
        self.contents = [j for color in self.contents for j in color]
        self.balls = []
    
    def draw(self, n):
        '''
        Args:
            n (int): indicates the number of balls to draw from the hat
            
        Returns:
            balls (list): 
            
        Notes: 
            (1) This method should remove balls at random from contents and return those 
                balls as a list of strings. 
                
            (2) The balls should not go back into the hat during the draw, similar to an
                urn experiment without replacement. 
                
            (3) If the number of balls to draw exceeds the available quantity, return 
                all the balls.
        ''' 
        if n > len(self.contents):
            return self.contents + self.balls
        
        self.balls = [self.contents.pop(random.randint(0, len(self.contents)-1)) for i in range(n)]
        return self.balls
            
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    Args:
        hat (Hat): A hat object containing balls that should be copied inside the function.
        
        expected_balls (list): An object indicating the exact group of balls to attempt to 
                               draw from the hat for the experiment.
        
        num_balls_drawn (int): The number of balls to draw out of the hat in each experiment.
        
        num_experiments (int): The number of experiments to perform. 
    
    Returns:
        (float): the estimated probability of obtaining the expected balls
        
    Notes:
        (1) expected_balls: For example, to determine the probability of drawing 2 blue balls 
            and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}. 
        
        (2) The more experiments performed, the more accurate the approximate probability 
            will be (up to an irreducible threshold)
    '''
    event = []
    for i in range(num_experiments):
        # Work with a fresh copy of the Hat
        tmp_hat = copy.deepcopy(hat)
        
        # A list of the drawn balls
        drawn = tmp_hat.draw(num_balls_drawn)
        
        # A dictionary of the frequencies
        freq = Counter(drawn)
        
        result = [freq[color] >= expected_balls[color] for color in expected_balls.keys()]
        
        # Did the experiment succeed?
        event.append(True if sum(result) == len(expected_balls) else False)
        
    return sum(event) / num_experiments