class Rectangle:
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
        
        
    def __str__(self):
        '''
        Example:
            >> rect = Rectangle(10, 3)
            >> print(rect)
            Rectangle(width=10, height=3)
        '''
        return f'Rectangle(width={self.width}, height={self.height})'
    
    
    def set_width(self, w):
        ''''''
        self.width = w
    
    
    def set_height(self, h):
        ''''''
        self.height = h
    
    
    def get_area(self): 
        '''Returns area (w*h)'''
        return self.width * self.height
    
    
    def get_perimeter(self): 
        '''Returns perimeter (2*w + 2*h)'''
        return 2*self.width + 2*self.height
    
    
    def get_diagonal(self): 
        '''Returns diagonal sqrt(w**2 + h**2)'''
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    
    def get_picture(self): 
        '''
        Returns:
            (str): a string that represents the shape using lines of "*". 
        
        Notes:
            (1) The number of lines should be equal to the height and the number of "*" 
                in each line should be equal to the width. 
                
            (2) There should be a new line (\n) at the end of each line. 
            
            (3) If the width or height is larger than 50, this should return the string: 
                "Too big for picture.".
        '''
        if  self.width > 50 or self.height > 50:
            return "Too big for picture."
        return '\n'.join(['*'*self.width for i in range(self.height)]) + '\n'
        
 
    
    def get_amount_inside(self, shape): 
        '''
        Args:
            shape (object): (square or rectangle) as an argument
        
        Returns:
            (int): the number of times the passed in shape could fit inside the 
                   shape (with no rotations).
            
        Notes:
            (1) For instance, a rectangle with a width of 4 and a height of 8 could fit 
                in two squares with sides of 4.
                >>sq = Square(4)
                >>rect2 = Rectangle(4, 8)
                >>rect2.get_amount_inside(sq)
                2
        '''
        return self.get_area() // shape.get_area()

class Square(Rectangle):
    
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
    
    
    def __str__(self):
        '''
        Example:
            >> squ = Square(10)
            >> print(squ)
            Square(side=10)
        '''
        return f'Square(side={self.height})'
    

    def set_side(self, s):
        ''''''
        self.width = s
        self.height = s


    def set_width(self, w):
        self.set_side(w)
    
    
    def set_height(self, h):
        self.set_side(h)