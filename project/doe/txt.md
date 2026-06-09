# Comparing Two Treatments

- Compare two conditions, treatments, recipes, methods, or processes.
- Decide whether the sample difference suggests a real population difference.
- Use **statistical hypothesis testing** as the analysis framework.
- Use the **two-sample t-test** to compare two population means.
- Use the pooled t-test version when its assumptions are appropriate.

## Basic Visualization

> How sample data describe a larger population?

A **sample** is a smaller set of *observations* taken from a larger *population*.

Sample data can be summarized numerically with:

- The **sample mean**, or sample average
- The **sample variance**
- The **sample standard deviation**

These summaries describe the center and spread of the observed data. While we may have same parameters for **population**.

[Graphical summaries: sample vs. population](review_basic_statistics.ipynb)

Graphical summaries help reveal center, spread, and shape.
- Box plots summarize data using (25th and 75th) percentiles, medians, and whiskers (min and max).
- For small samples, dot diagrams or stem-and-leaf plots are usually easier to read than histograms.

[Example: Portland cement visual comparison](portland_cement_example.ipynb)

## Hypothesis Testing Framework

The statistical method used to investigate this conjecture is **statistical hypothesis testing**.

### Sampling Situation

The hypothesis-testing picture starts with two probability distributions:

- Population 1: measurements from factor level 1, or treatment 1.
- Population 2: measurements from factor level 2, or treatment 2.
- In the Portland cement problem, the two populations represent the two mortar formulations.

Assumptions:

- Observations from population 1 and 2 are normally distributed.
- Population 1 has mean $\mu_1$ and variance $\sigma_1^2$.
- Population 2 has mean $\mu_2$ and variance $\sigma_2^2$.

### Hypotheses

The claim being investigated is that the two population means are the same.

The hypotheses are:

$$
H_0: \mu_1 = \mu_2
$$

$$
H_1: \mu_1 \ne \mu_2
$$

- $H_0$ is the **null hypothesis**.
- $H_0$ says the two means are equal.
- $H_1$ is the **alternative hypothesis**.
- $H_1$ says the two means are not the same.

## Mortar Summary Statistics

Each population has:

- A mean $\mu$
- A variance $\sigma^2$

These are estimated with sample statistics.

### Sample Mean

The sample average $\bar{y}$ estimates the population mean $\mu$.

To calculate it:

- Add all observations in the sample.
- Divide by the sample size $n$.

$$
\bar{y} = \frac{\sum_{i=1}^{n} y_i}{n}
$$

### Sample Variance

The sample variance estimates the population variance $\sigma^2$.

To calculate it:

- Subtract the sample average from each observation.
- Square those differences.
- Add the squared differences.
- Divide by $n - 1$.

$$
s^2 = \frac{\sum_{i=1}^{n}(y_i - \bar{y})^2}{n - 1}
$$

These calculations are straightforward and can be done with pocket calculators or statistical software.

The book also shows these calculations.

### Results for the Mortar Data

For the new recipe, the modified mortar:

- Sample mean: $\bar{y}_1 = 16.76$
- Sample variance: $s_1^2 = 0.100$
- Sample standard deviation: $s_1 = 0.316$
- Sample size: $n_1 = 10$

For the original recipe, the unmodified mortar:

- Sample mean: $\bar{y}_2 = 17.06$
- Sample variance: $s_2^2 = 0.061$
- Sample standard deviation: $s_2 = 0.248$
- Sample size: $n_2 = 10$

The standard deviations are not exactly the same, but they are fairly close.

This agrees with the earlier dot diagrams and stem-and-leaf plots:

- The sample means looked noticeably different.
- The sample spreads looked fairly similar.
- The summary statistics reflect the same pattern.

Source note:

- The updated transcript reports $\bar{y}_2 = 17.06$.
- It also reports $\bar{y}_1 - \bar{y}_2 = -0.28$.
- The difference $-0.28$ matches $16.76 - 17.04$, not $16.76 - 17.06$.
- The transcript detail is kept here because it affects the numerical example.

## Test Statistic Idea

The two-sample t-test is used to test:

$$
H_0: \mu_1 = \mu_2
$$

The procedure uses the sample means to draw conclusions about the population means.

The key quantity is the difference in sample means:

$$
\bar{y}_1 - \bar{y}_2
$$

Using the transcript's numerical example:

$$
\bar{y}_1 - \bar{y}_2 = -0.28
$$

The test divides the difference in sample means by the standard deviation of that difference.

This ratio measures how different the sample means are in **standard deviation units**.

### Standard Deviation of a Sample Mean

For one sample mean:

$$
\sigma_{\bar{y}}^2 = \frac{\sigma^2}{n}
$$

That is, the variance of the sample average is the variance of an individual observation divided by the sample size.

### Standard Deviation of the Difference in Sample Means

For two independent sample means:

$$
\sigma_{\bar{y}_1 - \bar{y}_2}^2 =
\frac{\sigma_1^2}{n_1}
+
\frac{\sigma_2^2}{n_2}
$$

The independence assumption is reasonable here because:

- The two samples are completely different samples.
- They were generated at different times.
- They are random samples.
- The treatments were applied essentially in random sequence.

### Known-Variance Statistic

If the variances were known, the statistic would be:

$$
z_0 =
\frac{\bar{y}_1 - \bar{y}_2}
{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}
$$

- The numerator is the difference in sample averages.
- The denominator is the standard deviation of the difference in sample means.
- If $\sigma_1^2$ and $\sigma_2^2$ were known, $z_0$ would follow a normal distribution.
- If $\mu_1 = \mu_2$, then $z_0$ would follow a standard normal distribution with mean 0 and variance 1.

For illustration, suppose:

$$
\sigma_1 = \sigma_2 = 0.3
$$

Plugging into the statistic gives:

$$
z_0 = -2.09
$$

## Fixed Significance Level Test

The question is how unusual $z_0 = -2.09$ would be if the two population means were really equal.

If $H_0$ is true, then $z_0$ has a standard normal distribution.

For a standard normal distribution:

- 95% of the probability lies between $-1.96$ and $+1.96$.
- $+1.96$ is the upper 2.5% point of the standard normal distribution.
- It is denoted $z_{0.025}$.
- $-1.96$ is the lower 2.5% point.

So, if the population means are equal:

- Most observed $z_0$ values should fall between $-1.96$ and $+1.96$.
- A value like $z_0 = -2.09$ is unusual.
- It would occur less than 5% of the time if the population means were equal.
- This is evidence that the population means may not be equal.

### Using the Standard Normal Table

The critical value 1.96 can be found from a standard normal cumulative distribution table.

Most standard normal tables:

- List positive $z$ values from 0 up to about 3.99.
- Give areas to the left of positive $z$ values.
- Use rows and columns to locate the desired $z$ value.

For $z = 1.96$:

- Use the 1.9 row.
- Use the .06 column.
- The table entry is 0.975.
- This means the area to the left of 1.96 is 0.975.
- The upper tail area is $1 - 0.975 = 0.025$.

Because the normal distribution is symmetric:

- Areas to the left of negative $z$ values match areas to the right of positive $z$ values.
- This makes it easy to handle negative test statistics such as $z_0 = -2.09$.

### Decision

For a 5% two-sided test:

- The critical values are $-1.96$ and $+1.96$.
- The calculated value is $z_0 = -2.09$.
- Since $-2.09$ is outside the interval $[-1.96, +1.96]$, reject $H_0$.

A statistician would say:

- Reject the null hypothesis at the 5% level of significance.
- The result is a fairly strong indication that the two means are not equal.

This is a **fixed significance level test** because:

- The test statistic is compared with a critical value.
- The critical value, here 1.96, is selected in advance before running the experiment.
- The standard normal distribution is the **reference distribution** for this known-variance test.

## P-Value Approach

Another common approach is the **P-value approach**.

- The P-value is the observed or actual significance level.
- For the Z-test, the P-value is easy to find from the standard normal distribution.
- The transcript introduces this approach but says it will be shown next time.
