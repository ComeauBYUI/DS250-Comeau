# %%
import pandas as pd
import altair as alt
import numpy as np
# %%
dat = pd.read_csv('https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.csv')
# %%

mydat = dat.query("~car.isna()")
mydat.fillna({'hp': mydat.query("~car.isna()").hp.mean()})


# %%
chart_dot = alt.Chart(mydat).encode(
    alt.X('hp', title = 'Horse Power', axis=alt.Axis(format = "+.1f")),
    alt.Y('mpg', title = "Miles per Gallon"),
    color = alt.value('red')
).mark_circle()


dat_label = pd.DataFrame({
    'x': [80, 160], 
    'y': [25, 20], 
    'label': ['Big', 'Real Big']})



line = alt.Chart(dat_label).encode(x = 'x').mark_rule(color = 'black')
text = (alt.Chart(dat_label)
    .encode(
        x = 'x', 
        y = 'y', 
        text = 'label')
    .mark_text(color = 'black', dx = -25))  

chart = (alt.layer(chart_dot, line, text)
    .properties(title = "This is dope.", width = 450)
    .configure_title(anchor='start')
)

chart.save('practice_mtcars.png')
# %%

practice_table = mydat.groupby(['cyl', 'carb']).agg(count = ('carb', 'size')).reset_index()

print(pd.pivot_table(practice_table, 
    values  = 'count', 
    index = 'cyl', 
    columns = 'carb',
    fill_value=0).to_markdown())


