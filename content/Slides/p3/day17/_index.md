---
title: "Day 17: How do I check my SQL work?"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 2
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

## Connecting to SQLite: [Lahman SQLite](https://byuistats.github.io/CSE250-Course/data/lahmansbaseballdb.sqlite)

__Download the sqlite file:__ [Lahman sqlite](https://byuistats.github.io/CSE250-Hathaway/data/lahmansbaseballdb.sqlite)

### What is SQLite?

> - [Wikipedia](https://en.wikipedia.org/wiki/SQLite): SQLite is **a popular choice as embedded database software for local/client storage in application software such as web browsers.** It is arguably the most widely deployed database engine, as it is used today by several widespread browsers, operating systems, and embedded systems (such as mobile phones), among others. SQLite has bindings to many programming languages.

> - [SQLite.org](https://www.sqlite.org/about.html): **SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.** The code for SQLite is in the public domain and is thus free for use for any purpose, commercial or private. SQLite is the most widely deployed database in the world with more applications than we can count, including several high-profile projects.

> - [Codecademy](https://www.codecademy.com/articles/what-is-sqlite): SQLite is a database engine. It is software that allows users to interact with a relational database. In SQLite, a database is stored in a single file — a trait that distinguishes it from other database engines. This fact allows for a great deal of accessibility: copying a database is no more complicated than copying the file that stores the data, sharing a database can mean sending an email attachment.

### Working with SQLite files in Python

[The Schema Table in SQLite](https://www.sqlite.org/schematab.html#:~:text=Every%20SQLite%20database%20contains%20a,are%20contained%20within%20the%20database.)


```python
# %%
import pandas as pd 
import altair as alt
import numpy as np
import sqlite3

# %%
sqlite_file = 'lahmansbaseballdb.sqlite'
con = sqlite3.connect(sqlite_file)
# %%
# See the tables in the database
table = pd.read_sql_query(
    "SELECT * FROM sqlite_master WHERE type='table'",
    con)
print(table.filter(['name']))
print('\n\n')
# 8 is collegeplaying
print(table.sql[8])

```

## Work with a subset in pandas

Often, you can pull a small subset of the data and work through the logic in Python to make sure you are working out the logic correctly.

1. Only want to pull small parts of each table needed.
2. Small part should be a a complete division.  For example, lets use Idaho.
3. Then use Pandas to work out all the table join logic.
4. Check your work against the SQL call.

### How can we check our SQL logic?

__For seasons after 1999, which year had the most players selected as All Stars but didn't play in the All Star game?__

- __Provide a summary of how many games, hits, and at bats occurred by those players had in that years post season.__

```python
pd.read_sql_query(
'''
SELECT bp.yearid, sum(ab) as ab, sum(h) as h,
    sum(g) as games, count(DISTINCT bp.playerid) as num_players, 
    asf.gp, asf.gameid
FROM BattingPost as bp
JOIN AllstarFull as asf
    ON  bp.playerid = asf.playerid AND
        bp.yearid = asf.yearid
WHERE bp.yearid > 1999
    AND gp == 0
GROUP BY bp.yearid
ORDER BY bp.yearid
''',
con)
```
#### Let's start by pulling a subset of our two tables

```python
bp = pd.read_sql_query(
'''
SELECT *
FROM battingpost
WHERE yearid == 2017
''', con)

alst = pd.read_sql_query(
'''
SELECT *
FROM allstarfull
WHERE yearid == 2017
''', con)

```

__Now we can join them__

```python
bp_noals = (bp.merge(
        alst.filter(['playerID', 'yearID', "GP"]), 
        on = ['playerID', 'yearID'])
    .query('GP == 0'))
```

__Using `.groupby()`, `agg()`, and `.reset_index()` lets recreate the year 2017 line.__ We can use `'sum'` and `'nunique'` in our `.agg()` method.


### An extra use case for those that want to dig deeper.

<!-- see d17_old.py -->

> I want to see how much money each college player from schools in the west and mountain west has made over their professional career. I want to know the full school name attended and the the Given name of each player.

_Is this query correct?_

```SQL
SELECT cp.playerID, nameGiven, birthYear
    ,cp.schoolID, name_full
    ,SUM(salary) as salary
FROM salaries as sal
JOIN people as p
    ON p.playerID = sal.playerID
JOIN CollegePlaying as cp
    ON p.playerID = cp.playerID
JOIN schools as sc
    ON sc.schoolID = cp.schoolID
WHERE sc.state = 'ID'
GROUP BY cp.playerID, cp.schoolID
ORDER BY name_full
```

```python
pd.read_sql_query(
'''
SELECT cp.playerID, nameGiven, birthYear
    ,cp.schoolID, name_full
    ,SUM(salary) as salary
FROM salaries as sal
JOIN people as p
    ON p.playerID = sal.playerID
JOIN CollegePlaying as cp
    ON p.playerID = cp.playerID
JOIN schools as sc
    ON sc.schoolID = cp.schoolID
WHERE sc.state = 'ID'
GROUP BY cp.playerID, cp.schoolID
ORDER BY name_full
''', con) 
```

#### Let's start here

```python
schools = pd.read_sql_query(
'''
SELECT *
FROM schools
WHERE state = 'ID'
''', con)
```