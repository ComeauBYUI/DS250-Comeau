---
title: "Day 21: Validating our ML model"
date: 2020-05-01T11:02:05+06:00
lastmod: 2020-09-01T10:42:26+06:00
weight: 2
draft: false
# search related keywords
keywords: [""]
---

## Investigating Machine Learning Models

> Applied data scientists make their mark by justifying a machine learning model.   
> <>    
> 1. We 'justify' the model algorithm.
> 2. We 'justify' the model fit.

## Justify a model algorithm

We are focusing on [supervised learning](https://scikit-learn.org/stable/supervised_learning.html).  There is another space of machine learning focused on [unsupervised learning](https://scikit-learn.org/stable/unsupervised_learning.html).

{{< faq "How many supervised ML models does scikit-learn have?">}}

- [17 different categories](https://scikit-learn.org/stable/supervised_learning.html)
- Many different 'model algorithms' under each category. Each algorithm has a high-level summary with a simple example.
    - [Linear Models](https://scikit-learn.org/stable/modules/linear_model.html) has at least 17 and represents the set of methods I was familiar with after a graduate degree in statistics.
    -  [Ensemble methods](https://scikit-learn.org/stable/modules/ensemble.html#) has at least eight algorithms.  We want to use the [Gradient Tree Boosting](https://scikit-learn.org/stable/modules/ensemble.html#gradient-tree-boosting).

{{</ faq >}}

{{< faq "What are boosted algorithms, and why would we use them?">}}

This is the beginning of the rabbit hole. We could have weeks of class on each algorithm ([ref](https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/)).  It works well.  Let's settle on that for now.

- __[Gradient Tree Boosting](https://scikit-learn.org/stable/modules/ensemble.html#gradient-tree-boosting)__


{{</ faq >}}


{{< faq "How would I compare two different algorithm's performance?">}}

I would use the output from the model fit for each to compare performance.

{{</ faq >}}

## Justify model fit

{{< faq "What does model fit mean?">}}

> Model fitting is a measure of how well a machine learning model generalizes to similar data to that on which it was trained. A model that is well-fitted produces more accurate outcomes. A model that is overfitted matches the [sample] data too closely. A model that is underfitted doesn’t match [either the sample data or the population] closely enough. [ref](https://www.datarobot.com/wiki/fitting/)

While statisticians can be data scientists and data scientists can be statisticians.  The below description generalizes how justification happens.

- __Statisticians justify:__ Comparing sample data to parametric fit assumption (math principles that explain the inference from the data) - for example, normality of errors, independence, linearity.

- __Data Scientists justify:__ Comparing the predictions from our model to the measured values (Results-oriented justification that supports inference). Data scientist justification depends on training and testing sample data.  The inference process explains metrics like correlation or precision on the testing sample data to justify the results.

[ref](https://towardsdatascience.com/clearly-explained-how-machine-learning-differs-from-statistical-modeling-967f2c5a9cfd)

{{</ faq >}}

{{< faq "How do I justify model fit with classification models?">}}

### `sklearn.metrics` descriptions

> - [Classification Metrics in scikit-learn](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)

#### Confusion matrix

```python
print(metrics.confusion_matrix(y_test, predict_p))
metrics.plot_confusion_matrix(classifier, X_test, y_test)
```

#### Everything evolves from the confusion matrix

__Can we create the classification report?__

- [Classification report](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-report)
- [Confusion Matrix Example](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)

```python
from sklearn.metrics import classification_report
```

#### ROC Curves

__Use the code from the following link to build a ROC curve for our data.__

- [How to Use ROC Curves and Precision-Recall Curves for Classification in Python](https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/)
- [sklearn.metrics.roc_curve()](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)

```python
metrics.plot_roc_curve(clf, X_test, y_test)
```

{{</ faq >}}


{{< faq "What is feature importance?">}}

## Plotting feature importance

__What do we need from our model to create this plot?__

![](https://scikit-learn.org/dev/_images/sphx_glr_plot_permutation_importance_001.png)

- [ref 1](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)

```python
df_features = pd.DataFrame(
    {'f_names': X_train.columns, 
    'f_values': clf.feature_importances_}).sort_values('f_values', ascending = False)
```

{{</ faq >}}
