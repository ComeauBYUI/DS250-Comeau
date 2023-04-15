---
title: "Day 2: Python for DS Introduction"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-17T10:42:26+06:00
weight: 1
draft: false
# search related keywords
keywords: [""]
---


## Finishing some setup


### Reading for Comprehensions VS. Reading for Reference

- How do we use the readings in this class?

{{< faq "What does `TL;DR` mean?">}}

Reading is the secret! Careful reading of material provided will bless you now and in the long run.

- [The idea of the Holy: 256 pages](https://www.amazon.com/Idea-Holy-R-Otto/dp/0195002105)
- [Journal Articles (I swear I have read this article almost 100 times)](https://pubs.acs.org/doi/abs/10.1021/es950733x)
- [Optional References](../../projects/introduction/)

> Read 500 pages like this every day. That’s how knowledge works. It builds up, like compound interest. All of you can do it, but I guarantee not many of you will do it.
>
> -[Warren Buffett](https://www.cnbc.com/2016/11/16/warren-buffetts-reading-routine-could-make-you-smarter-suggests-science.html)

{{</ faq >}}



{{< faq "Any issues with getting Python installed?">}}

> - [Python](https://www.python.org/downloads/)
> - [VS Code](https://code.visualstudio.com/)
> - [Altair in VS Code](../../../course-materials/altair)

{{</ faq >}}


{{< faq "Does everyone have `pandas`, `altiar`, `numpy`, `scikit-learn` installed?">}}

> - [VS Code, Python, and packages](../../../course-materials/vs-code/)


```bash
python -m pip install pandas altair sklearn
```

{{</ faq >}}



{{< faq "Does everyone have `altair-saver` working?">}}

- [altair_saver GitHub](https://github.com/altair-viz/altair_saver)
- [Altair Charts and NodeJS](../../../course-materials/altiar/)

{{</ faq >}}


{{< faq "Why aren't we using conda?">}}

Because VS Code fixed all the problems that I have historically had with pip.  It just works now and is the method our students have been taught in CSE 110 and CSE 111.

> - [pip and conda](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)

![](https://imgs.xkcd.com/comics/python_environment_2x.png)

{{</ faq >}}

## Can we practice making a chart in Altair with VS Code?

{{< faq "What can Python Interactive do?">}}

## Let's review the power of [Python Interactive](https://code.visualstudio.com/docs/python/jupyter-support-py)

> - `# %%` in my `.py` script is much better than Jupyter notebooks (`.ipynb`). 
>     - If we hope to have our code work in a production environment then Jupyter is problematic.
>     - Caching and code chunks are problematic
>     - https://medium.com/@_orcaman/jupyter-notebook-is-the-cancer-of-ml-engineering-70b98685ee71 

{{</ faq >}}



{{< faq "Set-up your `py` script">}}

## Setting up your script

> __A good data science `.py` script will have packages and data loaded at the top. Usually you have a few short commented sentences that descibe the script purpose.__

   ```python
   # %%
   # import pandas, altair, numpy
   import pandas as pd
   import altair as alt
   import numpy as np

   # %%
   # load data
   # handgrenade data https://github.com/byuidatascience/data4soils/blob/master/data-raw/cfbp_handgrenade/cfbp_handgrenade.csv
   
   url = 'https://github.com/byuidatascience/data4soils/raw/master/data-raw/cfbp_handgrenade/cfbp_handgrenade.csv'
   
   dat = pd.read_csv(url)

   ```

{{</ faq >}}


{{< faq "Make a scatter plot with `hmx` on the x and `rdx` on the y">}}

```python
alt.Chart(dat).encode()
```

{{</ faq >}}


{{< faq "Make a spatial plot with `hmx` colored">}}

1. Encode the `row` and `column` to the axes.
2. Color the `hmx` points using the 'goldorange' color scheme.
3. Use `mark_square()` and make the square sizes 500.

{{</ faq >}}


{{< faq "Create a histogram of `hmx`">}}

1. Encode the x-axis as binned.
2. Encode the y-axis as counts.
3. Configure the title to a `fontSize` of 20.
4. Use properties to place the title.

{{</ faq >}}
