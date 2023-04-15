---
title: "Day 7: Is JSON missing?"
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

## Data has structure

1. __Was our baby names data tidy?__

- [Tidy Data](https://byuidatascience.github.io/python4ds/tidy-data.html)
- [DataFrame](https://byuidatascience.github.io/python4ds/dataframe.html)s

![](https://byuidatascience.github.io/python4ds/images/tidy-1.png)
## Connecting to Application Programming Interfaces (APIs)

### Representational State Transfer (REST APIs)

> Over the course of the ’00s, another Web services technology, called __Representational State Transfer, or REST__, began to overtake [all other tools] for the purpose of transferring data. One of the big advantages of programming using REST APIs is that you can use multiple data formats — not just XML, but JSON and HTML as well. As web developers came to prefer JSON over XML, so too did they come to favor REST over SOAP. As Kostyantyn Kharchenko put it on the Svitla blog, “In many ways, the success of REST is due to the JSON format because of its easy use on various platforms.”   
> Today, JSON is the de-facto standard for exchanging data between web and mobile clients and back-end services. [ref](https://www.infoworld.com/article/3222851/what-is-json-a-better-format-for-data-exchange.html)

### JavaScript Object Notation

> Well, when you’re writing frontend code in Javascript, getting JSON data back makes it easier to load that data into an __object tree__ and work with it. And JSON formats data in a more __succinct way__, which saves bandwidth and improves response times when sending messages back and forth to a server.    
> In a world of APIs, cloud computing, and ever-growing data, JSON has a big role to play in greasing the wheels of a modern, open web.[ref](https://blog.sqlizer.io/posts/json-history/)

## Handling JSON data in Python

### Dealing with the World Wide Web

[Web requests in Python](https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul)

__Internal Packages__

- [urlib](https://docs.python.org/3/library/urllib.html#module-urllib)
- [urlib3](https://urllib3.readthedocs.io/en/latest/)

__External Packages__   

- [Requests package](https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


### Our path

__urllib3__: <https://urllib3.readthedocs.io/en/latest/user-guide.html>

```python
# internal packages
import urllib3 
import json

url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"

# %%
http = urllib3.PoolManager()
response = http.request('GET', url)
cars_json = json.loads(response.data.decode('utf-8'))

```

__requests__: <https://requests.readthedocs.io/en/master/>

```bash
pip install requests
```

```python
# external package
import requests

url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"

# %%
resp_req = requests.get(url)
cars_json_req = resp_req.json()

```

### JSON for data

- _What do we notice is different about the first two cars?_
- _Why do JSON files seem optimal for data sharing?_
- _Compare and contrast `.csv` and `.json` format benefits._


[Motor Trends Car Road Tests data with missing values](https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json)


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

#### JSON to DataFrame

- [.from_dict()](https://stackoverflow.com/questions/42518864/convert-json-data-from-request-into-pandas-dataframe)
- [.json_normalize()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html)
- [Which should we use?](https://hackersandslackers.com/json-into-pandas-dataframes/)



```python
# cars = pd.DataFrame.from_dict(cars_json)
cars = pd.json_normalize(cars_json) # handles nested jsons.
```

## What is missing data?

### How pandas handles missingness

Read ['Handling missing in pandas'](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#calculations-with-missing-data)

```python
df = (pd.DataFrame(
    np.random.randn(5, 3), 
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three'])
  .assign(
    four = 'bar', 
    five = lambda x: x.one > 0,
    six = [np.nan, np.nan, 2, 2, 1],
    seven = [4, 5, 5, np.nan, np.nan])
  )
```


{{< faq "What happens when you add two pandas objects with missing values?">}}

```python
df.seven + df.six
```

[Answer](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#calculations-with-missing-data)

{{</ faq >}}

{{< faq "What happens when you sum within a column?">}}

```python
df.seven.sum()
```

[reference](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#calculations-with-missing-data)

{{</ faq >}}

{{< faq "How could I add two columns treating NaN like zeros?">}}

[reference](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#filling-missing-values-fillna)


{{</ faq >}}

