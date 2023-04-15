---
title: "Day 19: Understanding the Pavlov in Machine Learning"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-01T10:42:26+06:00
weight: 4
draft: false
# search related keywords
keywords: [""]
---

__Read the project overview and Questions for understanding.__

- [Our 2-week project details](..)
- Questions?
## The big ML picture

<!-- https://www.microsoft.com/en-us/videoplayer/embed/RE4xAok?pid=RE4xAok-ax-85-id-oneplayer&postJsllMsg=true&autoplay=false&mute=false&loop=false&market=en-us&playFullScreen=false -->

> AI is able to learn 'rules' from highly repetitive data. [Sebastian Thrun](https://www.youtube.com/watch?v=ZJixNvx9BAc)   


> The single most important thing for AI to accomplish in the next ten years is to free us from the burden of repetitive work. [Sebastian Thrun](https://www.youtube.com/watch?v=ZJixNvx9BAc)   

<iframe width="560" height="315" src="https://www.youtube.com/embed/asmXyJaXBC8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/XZDLbbfT9_Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

###  Understanding Classification Machine Learning

__As we review the following material, be prepared to address the following questions__

- What is the difference between a feature and a target?
- What does it mean to classify?
- What does it mean to create a machine learning model?
- What does it mean to find _'boundaries'_ in our variables or features?
- How does finding _'boundaries'_ help us in ML?
- What is a histogram?
- What are false positives?
- What are false negatives?
- What is accuracy?
- What is training data?
- What is test data?

> [Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)

> 1. Machine learning identifies patterns using statistical learning and computers by unearthing boundaries in data sets. You can use it to make predictions.
> 2. One method for making predictions is called a decision trees, which uses a series of if-then statements to identify boundaries and define patterns in the data.
> 3. Overfitting happens when some boundaries are based on distinctions that don't make a difference. You can see if a model overfits by having test data flow through the model.

### Evaluating Machine Learning Models

__As we review the following material, be prepared to address the following questions__

- What is bias?
- What is variance?
- What is the _'minimum node size'_ do?

> Variance, in the context of Machine Learning, is a type of error that occurs due to a model's sensitivity to small fluctuations in the training set. High variance would cause an algorithm to model the noise in the training set. This is most commonly referred to as overfitting [ref](https://www.google.com/search?q=explaining+variance+in+ml+models&oq=explaining+variance+in+ml+models&aqs=chrome..69i57.4991j0j1&sourceid=chrome&ie=UTF-8)

> [Bias-Variance Tradeoff](http://www.r2d3.us/visual-intro-to-machine-learning-part-2/)

> 1. Models approximate real-life situations using limited data.
> 2. In doing so, errors can arise due to assumptions that are overly simple (bias) or overly complex (variance).
> 3. Building models is about making sure there's a balance between the two.

### Reviewing the reward/penalty in Machine Learning

__What is the 'Pavlovian bell' in the machine learning model?__

![](../../../images/ml/test.png)

Some mathematical penalty/reward equation.

> - __[Variance, RMSE, SD](https://setosa.io/ev/ordinary-least-squares-regression/)__
> - __Proportions, Classification__


### If your model is near perfect in its predictability, you might be cheating.

### Watch out for [transactional data](https://www.sciencedirect.com/topics/computer-science/transactional-data)!

> - Financial: orders, invoices, payments
> - Work: plans, activity records
> - School: Grades

## [scikit learn](https://scikit-learn.org/stable/)

> - [Tutorials](https://scikit-learn.org/stable/tutorial/index.html)
> - [Getting Started](https://scikit-learn.org/stable/getting_started.html): _What do you notice about the header portion of each of the script chunks?_
>    - [`import` vs `from ... import`](https://scikit-learn.org/stable/getting_started.html)

## Using our project data to understand features, targets, and samples.

### Getting our packages for project 4

```python
# install packages
import sys
!{sys.executable} -m pip install seaborn scikit-learn
```

> 1. Import `dwellings_ml.csv` and write a short sentence describing your data. Remember to explain an observation and what measurements we have on that observation.

```python
# the full imports
import pandas as pd 
import numpy as np
import seaborn as sns
```

```python
# the from imports
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
```


```python
dwellings_denver = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv")
dwellings_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv")
dwellings_neighborhoods_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv")   

alt.data_transformers.enable('json')

```

> 2. Now try describing the modeling (machine learning) we are going to do in terms of features and targets.
>    A. _Are there any columns that are the target in disguise?_
>    B. _Are the observational units unique in every row?_

![](../../../images/ml/iris_description.png)

```python
# %%
h_subset = dwellings_ml.filter(['livearea', 'finbsmnt', 
    'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 
    'stories', 'yrbuilt', 'before1980']).sample(500)

sns.pairplot(h_subset, hue = 'before1980')

corr = h_subset.drop(columns = 'before1980').corr()
# %%
sns.heatmap(corr)

```



