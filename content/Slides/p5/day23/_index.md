---
title: "Day 23: The war with Star Wars"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 4
draft: false
# search related keywords
keywords: [""]
---

__Read the project overview and Questions for understanding.__

- [Our 2-week project details](..)
- Questions?

## It might not be 80% but Cleaning data takes time.

> Data science is frequently about doing bespoke analysis which means creating and labelling unique datasets. No matter how cleanly formatted or standardized a dataset its likely to need some work. [ref](https://blog.ldodds.com/2020/01/31/do-data-scientists-spend-80-of-their-time-cleaning-data-turns-out-no/)

> I would argue that spending time working with data. To transform, explore and understand it better is absolutely what data scientists should be doing. This is the medium they are working in. [ref](https://blog.ldodds.com/2020/01/31/do-data-scientists-spend-80-of-their-time-cleaning-data-turns-out-no/)

### Tableau on tidying data

> 1. [Think about your data holistically](https://www.tableau.com/learn/whitepapers/data-prep-best-practices#think)
> 2. [Know the basic structure of your data](https://www.tableau.com/learn/whitepapers/data-prep-best-practices#know)
> 3. [Keep track of your steps](https://www.tableau.com/learn/whitepapers/data-prep-best-practices#track)
> 4. [Spot check throughout](https://www.tableau.com/learn/whitepapers/data-prep-best-practices#spot)

> Creating new steps for a specific set of actions keeps your flow nice and tidy. Think of your steps as folders in your filing cabinet—you organize files by their subject, making it easier to find what you’re looking for. Similarly, the steps in the flow should group a set of changes that capture a particular task. For example, cleaning up customer names might involve splitting a field, remapping a bunch of values, and applying filters on other fields to get the right customer segmentation for the output of the data source. When you keep these actions in the same step, you can add a descriptive name to help you understand the flow later on. Not only does this help you, but if you’re sharing the flow with fellow analysts, it lets them find and reference the same actions, giving them a way to easily make any edits.

## Structure your project, structure your thinking

### Compartmentalize and Organize your scripts and data

> - [BEST PRACTICES ORGANIZING DATA SCIENCE PROJECTS](https://www.thinkingondata.com/how-to-organize-data-science-projects/)
> - [How to organize your Python data science project](https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510#directory-structure)
> - [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/#directory-structure)
> - [Data Science Project Folder Structure](https://dzone.com/articles/data-science-project-folder-structure)
> - [BYU-I DSS](https://github.com/BYUIDSS/blank_project_repository)

### Structured Thinking

> Here is how to read this graph:
>
> - Red line in the graph shows how time to complete a project (in weeks) has come down with experience
> - With in each of three blocks (< 1 year; 1 – 3 year; 3+ years), the area of color shows the factor responsible for drop in time.
> - For example, during the first block, time required to complete the project comes down from 12+ weeks to 3 weeks and 75% of this drop is because of structured thinking. [ref](https://www.analyticsvidhya.com/blog/2013/06/art-structured-thinking-analyzing/)

![](https://www.analyticsvidhya.com/wp-content/uploads/2013/06/time-required-project-completion.jpg)

## Let's load the data

```python
# %%
import pandas as pd 
import altair as alt
import numpy as np

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

dat = pd.read_csv(url)

```

### What are codecs and encodings?

- [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
- [Python Unicode Basics](http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html#unicode-basics)
- [pd.read_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [ISO-8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1)

### Take the time to describe how the current data is organized.

1. What does each row represent?
2. What does each column represent?

### What do we want our columns to look like to use ML?

__What do we want each row to represent?__

1. We want shorter column names.
2. We want responses in the columns.
3. We need to one-hot-encode binary responses.
4. We need to create numeric values out of some of the category columns.

### Where are the column names?

__How could we create our column names?__

1. Use arguments of `pd.read_csv()`
2. Use `.melt()`
3. Leverage the `.replace()` method with a dictionary.


