---
title: "Day 16: We should join together in our SQL calculations"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---

## SQL queries are typed in the following pattern;

```SQL
SELECT -- <columns> and <column calculations>
FROM -- <table name>
  JOIN -- <table name>
  ON -- <columns to join>
WHERE -- <filter condition>
GROUP BY -- <subsets for column calculations>
ORDER BY -- <how the output is returned in sequence>
LIMIT -- <number of rows to return>
```

## Connecting to data.world in Python

### Let's make the connection

[Class reading](../../course-materials/sql-for-data-science/)

```python
import datadotworld as dw

results = dw.query('byuidss/cse-250-baseball-database', 
    'SELECT * FROM batting LIMIT 5')

batting5 = results.dataframe
```

### Let's view our tables

- [data.world basebal data](https://data.world/byuidss/cse-250-baseball-database/workspace)

- [Lahman data dictionary](https://data.world/byuidss/cse-250-baseball-database/workspace/file?filename=readme2014.txt)


#### I want to do a calculation in SQL and return it in a new column in Python?

__Use the batting table to show the player and his team with his at batts and runs together with a calculated value of `ab / r` that is called `runs_atbat`.__

- __Try do complete the above statement without using the info in the questions below.__

{{< faq "What table do we want to use?">}}

```python
q = '''
SELECT *
FROM batting
LIMIT 5
'''

dw.query('byuidss/cse-250-baseball-database', q).dataframe

```

{{</ faq >}}



{{< faq "What columns do we want to select?">}}

```python
q = '''
SELECT playerid, teamid, ab, r
FROM batting
LIMIT 5
'''

dw.query('byuidss/cse-250-baseball-database', q).dataframe

```

{{</ faq >}}


{{< faq "What calculation do we want to perform?">}}


```python
q = '''
SELECT playerid, teamid, ab, r, ab/r 
FROM batting
LIMIT 5
'''

batting_calc = dw.query('byuidss/cse-250-baseball-database', q).dataframe

```


{{</ faq >}}


{{< faq "What name do we give our calculated column?">}}


```python
q = '''
SELECT playerid, teamid, ab, r, ab/r as runs_atbat
FROM batting
LIMIT 5
'''

batting_calc = dw.query('byuidss/cse-250-baseball-database', q).dataframe

```

{{</ faq >}}


#### I want to join two tables to help in decision making

__For seasons after 1999, which year had the most players selected as All Stars but didn't play in the All Star game?__

- __Provide a summary of how many games, hits, and at bats occurred by those players had in that years post season.__


```python
import pandas as pd 
import altair as alt
import numpy as np
import datadotworld as dw

con_url = 'byuidss/cse-250-baseball-database'
```

{{< faq "What table do we want for All Star information?">}}


```python
# %%
# allstar table

dw.query(con_url, 
'''
SELECT *
FROM AllstarFull
WHERE 
    AND 
LIMIT 5
''').dataframe

```

{{</ faq >}}



{{< faq "Can you use a groupby to get the counts of players per year?">}}

```python
dw.query(con_url, 
'''
SELECT yearid, -- <stuff to calculate>
FROM AllstarFull
WHERE yearid > 1999 
    AND gp != 1
GROUP BY --?
ORDER BY --?
''').dataframe
```

{{</ faq >}}



{{< faq "What table do we want for the post season at bats?">}}

```python
dw.query(con_url, 
'''
SELECT *
FROM BattingPost as bp
LIMIT 5
''').dataframe
```

{{</ faq >}}

{{< faq "Can you join the batting table and AllStar information and keep only the at bats, hits with the all star gp and gameid columns?">}}

__Let's only keep players with at least one at bat in the post season__

```python
dw.query(con_url, 
'''
SELECT -- <columns to keep>
FROM BattingPost as bp
JOIN AllstarFull as asf
    ON  -- <two columns for the join>
WHERE bp.yearid > 1999
    AND gp != 1
    AND -- <at bat condition>
LIMIT 15

'''
).dataframe
```
{{</ faq >}}

{{< faq "Let's build the final table">}}


__For seasons after 1999, which year had the most players selected as All Stars but didn't play in the All Star game?__

- __Provide a summary of how many games, hits, and at bats occurred by those players had in that years post season.__

```python
dw.query('byuidss/cse-250-baseball-database', 
'''
SELECT -- <lots of calculations>
FROM BattingPost as bp
JOIN AllstarFull as asf
    ON  bp.playerid = asf.playerid AND
        bp.yearid = asf.yearid
WHERE bp.yearid > 1999
    AND gp != 1
    AND ab > 0
GROUP BY -- <column>
ORDER BY -- <column>
'''
).dataframe
```
{{</ faq >}}

#### I get SQL and want to be challenged.


[Do this Math 335 task with SQL commands in Python](https://byuistats.github.io/M335/class_tasks/task12_details.html).