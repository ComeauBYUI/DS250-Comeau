---
title: "Day 5: Making your name stand out."
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-22T10:42:26+06:00
weight: 2
draft: false
# search related keywords
keywords: [""]
---

## Coding Methods and Calculation Questions

Let's review canvas and make sure we understand the checkpoints.

## Partner Programming Activity


## How does your name at your birth year compare to its use historically?


> To be truthful and revealing, data graphics must bear on the question at the heart of quantitative thinking: "Compared to what?" The emaciated, data-thin design should always provoke suspicion, for graphics often lie by omission, leaving out data sufficient for comparisons. [Edward Tufte](https://medium.com/@AnyChart/advices-by-edward-tufte-importance-of-context-for-charts-819396300255)


{{< faq "What are some charts types we could use to answer this question?">}}

__There is a clear first choice, but I think there are a few other choices that could provide insight.__

> - [Visualization Catalog](https://datavizcatalogue.com/)
> - [Altair Example Gallery](https://altair-viz.github.io/gallery/index.html)

<iframe src="http://ipadstopwatch.com/timer-fullscreen.html" frameborder="0" scrolling="no" width="425" height="340"></iframe>


{{</ faq >}}



{{< faq "Use the `query()` method and `filter()` method to get your name and years in the rows with and include the `name`, `year`, and `Total` columns">}}

> 1. filter the data down to your names (`query`)
> 2. select the pertinent columns (`filter()`)
> 3. Create a new data object for your name. 

{{</ faq >}}

{{< faq "Create a chart with lines and dots to chart the data">}}

```python
base = (alt.Chart()
    .encode(
        alt.X(''),
        alt.Y('')
    )
`"

{{</ faq >}}


{{< faq "Create a new DataFrame with your birthday information in the row">}}

> 1. Create a `DataFrame` with `x`, `y`, and `label` as columns. [help](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

<iframe src="https://beepmyclock.com/widget/timer" frameborder="0" style="border:0;height:150px;width:600px" scrolling = "no"></iframe>


{{</ faq >}}


{{< faq "Add the vertical rule mark to show your birthday">}}

> - [Using layered charts](https://altair-viz.github.io/user_guide/compound_charts.html)
> - [Altair Marks](https://altair-viz.github.io/user_guide/marks.html)
> - [Add a horizontal line to an existent chart](https://github.com/altair-viz/altair/issues/2059)

<iframe src="https://beepmyclock.com/widget/timer" frameborder="0" style="border:0;height:150px;width:600px" scrolling = "no"></iframe>

{{</ faq >}}


{{< faq "Work with your partner to create a line chart that includes both of your names?">}}

> - Can you include total and data for the state in which you were born?
> - Work together to make the code as eloquent as possible.
> - [compound charts](https://altair-viz.github.io/user_guide/compound_charts.html)

<iframe src="https://beepmyclock.com/widget/timer" frameborder="0" style="border:0;height:150px;width:600px" scrolling = "no"></iframe>

{{</ faq >}}


{{< faq "Can you modify your previous chart to include your birth state?">}}

> - Can you include `Total` and your birth state?
> - Is there a better metric than raw counts that you could calculate?
> - Are there good labels that you could include on the chart ([`mark_text()`](https://altair-viz.github.io/gallery/bar_chart_with_labels.html#gallery-bar-chart-with-labels))?

<iframe src="https://beepmyclock.com/widget/timer" frameborder="0" style="border:0;height:150px;width:600px" scrolling = "no"></iframe>


{{</ faq >}}


{{< faq "Now come up with a different chart than a line chart">}}

__Just use your state count our the `Total` count for your name.__

<iframe src="https://beepmyclock.com/widget/timer" frameborder="0" style="border:0;height:150px;width:600px" scrolling = "no"></iframe>


{{</ faq >}}

