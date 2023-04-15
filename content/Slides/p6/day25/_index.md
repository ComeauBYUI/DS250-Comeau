---
title: "Day 25: Resumes and Coding Challenges"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-10-12T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---

## What the fork?

Now is time for you to find a partner that will edit your resume.  You are going to want to keep the same partner.

1. Each of you `fork` the other student's repository that has edits.
2. Now, you want to clone that forked repository to your computer.
3. On your local version of the forked repository, do the following;   
   A. Create a new file called `edits.md` and save it in the main folder or the repository.   
   B. Make a few recommendations or notes about what each of you discussed about your resumes in the file.   
   C. `add, commit, push` your edits.   
   D. Go to the forked repo on GitHub and check to see if the `edits.md` file is in yours.   
4. Now, create a `pull request` to get your edits into your partner's original repo.

## On Data Science Resumes

> [byuidatascience.github.io](https://byuidatascience.github.io/resume_example.html)   
> [undergraduate ds resumes](https://byuidatascience.github.io)   
> [Hathaway's resume](http://jhathaway.io/extra/hathaway.pdf)   

## Creating a fork on [byuids-resumes](https://github.com/byuids-resumes)

## Questions on resumes (open time to finalize your resume)

## Coding Challenge Example

_I will ask you to complete coding about as challenging as what is shown below.  Plus, you will need to fit a Machine Learning model with data I provide._ __Remember, you will only have 60 minutes.__

- [challenge template](../../../template/challenge_template.md)
### Practice Challenge


```python

import pandas as pd
import altair as alt
import numpy as np

dat = pd.read_csv('https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.csv')

```


1. Try recreating this chart using the [mtcars missing](https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.csv).

- Note that `hp` has missing values, and you will have to replace them with the mean.
- Please drop all cars with a missing name.

![](practice_mtcars.png)

2. Try writing code to recreate the following table.

- Have `cyl` on the rows and `carb` on the columns
- Each value shows the counts of each.

The [pivot_table](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html#pandas.pivot_table) function could prove valuable as well as [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) and [agg](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html).


|   cyl |   1 |   2 |   3 |   4 |   6 |   8 |
|------:|----:|----:|----:|----:|----:|----:|
|     4 |   5 |   4 |   0 |   0 |   0 |   0 |
|     6 |   2 |   0 |   0 |   4 |   1 |   0 |
|     8 |   0 |   3 |   3 |   5 |   0 |   1 |

3. I will also ask you to fit a Machine Learning Model as well.
