# import needed libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set global font configuration to Tahoma Bold
plt.rcParams['font.family'] = 'Tahoma'
plt.rcParams['font.weight'] = 'bold'

# dataset (list nearby cities, income in thousands and life expectancy in years)
data = {
    'City': ['Gates Mills', 'Shaker Heights', 'Cleveland Heights', 'East Cleveland'],
    'Median_Income':[231, 104, 73, 22],
    'Life_Expectancy': [86.2, 81.6, 77.3, 69.9]
}
df = pd.DataFrame(data)

# custom color dictionary mapping
city_colors = {
    'Gates Mills': '#0d47a1',
    'Shaker Heights': '#1976d2',
    'Cleveland Heights': '#64b5f6',
    'East Cleveland': '#b0bec5'
}

# initialize figure and primary axis (income)
fig, ax1 = plt.subplots(figsize=(11, 8))

# plot bars
sns.barplot(x='City', y='Median_Income', data=df, ax=ax1, palette=city_colors)
ax1.set_ylabel('Median Household Income ($ in thousands)', color='#0d47a1', fontsize=10, fontweight='bold')
ax1.set_xlabel('Village/City/Suburb', fontsize=10, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#0d47a1')
ax1.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# add data labels on top of bars
for container in ax1.containers:
    ax1.bar_label(
        container,
        labels=[f"${x:,.0f}" for x in container.datavalues],
        padding=4,
        fontsize=10,
        fontweight='bold',
        color='#0d47a1'
    )

# create shared twin axis for Life Expectancy
ax2 = ax1.twinx()

# plot Life Expectancy Line
sns.lineplot(x='City', y='Life_Expectancy', data=df, ax=ax2, color='#00FF00', marker='o', linewidth=3, markersize=8)
ax2.set_ylabel('Average Life Expectancy (Years)', color='#00FF00', fontsize=10, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='#263238')
ax2.set_ylim(65, 95)

# add labels to the lind=e chart data points
# loop through the index and coordinates of our dataframe rows
for i in range(df.shape[0]):
    ax2.text(
        x=i,                                 # horizontal position matches the bar index (0, 1, 2, 3)
        y=df['Life_Expectancy'][i] + 0.8,    # vertical position placed slightly above (+0.8 years) the point
        s=f"{df['Life_Expectancy'][i]} yrs", # the text string format
        color='#263238',
        fontsize=10,
        fontweight='bold',
        ha='center'                          # horizontally centers the text directly over the dot marker
    )

fig.suptitle('Socioeconomic Health Split in Cuyahoga County, OH', fontsize=14, fontweight='bold', y=0.96)
plt.tight_layout()
plt.show()
