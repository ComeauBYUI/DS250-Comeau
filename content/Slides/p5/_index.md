---
title: "Week 10-11: Project 5 - The War with Star Wars"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-15T10:42:26+06:00
weight: 3
draft: false
# search related keywords
keywords: [""]
---


{{% notice info %}}
A significant portion of a data scientist's job is data cleaning.  During these two weeks, we will not hide the data munging from you.  We will practice data cleaning using a Star Wars survey from [FiveThirtyEight](https://fivethirtyeight.com/). Survey data is notoriously difficult to handle.  Even when the data is recorded cleanly the options for ‘write in questions’, ‘choose from multiple answers’, ‘pick all that are right’, and ‘multiple choice questions’ makes storing the data in a tidy format difficult.
{{% /notice %}}


{{% notice note %}}

**Completed Readings:**  [Python for Data Science: Tidy Data](https://byuidatascience.github.io/python4ds/tidy-data.html), [Python for Data Science: Graphics for Communication](https://byuidatascience.github.io/python4ds/graphics-for-communication.html), and [Python for Data Science: Strings](https://byuidatascience.github.io/python4ds/strings.html)


{{% /notice %}}

{{% notice tip %}}
Use the [StarWars.csv](https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv) from [FiveThirtyEights Github account](https://github.com/fivethirtyeight) and read the [article](https://fivethirtyeight.com/features/americas-favorite-star-wars-movies-and-least-favorite-characters/)


{{% /notice %}}

### Grand Questions

1. __Please validate that the data provided on GitHub lines up with the article by recreating 2 of their visuals and calculating 2 summaries that they report in the article.__
   1. __Shorten the column names and clean them up for easier use with pandas.__
   1. __Filter the dataset to those that have seen at least one film.__
1. __Clean and format the data so that it can be used in a machine learning model. Please acheive the following requests and provide examples of the table with a short description the changes made in your report.__
   1. __One-hot encode all columns that have categories.__
   1. __Convert all yes/no responses to 1/0 numeric.__
   1. __Create an additional column that converts the income ranges to a number.__
   1. __Create an additional column that converts the age ranges to a number.__
   1. __Create an additional column that converts the school groupings to a number.__
1. __Build a machine learning model that predicts whether a person makes more than $50k.__
