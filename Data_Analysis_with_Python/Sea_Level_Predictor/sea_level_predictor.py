import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    '''
    Notes:
      (1) Create first line of best fit from 1880 to 2013

      (2) Plot the line of best fit over the top of the scatter plot. Make the line go through 
          the year 2050 to predict the sea level rise in 2050.

      (3) Next, just use the data from year 2000 through the most recent year in the dataset.
          Make the new line of best fit also go through the year 2050 to predict the sea level 
          rise in 2050 if the rate of rise continues as it has since the year 2000.

      (4) https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
    '''
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', index_col='Year')

    # Create scatter plot
    x, y = df.index, df['CSIRO Adjusted Sea Level'].values
    _ = plt.scatter(x, y, marker='.', label='Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err =  linregress(x, y)

    # Plot the line of best fit over the top of the scatter plot. 
    xnew = np.arange(1880,2050)
    f = lambda i: slope*i + intercept
    plt.plot(xnew, f(xnew), label='Extrapolated from 1880')

    # Plot a new line of best fit 
    df2000 = df.iloc[len(df)-14:]
    x2000, y2000 = df2000.index, df2000['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err =  linregress(x2000, y2000)
    xnew = np.arange(2000,2050)
    f = lambda i: slope*i + intercept
    plt.plot(xnew, f(xnew), label='Extrapolated from 2000')

    # Add labels, title, and misc
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.grid(True)
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()