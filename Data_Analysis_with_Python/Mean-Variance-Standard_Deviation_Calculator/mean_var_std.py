import numpy as np

def calculate(vec):
    '''
    Args:
        list: input 1D row vector
  
    Returns:
        (dict): the mean, variance, standard deviation, max, min, and sum of the rows, 
                columns, and elements in a 3 x 3 matrix

    Notes:
        (1) The input of the function should be a list containing 9 digits. 
        
        (2) The function should convert the list into a 3 x 3 Numpy array, 
            and then return a dictionary containing the mean, variance, 
            standard deviation, max, min, and sum along both axes and for 
            the flattened matrix:

            {
              'mean': [axis1, axis2, flattened],
              'variance': [axis1, axis2, flattened],
              'standard deviation': [axis1, axis2, flattened],
              'max': [axis1, axis2, flattened],
              'min': [axis1, axis2, flattened],
              'sum': [axis1, axis2, flattened]
            }
    '''
    if len(vec) < 9:
        raise ValueError("List must contain nine numbers." )

    summary = {}
    vec = np.reshape(vec, (3,3))
    
    # The dictionary keys
    metrics = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    
    # The corresponding functions as objects in a list
    funcs = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    
    for m, f in zip(metrics, funcs):
        # Apply each function
        calc = [list(f(vec, axis=0)), list(f(vec, axis=1)), f(vec.flatten())]
        summary[m] = calc
        
    return summary