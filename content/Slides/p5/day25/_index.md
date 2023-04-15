---
title: "Day 25: May the ML columns be with you"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 2
draft: false
# search related keywords
keywords: [""]
---


## Moving from categories to values.

> 1. __Create an additional column(s) that converts the income ranges to a number.__
> 1. __Create an additional column(s) that converts the age ranges to a number.__
> 1. __Create an additional column(s) that converts the school groupings to a number.__

- [str.replace('', '9')](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html)
- [astype('float')](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html)
- [pd.concat(axis=1)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

### Why are we converting the columns to numerical values?

## One-hot encoding

1. __One-hot encode all columns that have categories.__
1. __Convert all yes/no responses to 1/0 numeric.__

- [pd.get_dummies](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html)
- [pd.factorize(x)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.factorize.html)

### Which columns are going to be problematic for the function `pd.get_dummies()`?

### What is `pd.get_dummies()` default behavior for the columns that are created?  Should we change that behavior?