class Category:
    '''
    It should be able to instantiate objects based on different budget categories like food, 
    clothing, and entertainment. When objects are created, they are passed in the name of the 
    category. 
    '''
    
    def __init__(self, n):
        self.name = n
        self.ledger = []
   

    def get_balance(self):
        '''
        Args:      
        Returns:
            (float): the current balance of the budget category based on the deposits 
                     and withdrawals that have occurred
                     
        Notes:
        '''
        return sum(entry.get('amount', 0) for entry in self.ledger)
    
    
    def __str__(self):
        '''
        When the budget object is printed it should display:

           (1) A title line of 30 characters where the name of the category is centered in a line 
               of * characters.

           (2) A list of the items in the ledger. Each line should show the description and amount. 
               The first 23 characters of the description should be displayed, then the amount. 
               The amount should be right aligned, contain two decimal places, and display a 
               maximum of 7 characters (i.e. we're assuming no amounts are > 9999.99 or  < -999.99).

           (3) A line displaying the category total.

        Example:
            >> print(food)
            *************Food*************
            initial deposit        1000.00
            groceries               -10.15
            restaurant and more foo -15.89
            Transfer to Clothing    -50.00
            Total: 923.96
        '''   
        output = [self.name.center(30, '*')]
        for entry in self.ledger: 
            amount, desc = entry['amount'], entry['description']
            len_d = min(23,len(desc)) 
            len_n = 30 - len_d
            
            # description limited to <=23 characters + amount limited to 7> characters. Zero padded in middle 
            line = desc[:len_d] + ('{:>'+f'{max(7,len_n)}'+'.2f}').format(amount)
            output.append(line)
            
        output.append(f'Total: {self.get_balance()}')
        return '\n'.join(output)

        
    def deposit(self, amount, description=''):
        '''
        Args:
            amount (float): the amount being deposited
            
            description (str): description of deposit
        
        Notes:
            The method should append an object to the ledger list in the form of 
            {"amount": amount, "description": description}.
        '''
        self.ledger.append({"amount": amount, "description": description})
    
    
    def check_funds(self, amount):
        '''
        Args:
            amount (float): the query amount
        
        Returns:
            (bool): returns False if the amount is less than the balance of the budget category 
                    and returns True otherwise
        
        Notes:
            (1) This method should be used by both the withdraw method and transfer method.
        '''
        return True if self.get_balance() >= amount else False
    
        
    def withdraw(self, amount, description=''):
        '''
        Args:
            amount (float): amount being withdrawn to be stored in the ledger as a negative number.
                        
            description (str): description of withdrawal
        
        Returns:
            (bool): return True if the withdrawal took place, and False otherwise
        
        Notes:
            (1) If there are not enough funds, nothing should be added to the ledger. 
        '''
        outcome = self.check_funds(amount)
        if outcome == True:
            self.deposit(-amount, description)
        return outcome
    
        
        
    def transfer(self, amount, category):
        '''
        Args:
            amount (float): the amount to transfer
            
            category (str): a budget category
        
        Returns:
            (bool): True if the transfer took place, and False otherwise.
            
        Notes:
            (1) The method should add a withdrawal with the amount and the description 
                "Transfer to [Destination Budget Category]". 
                
            (2) The method should then add a deposit to the other budget category with the amount and 
                the description "Transfer from [Source Budget Category]". 
                
            (3) If there are not enough funds, nothing should be added to either ledgers. 
        '''
        outcome = self.check_funds(amount)
        if outcome == True:
            self.deposit(-amount, f"Transfer to {category.name}") 
            category.deposit(amount, f"Transfer from {self.name}")
        return outcome
    
def labels(names):
    '''Helper function
    Args:
        names (list):
        
    Returns:
        (str): a string of vertically formatted labels
        
    Example:
        >> labels(['Food','Clothing','Auto'])
         F  C  A  
         o  l  u  
         o  o  t  
         d  t  o  
            h     
            i     
            n     
            g     
    '''
    s4 = ' '*4
    # len of the longest category name
    biggest = max(map(len, names))   
    # e.g. ['Food    ', 'Clothing', 'Auto    ']
    standardized = [cat.ljust(biggest) for cat in names] 
    tmp = []
    for i in range(biggest):
        line = '' 
        for cat in range(len(names)):
            line += ' ' + standardized[cat][i] + ' '
        # e.g. ' F  C  A  '
        tmp.append(s4 + line + ' ') 
    return '\n'.join(tmp)    


def makeCircles(categories):
    ''''''
    spent = [sum(-1*entry.get('amount', 0) for entry in c.ledger if entry.get('amount', 0) < 0) for c in categories]
    percentage = [(spent[i] / sum(spent))*100 // 10 * 10 for i in range(len(categories))]
    
    circles = []
    # For each percentage bin: 100, 90, ..., 0
    for i in range(100,-1,-10):
        calc = ''
        for per in percentage:
            if per >= i:
                calc += ' o '
            else:
                calc += ' '*3
        line = calc + ' ' 
        circles.append(line)
        
    return circles
    
def create_spend_chart(categories):
    '''
    Args:
        categories (list[Category]): a list of categories
    
    Returns:
        (str): return a string that is a bar chart.
        
    Notes:
        (1) The chart should show the percentage spent in each category passed in to the function. 
        
        (2) The percentage spent should be calculated only with withdrawals and not with deposits. 
        
        (3) Down the left side of the chart should be labels 0 - 100. 
        
        (4) The "bars" in the bar chart should be made out of the "o" character. 
        
        (5) The height of each bar should be rounded down to the nearest 10. 
        
        (6) The horizontal line below the bars should go two spaces past the final bar. 
        
        (7) Each category name should be vertacally below the bar. 
        
        (8) There should be a title at the top that says "Percentage spent by category".
    
    Example:
        >> create_spend_chart([food, clothing, auto])
        Percentage spent by category
        100|          
         90|          
         80|          
         70|          
         60| o        
         50| o        
         40| o        
         30| o        
         20| o  o     
         10| o  o  o  
          0| o  o  o  
            ----------
             F  C  A  
             o  l  u  
             o  o  t  
             d  t  o  
                h     
                i     
                n     
                g     
    '''
    names = [c.name for c in categories]
    title = 'Percentage spent by category\n'
    divider = ' '*4 + '-'*(3*len(categories) + 1) + '\n'
    
    circles = makeCircles(categories)
    
    chart = '\n'.join([str(i).rjust(3) + '|' + circles[idx] for idx, i in enumerate(range(100,-1,-10))]) + '\n'
           
    return title + chart + divider + labels(names)