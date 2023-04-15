---
title: "Day 9: Real world replacement."
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 2
draft: false
# search related keywords
keywords: [""]
---


## The flight project data

```python
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)

```

## Handling the NaN's

- [isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isnull.html)
- [sum()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html)

### Handling the missing months

{{< faq "How many rows have missing months?">}}

```python
flights.month.value_counts()
```

{{</ faq >}}

{{< faq "Can we figure out any patterns in the missingness?">}}

- [`pd.crosstab()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.crosstab.html)   

```python
pd.crosstab(
    flights.month, 
    flights.airport_code)
```

{{</ faq >}}


### Handling the non `nan` missing

- [describe()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)


### Fixing the missing values.

__Careful to handle the missing Late Aircraft data correctly__

- Could we make a function that checks if a column has missing issues?
- [np.where()](https://numpy.org/doc/stable/reference/generated/numpy.where.html)

{{< faq "What columns do we need to use for question 4 (total number of flights delayed by weather)?">}}

```python
weather = flights.assign(
    severe = lambda x: #need to fix missing,
    nodla_nona = lambda x:
    mild_late = lambda x: # need to fix missing,
    mild = np.where(#use isin, 
     # fix missing * proportion, 
     # fix missing * proportion
        ),
    weather = # add up stuff
    percent_weather = # calculate percent weather over total
).filter(['airport_code','month','severe','mild', 'mild_late',
    'weather', 'num_of_delays_total', 'percent_weather'])
```

{{</ faq >}}


### Visualizing the flight data

```
RangeIndex: 924 entries, 0 to 923
Data columns (total 17 columns):
 #   Column                         Non-Null Count  Dtype  
---  ------                         --------------  -----  
 0   airport_code                   924 non-null    object 
 1   airport_name                   924 non-null    object 
 2   month                          924 non-null    object 
 3   year                           901 non-null    float64
 4   num_of_flights_total           924 non-null    int64  
 5   num_of_delays_carrier          924 non-null    object 
 6   num_of_delays_late_aircraft    924 non-null    int64  
 7   num_of_delays_nas              924 non-null    int64  
 8   num_of_delays_security         924 non-null    int64  
 9   num_of_delays_weather          924 non-null    int64  
 10  num_of_delays_total            924 non-null    int64  
 11  minutes_delayed_carrier        872 non-null    float64
 12  minutes_delayed_late_aircraft  924 non-null    int64  
 13  minutes_delayed_nas            893 non-null    float64
 14  minutes_delayed_security       924 non-null    int64  
 15  minutes_delayed_weather        924 non-null    int64  
 16  minutes_delayed_total          924 non-null    int64  
dtypes: float64(3), int64(10), object(4)
memory usage: 122.8+ KB
```

- What questions from the project can we answer with a chart?
- What charts could we create that support the answer to the grand question?
- What types of charts are available to use with this data?

> - [Data Visualisation Catalogue](https://datavizcatalogue.com/)
> - [Altair Example Gallery](https://altair-viz.github.io/gallery/index.html)