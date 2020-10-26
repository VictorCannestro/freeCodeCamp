import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# filter out days when the page views were in the top 2.5% of the dataset or bottom 2.5% 
df = df[(df.value > df.value.quantile(0.025))&
        (df.value < df.value.quantile(0.975))]


def draw_line_plot():
    '''
    Notes:
      (1) The title should be "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
      
      (2) The label on the x axis should be "Date"

      (3) The label on the y axis should be "Page Views".
    '''
    df_line = df.copy()
    title = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"

    fig, ax = plt.subplots(figsize=(14,6))
    sns.lineplot(x=df_line.index, y='value', color='red', data=df_line, ax=ax)

    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title(title)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    '''
    Notes:
      (1) It should show average daily page views for each month grouped by year
      
      (2) The legend should show month labels and have a title of "Months"

      (3) https://seaborn.pydata.org/tutorial/color_palettes.html

      (4) Alternative implementation:
          g = sns.catplot(x='year',
                          y='value',
                          hue='month',
                          kind='bar',
                          palette='tab10',
                          legend_out=True,
                          aspect=2,
                          data=df_bar)               
          g.set_axis_labels("Years", "Average Page Views")
          fig = g.fig
    '''
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['month'] = df_bar.index.month.map(dict(zip(range(1,13), labels)))

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(14,6))
    sns.barplot(x='year',
                y='value',
                hue='month',
                palette='Paired',
                ax=ax,
                ci=False,
                data=df_bar)

    ax.set(xlabel="Years", ylabel="Average Page Views")
    ax.legend(loc='upper left')

    # Get the bars and the corresponding labels from the legend
    handles, labels = plt.gca().get_legend_handles_labels()

    # We need to fix the scrambled order of the legend since the data starts at March
    order = [8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]

    # Match the bars to the months in the desired order
    ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    '''
    Notes:
      (1) Draw two adjacent box plots
      
      (2) Sould show how the values are distributed within a given year or month and how it compares over time.

      (3) The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)"

      (4) Make sure the month labels on bottom start at "Jan" and the x and x axis are labeled correctly. 

      (5) https://seaborn.pydata.org/generated/seaborn.boxplot.html
    '''
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    fig, axs = plt.subplots(ncols=2, nrows=1, figsize=(14,6))

    sns.boxplot(x='year', y='value', data=df_box, ax=axs[0]) 
    axs[0].set(xlabel="Year", 
               ylabel="Page Views", 
               title='Year-wise Box Plot (Trend)')

    sns.boxplot(x='month', y='value', order=names, data=df_box, ax=axs[1])
    axs[1].set(xlabel="Month", 
               ylabel="Page Views", 
               title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig