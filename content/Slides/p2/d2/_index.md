---
title: "Day 8: Using pandas to handling missingness."
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---


## Let's get our JSON files into Python.

### Looking at cars

```python
# Cars
url_cars = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"
cars = pd.read_json(url_cars)
```

### The flight project data

```python
# the long way to help us understand json files and 
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)
```

## Handling Missing Data

### What is `missing` in pandas

> - [NaN, NaT, None](https://dev.to/discdiver/the-weird-world-of-missing-values-in-pandas-3kph)   
> - [pd.NA](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#experimental-na-scalar-to-denote-missing-values)

### Be careful with `.dropna()`

[Let's use the pandas example](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) with a little extra.


```python
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman', np.nan],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip',np.nan],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT, pd.NaT],
                    "power": [np.nan, np.nan, np.nan, np.nan]})

```

{{< faq "When would we ever use `df.dropna()`?">}}

__Almost never!__ _Why do you think it is a bad idea?_

```python
df.dropna()
```

{{</ faq >}}

#### `dropna()` with arguments

{{< faq "What argument do we use to drop rows where all values are `NA`?">}}

[reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)

```python
df.dropna(<ARGUMENTS>)
```

{{</ faq >}}


{{< faq "What if we want to drop `NA` rows based on one column?">}}

[reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)

```python
df.dropna()
```

{{</ faq >}}


### Replacing missing values

#### Figuring out `fillna()`


{{< faq "What if we want to replace all the `NA` values with the mean weight in the `wt` column of the cars data?">}}

[reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html)

{{</ faq >}}

#### Figuring out `replace()`

{{< faq "What if we want to replace all the `999` with `4` in the cars data?">}}

[reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html)

{{</ faq >}}


#### Interpolating `interpolate()`

{{< faq "What if we want to replace all the `NA` values with a linear interpolation?">}}

```python
s = pd.Series([0, 1, np.nan, 3])
s2 = pd.Series([0, 1, np.nan, 3, np.nan, 8, np.nan, 6])
```

[reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
)

{{</ faq >}}

## The cars data

_Suppose that the missing car names should be the value preceding it in the table (which is not correct)._

__Write the code to do the replacement with the functions above.__

## The flights data

### Handling the non `nan` missings

__Careful to handle the missing Late Aircraft data correctly__

> - Let's list what values are being used to represent missing.

{{< faq "What columns do we need to use for question 4 (total number of flights delayed by weather)?">}}

> - `num_of_delays_late_aircraft`
> - `num_of_delays_nas`

{{</ faq >}}


### Handling the missing months

{{< faq "How many rows have missing months?">}}

```python
flights.month.value_counts()
```

{{</ faq >}}

{{< faq "Can we figure out any patterns in the missingness?">}}

- [`pd.crosstab()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.crosstab.html)   
- [groupby](https://byuidatascience.github.io/python4ds/transform.html#grouped-summaries-or-aggregations-with-agg)


{{</ faq >}}

