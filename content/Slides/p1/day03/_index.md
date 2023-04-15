---
title: "Day 3: Learning names with pandas"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-22T10:42:26+06:00
weight: 4
draft: false
# search related keywords
keywords: [""]
---

## Completing Last Week

1. __Markdown Preview Enhanced__ [Install](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) & [Manual](https://shd101wyy.github.io/markdown-preview-enhanced/#/)
2. __Stop saving files everywhere!__ Structure your folders. [Example 1](https://drivendata.github.io/cookiecutter-data-science/), [Example 2](https://github.com/BYUIDSS/blank_project_repository).
3. __Finishing the Introduction Project__    
    A. `data_science_programming > introduction`   
    B. In  `introduction` I will save my `.py`, `.md`, and any `.png` files that are created with my `.py` file.   
    C. Let's use the [project template](../../../template/cse250_project_template.md)     
    D. Now lets use __Markdown Preview Enhanced__ to finish our introduction project.   
    E. Now submit it in Canvas.   

{{< faq "What was that data science community portion of our grade?" >}}

__The [Syllabus](../../course-materials/syllabus) has this section which says;__

> Data science community
> 1. Attend data science society at least once during the semester.
> 2. Register to get a regular email on topics related to data science.

__Interview Question:__  What do you do to stay up with the current methods in data science?

__Don't Say:__ _Nothing_


### Register for a newsletter

> - https://www.datascienceweekly.org/
> - https://dataelixir.com/ [Archives](https://dataelixir.com/newsletters/)
> - https://tinyletter.com/data-is-plural
> - https://towardsdatascience.com/tagged/tds-letter [sign-up](https://towardsdatascience.com/receive-our-newsletters-681049ffa0cf)

{{</ faq >}}

{{< faq "How do we handle the reading and preparing for class?" >}}

Each project has a __Readings__ section. See [Project 1](../../../projects/project-1) for example. Let's look at the readings and figure out what we need.

> - [Python for Data Science (P4DS): Data Visualization](https://byuidatascience.github.io/python4ds/data-visualisation.html) 
> - [P4DS: Graphics for Communication](https://byuidatascience.github.io/python4ds/graphics-for-communication.html)
> - [P4DS: Markdown](https://byuidatascience.github.io/python4ds/markdown.html)
> - [P4DS: 5.2 Filter rows with .query()](https://byuidatascience.github.io/python4ds/transform.html#filter-rows-with-.query)



{{</ faq >}}

## Understanding the power of pandas

{{< faq "What is the data science workflow?" >}}

## The data science workflow

> - __You are going to hit `SHIFT + ENTER` thousands of times.__
> - __We don't usually source our scripts.__
> - __Think of Python Interactive like a [TI-86](https://en.wikipedia.org/wiki/TI-86) or Excel on steroids.__
> - __You code in pieces.__
> - __Rewrite for clarity!__

{{</ faq >}}



{{< faq "Can you figure out the functions of pandas?" >}}

{{% notice tip %}}
[Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
{{% /notice %}}

```python
df = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]})
# Can someone read this code in english?
```


### Use the cheat sheet to find the functions you would need to implement the following steps.

__I want to;__

1. sort my table by column `a` then
1. only use the first 2 rows then
1. calculate the mean of column `b`.

__I want to;__

1. rename column `a` to `duck` then
1. subset to only have `duck` and `b` columns then
1. keep all rows where `b` is less than 9 then
1. find the min of `duck`

{{</ faq >}}


{{< faq "What is method chaining?" >}}

Pandas and Altiar are built to allow for method chaining.  

- Altair is a chart object
- pandas is a DataFrame object
- We usually include `()` around our entire method so we can show it in steps.

```python
flights_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/flights/flights.csv"
flights = pd.read_csv(flights_url)
flights['time_hour'] = pd.to_datetime(flights.time_hour, format = "%Y-%m-%d %H:%M:%S")

(flights
    .filter(['dep_time'])
    .assign(
      hour = lambda x: x.dep_time // 100,
      minute = lambda x: x.dep_time % 100
      ))
```

```python
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"

mpg = pd.read_csv(url)

chart_loess = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy")
  .transform_loess("displ", "hwy")
  .mark_line()
)

chart_loess
```

{{</ faq >}}