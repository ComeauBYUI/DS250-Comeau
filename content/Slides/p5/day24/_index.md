---
title: "Day 24: Star Wars and strings"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---

## The `.str` functions in pandas

> - `.strip`: [Strip white space](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.strip.html)
> - `.replace`: [replace one string of characters with another.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html)
> - `.split`: [Separate a character string into two values.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html)
> - `.cat`: [Combine strings in series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.cat.html)

### `.str.strip()`

```python
s = pd.Series(['1. Ant.  ', '2. Bee!\n', '3. Cat?\t', '4. Beat?\t', np.nan])

s.str.strip()

s.str.strip('123.!? \n\t')

s.str.strip('1234.!? \n\t')

```

### `.str.replace()`

```python
s.str.replace('Ant.', 'Man')
s.str.replace('a', 8)
s.str.replace('a', '8')
s.str.replace('a', '8', case = False)
s.str.replace('a|e', '8', case = False)

s.str.replace('\d', '', case = False)

```

### `.str.split()`

_Let's split these series into multiple columns._

```python
s2 = pd.Series(['1-20', '21-50', '51-80', '81-100', np.nan])
s3 = pd.Series(
    [
        "this is a regular sentence",
        "https://docs.python.org/3/tutorial/index.html",
        np.nan
    ]
)
```

### `.str.cat()`

```python
two_columns = s2.str.split("-", expand = True).rename(
   columns = {0: 'minimum', 1: 'maximum'})

two_columns.fillna("").agg("__".join, axis = 1)

two_columns.minimum.str.cat(two_columns.maximum, sep = "__")

```

## Cleaning our data

### Creating column names

#### Let's look at the column names and figure out what we have.

- Where are the column names located?
- Why are they stored like that?
- How could we shorten them?

#### Now what do we want?

_Run the below code and tell me what we have._

```python
url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

dat_names = pd.read_csv(url, encoding = "ISO-8859-1", nrows = 1).melt()
dat = pd.read_csv(url, skiprows = 2, header=None)

# this is not complete.
dat_names =(dat_names
   .replace('Unnamed: \d{1,2}', np.nan, regex=True)
   .replace('Response', "")
   .assign(
      clean_variable = lambda x: x.variable.str.strip()
         .replace(
            'Which of the following Star Wars films have you seen? Please select all that apply.','seen'),
      clean_value = lambda x: x.value.str.strip()
      )
   .fillna(method = 'ffill')
   .assign(
      column_name = lambda x: x.clean_variable.str.cat(x.clean_value, sep = "__")
   )
)

dat_names.column_name
#dat.columns 

```

### Creating new columns

