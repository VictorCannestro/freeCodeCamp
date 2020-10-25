import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def setupData():
    # Import data
    df = pd.read_csv('medical_examination.csv')

    # Add 'overweight' column
    # To determine if a person is overweight, first calculate their BMI by 
    # dividing their weight in kilograms by the square of their height in meters. 
    # If that value is > 25 then the person is overweight. Use the value 0 for 
    # NOT overweight and the value 1 for overweight.
    def bmi(dataframe):
        '''
        weight is in units of kg
        height is in units of cm
        '''
        return dataframe['weight'] / (dataframe['height']/100)**2 

    cat = [0 if val <= 25 else 1 for val in bmi(df)]
    df['overweight'] =  cat

    # Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol'
    # or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
    df['cholesterol'] = df['cholesterol'].map({i: 0 if i==1 else 1 for i in df.cholesterol})
    df['gluc'] = df['gluc'].map({i: 0 if i==1 else 1 for i in df.gluc})
    
    return df

# Draw Categorical Plot
def draw_cat_plot():
    '''
    Notes:
        (1) https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot
    '''
    df = setupData()
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable', 
                      col="cardio", 
                      hue='value', 
                      kind="count", 
                      data=df_cat)
    
    g.set(ylabel='total')  # setting y label in here
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    '''
      Notes:
        (1)  Filter out the following patient segments that represent incorrect data:
        
            diastolic pressure is higher then systolic (Keep the correct data with df['ap_lo'] <= df['ap_hi']))
        
            height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
        
            height is more than the 97.5th percentile
        
            weight is less then the 2.5th percentile
        
            weight is more than the 97.5th percentile
            
        (2) https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html
        
        (3) https://seaborn.pydata.org/generated/seaborn.heatmap.html
    '''
    df = setupData()

    # Masks for filtering
    dia_over_sys = df['ap_lo'] <= df['ap_hi']
    ht_under_2_5 = df['height'] >= df['height'].quantile(0.025)
    ht_over_97_5 = df['height'] <= df['height'].quantile(0.975)
    wt_over_97_5 = df['weight'] <= df['weight'].quantile(0.975)
    wt_under_2_5 = df['weight'] >= df['weight'].quantile(0.025)

    # Clean the data
    df_heat = df[(dia_over_sys)&
                 (ht_under_2_5)&
                 (ht_over_97_5)&
                 (wt_over_97_5)&
                 (wt_under_2_5)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    n = len(df_heat.columns)
    mask = np.triu(np.ones(n**2).reshape((n,n)))

    # Set up the matplotlib figure
    fig = plt.figure(figsize=(14,12))
    ax = sns.heatmap(data=corr, 
                    annot=True, 
                    fmt='.1f', 
                    cbar=True, 
                    mask=mask, 
                    linewidths=.25)
    fig.add_axes(ax)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
