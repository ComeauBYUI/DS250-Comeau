---
title: "Day 10: Exporting JSON"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 1
draft: false
# search related keywords
keywords: [""]
---



## Let's get our JSON files out of Python.

### The flight project data

```python
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.io.json.json_normalize(flights_json)
```

### Saving JSON files from and pandas dataframe

__Remember you need to replace your missing values with NaN.__

#### What parameters do we need to change in `.to_json()` to get the same output format?

```JS
[
  {
    "car": "Mazda RX4",
    "mpg": 21,
    "cyl": 6,
    "disp": 160,
    "hp": 110,
    "drat": 3.9,
    "wt": 2.62,
    "qsec": 16.46,
    "vs": 0,
    "am": 1,
    "gear": 4,
    "carb": 4
  },
  {
    "car": "Mazda RX4 Wag",
    "mpg": 21,
    "cyl": 6,
    "disp": 160,
    "hp": 110,
    "drat": 3.9,
    "wt": 2.875,
    "qsec": 17.02,
    "am": 1,
    "gear": 4,
    "carb": 4
  },
  {
    "car": "Datsun 710",
    "mpg": 22.8,
    "cyl": 4,
    "disp": 108,
    "hp": 93,
    "drat": 3.85,
    "wt": 2.32,
    "qsec": 18.61,
    "vs": 1,
    "am": 1,
    "gear": 999,
    "carb": 1
  }
]
```

[df.to_json()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)


#### What is wrong with pandas `.to_json()` method for handling Nans?

- [stackoverflow: Pandas remove null values when to_json
](https://stackoverflow.com/questions/30912746/pandas-remove-null-values-when-to-json)
- [How to Write String to Text File in Python?](https://pythonexamples.org/python-write-string-to-text-file/)

#### How do we format our JSON in VS Code?

![](format_json.gif)