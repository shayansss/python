# Comparing Two Treatments

This chapter explains how to compare two treatments using statistical inference, from visualizing sample data to testing differences in population means. It covers independent and paired t-tests, pooled and Welch methods, assumptions, P-values, and confidence intervals.

## Basic Visualization

> How sample data describe a larger population?

A **sample** is a smaller set of *observations* taken from a larger *population*.

Sample data can be summarized numerically with:

- The **sample mean**, or sample average
- The **sample variance**
- The **sample standard deviation**

These summaries describe the center and spread of the observed data. While we may have same parameters for **population**.

<details>
<summary>Graphical summaries: sample vs. population</summary>

[Open the graphical summaries notebook](review_basic_statistics.ipynb)

Graphical summaries help reveal center, spread, and shape.

- Box plots summarize data using (25th and 75th) percentiles, medians, and whiskers (min and max).
- For small samples, dot diagrams or stem-and-leaf plots are usually easier to read than histograms.

</details>

## Basic Hypothesis Testing

<details>
<summary>A hypothesis test determines whether sample evidence is too unusual under a null claim to be explained reasonably by sampling variation alone.</summary>

Because different random samples produce different results, an observed difference does not automatically imply a real population difference. Hypothesis testing therefore follows conditional logic:

1. Temporarily assume that the null hypothesis is true.
2. Determine which results would be expected under that assumption.
3. Compare the observed result with those expected results.
4. Reject the assumption only when the observed evidence is sufficiently incompatible with it.

</details>

### State the Hypotheses

Let $\theta$ denote the population parameter of interest and $\theta_0$ the value being tested:


| Null hypothesis | Alternative hypothesis | Test type |
| --- | --- | --- |
| $H_0:\theta=\theta_0$ | $H_1:\theta\ne\theta_0$ | Two-sided |
| $H_0:\theta\leq\theta_0$ | $H_1:\theta>\theta_0$ | Upper-tailed |
| $H_0:\theta\geq\theta_0$ | $H_1:\theta<\theta_0$ | Lower-tailed |


<details>

- The **null hypothesis**, $H_0$, is the baseline claim used to calculate probabilities.
- The **alternative hypothesis**, $H_1$, describes the effect or difference for which evidence is sought.
- The null hypothesis always includes equality; the test is calculated at the boundary $\theta=\theta_0$.

</details>


### Sampling Variation and Standard Error

Suppose $\hat\theta$ is a sample estimate of $\theta$. Its value changes from sample to sample. The probability distribution of $\hat\theta$ across repeated samples is its **sampling distribution**.

The **standard error** measures the standard deviation of that sampling distribution:

$$
SE(\hat\theta)
=
\sqrt{\operatorname{Var}(\hat\theta)}
$$

Standard errors generally decrease as the sample size increases, although their exact formula depends on the design and estimator.

### Construct a Test Statistic

A test statistic compares the estimated effect with its value under $H_0$ and scales the difference by its standard error:

$$
\text{test statistic}
=
\frac{\text{estimate}-\text{hypothesized value}}
{\text{standard error of the estimate}} =
\frac{\hat\theta-\theta_0}
{SE(\hat\theta)}
$$

- A value near zero is usually consistent with $H_0$, whereas a value far from zero may support $H_1$.
- The **null distribution** or **reference distribution** describes the possible values of $T$ (test statistic) when $H_0$ is true.

### Choose a Significance Level

**Type I error**: The significance level $\alpha$ is selected before analyzing the data. It is the maximum long-run probability of rejecting $H_0$ when it is actually true:

$$
P(\text{reject }H_0\mid H_0\text{ is true})\leq\alpha
$$

Common choices include $\alpha=0.05$ and $\alpha=0.01$.

**Type II error**: it occurs when the test fails to reject $H_0$ even though a specified alternative value $\theta_a$ is true. Its probability is denoted by $\beta(\theta_a)$:

$$
P_{\theta_a}(\text{fail to reject }H_0)=\beta(\theta_a)
$$

The **power** of a test is the probability of detecting that alternative:

$$
\text{Power at }\theta_a=1-\beta(\theta_a)
$$

| Reality | Reject $H_0$ | Fail to reject $H_0$ |
| --- | --- | --- |
| $H_0$ is true | Type I error, probability $\alpha$ | Correct decision |
| $H_1$ is true | Correct decision; power $1-\beta$ | Type II error, probability $\beta$ |

Reducing $\alpha$ without increasing the sample size can reduce power, so error rates should be considered during experimental design rather than only after data collection.

### Use a Critical Value or P-Value

Two equivalent approaches can be used at the same significance level:

- **Critical-value approach:** Use the null distribution to define a rejection region whose total probability under $H_0$ is $\alpha$. Reject $H_0$ when the test statistic falls in that region.
- **P-value approach:** Calculate the probability, assuming $H_0$ is true, of obtaining a test statistic at least as extreme as the observed value in the direction specified by $H_1$.

E.g., for a symmetric two-sided test, the critical-value rule often has the form:

$$
\text{Reject }H_0
\quad\text{when}\quad
|T|>c_{\alpha/2}
$$

The P-value decision rule is:

$$
\begin{cases}
\text{Reject }H_0, & \text{if P-value}\leq\alpha,\\
\text{Fail to reject }H_0, & \text{if P-value}>\alpha.
\end{cases}
$$

The P-value is the smallest significance level at which the observed result would be rejected by the same test.

### Relationship With Confidence Intervals

A hypothesis test gives a decision about a specified value, whereas a confidence interval shows a range of parameter values compatible with the data. For a two-sided test of:

$$
H_0:\theta=\theta_0
$$

at significance level $\alpha$, the matching $100(1-\alpha)\%$ confidence interval gives the same decision when both use the same model and assumptions:

$$
\theta_0\notin\text{confidence interval}
\quad\Longleftrightarrow\quad
\text{reject }H_0
$$

The interval is usually more informative because it displays both the estimated effect size and its precision.


## Applying Hypothesis Testing to Two Treatments

The general framework can now be applied to two treatments. Here, the parameter of interest is the difference between two population means, $\mu_1-\mu_2$, and the sample estimate is $\bar y_1-\bar y_2$.

### Sampling Situation

The hypothesis-testing picture starts with two probability distributions:

- Population 1: measurements from factor level 1, or treatment 1.
- Population 2: measurements from factor level 2, or treatment 2.

Assumptions:

- Observations from population 1 and 2 are normally distributed.
- Population 1 has mean $\mu_1$ and variance $\sigma_1^2$.
- Population 2 has mean $\mu_2$ and variance $\sigma_2^2$.

### Parameters and Hypotheses

For a two-sided comparison, equality of the population means is the null hypothesis:

$$
H_0: \mu_1 = \mu_2
$$

$$
H_1: \mu_1 \ne \mu_2
$$

Equivalently, these hypotheses test whether the population mean difference is zero:

$$
H_0:\mu_1-\mu_2=0
\qquad\text{versus}\qquad
H_1:\mu_1-\mu_2\ne0
$$

<details>
<summary>Example: Portland cement setup and visual comparison</summary>

[Open the Portland cement notebook](portland_cement_example.ipynb)

The example asks whether there is statistical evidence that the mean tension bond strength differs between two mortar recipes. The two populations represent the two mortar formulations, so the question leads naturally to a two-sample hypothesis test.

</details>

## Summary Statistics

Each population has:

- A mean $\mu$
- A variance $\sigma^2$

These are estimated with sample statistics.

### Sample Mean

The sample average $\bar{y}$ estimates the population mean $\mu$:

$$
\bar{y} = \frac{\sum_{i=1}^{n} y_i}{n}
$$

### Sample Variance

The sample variance estimates the population variance $\sigma^2$:

$$
s^2 = \frac{\sum_{i=1}^{n}(y_i - \bar{y})^2}{n - 1}
$$

<details>
<summary>Example: Portland cement sample summaries</summary>

The standard deviations are not exactly the same, but they are fairly close.

This agrees with the earlier dot diagrams and stem-and-leaf plots:

- The sample means looked noticeably different.
- The sample spreads looked fairly similar.
- The summary statistics reflect the same pattern.

</details>

### Test Statistic Idea

The two-sample t-test is used to test:

$$
H_0: \mu_1 = \mu_2
$$

The procedure uses the sample means to draw conclusions about the population means.

The key quantity is the difference in sample means:

$$
\bar{y}_1 - \bar{y}_2
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

This formula requires the two sample means to be independent. Independence is generally supported when the samples contain different experimental units and observations are obtained through random sampling or randomized treatment assignment.

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

### Applying the Critical-Value Rule

If $H_0$ is true, $z_0$ has a standard normal distribution. For a two-sided test with significance level $\alpha$, reject the null hypothesis when:

$$
|z_0|>z_{\alpha/2}
$$

and fail to reject it when $|z_0|\leq z_{\alpha/2}$. The critical value is selected before analyzing the data; at $\alpha=0.05$, it is $z_{0.025}=1.96$.

<details>
<summary>Example: Portland cement fixed-level Z-test</summary>

For the Portland cement data, the illustrative known-variance statistic is $z_0=-2.09$. Because:

$$
|z_0|=2.09>1.96
$$

the statistic falls in the rejection region. At the 5% significance level, reject $H_0$ and conclude that the population means may differ.

</details>

### Applying the P-Value Rule

Another common approach is the **P-value approach**.

- The P-value is the smallest significance level at which the observed result would lead to rejection of $H_0$.
- It measures how incompatible the observed test statistic is with $H_0$.
- For a two-sided Z-test, equally extreme results in both tails are counted:

$$
\text{P-value}
=2P(Z>|z_0|)
$$

The decision rule is:

- Reject $H_0$ when $\text{P-value}\leq\alpha$.
- Fail to reject $H_0$ when $\text{P-value}>\alpha$.

> **Interpretation caution:** A P-value is not the probability that $H_0$ is true. It is the probability, assuming $H_0$ is true, of observing a test statistic at least as extreme as the one calculated.

<details>
<summary>Example: Portland cement Z-test P-value</summary>

For $z_0=-2.09$, use $|z_0|=2.09$. The standard normal table gives:

$$
P(Z\leq2.09)=\Phi(2.09)=0.98169
$$

Therefore, the two-sided P-value is:

$$
\begin{aligned}
\text{P-value}
&=2P(Z>2.09)\\
&=2(1-0.98169)\\
&=0.03662
\end{aligned}
$$

Since $0.03662<0.05$, reject $H_0$. The data provide evidence that the two mortar formulations have different mean tension bond strengths. The result would not be significant at the stricter $\alpha=0.01$ level.

</details>

## From the Z-Test to the Two-Sample t-Test

The known-variance Z-test works directly when the population variances $\sigma_1^2$ and $\sigma_2^2$ are known. In practice, they usually are not known.

### Large-Sample Approximation

One possibility is to replace the unknown population variances with the sample variances:

$$
z_0\approx
\frac{\bar{y}_1-\bar{y}_2}
{\sqrt{s_1^2/n_1+s_2^2/n_2}}
$$

This normal approximation generally works reasonably well when both sample sizes are large, commonly at least 30 and sometimes conservatively taken as 40.

For small samples, however, estimating the population variances adds uncertainty. The standard normal distribution is no longer the appropriate reference distribution. This is the problem addressed by Student's t-distribution.

### Equal-Variance Assumption

For the pooled two-sample t-test, assume:

- The two samples are independent random samples.
- Each population is normally distributed.
- The two population variances are unknown but equal:

$$
\sigma_1^2=\sigma_2^2=\sigma^2
$$

Because the variances are assumed equal, the two sample variances can be combined into one estimate.

### Pooled Estimate of Variance

The pooled variance is a degrees-of-freedom-weighted average of the two sample variances:

$$
s_p^2=
\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}
{n_1+n_2-2}
$$

Its positive square root, $s_p$, is the pooled standard deviation.

### Pooled Two-Sample t-Statistic

Substituting the pooled standard deviation into the standardized difference gives:

$$
t_0=
\frac{\bar{y}_1-\bar{y}_2}
{s_p\sqrt{1/n_1+1/n_2}}
$$

When $H_0:\mu_1=\mu_2$ is true, this statistic follows a t-distribution with:

$$
\nu=n_1+n_2-2
$$

degrees of freedom.

Like $z_0$, the statistic $t_0$ is a distance measure:

- Values near zero are consistent with $H_0$.
- Values far from zero support $H_1$.
- The statistic measures the difference between the sample means in estimated standard-error units.

It can also be interpreted as a signal-to-noise ratio:

$$
t_0=
\frac{\text{signal: difference in sample means}}
{\text{noise: estimated standard error of the difference}}
$$

### Reference Distribution and Decision Rules

The t-distribution is symmetric around zero, like the standard normal distribution, but has heavier tails. Its shape depends on the degrees of freedom, and its heavier tails account for the uncertainty introduced by estimating variance from small samples.

For a two-sided pooled t-test, the critical-value rule is:

$$
\text{Reject }H_0
\quad\text{when}\quad
|t_0|>t_{\alpha/2,\,n_1+n_2-2}
$$

The equivalent two-sided P-value is:

$$
\text{P-value}
=P\left(|T_\nu|\geq|t_0|\right)
=2P\left(T_\nu\geq|t_0|\right)
$$

Reject $H_0$ when $\text{P-value}\leq\alpha$. A t-table can bracket the P-value between listed tail probabilities, while statistical software provides a more precise value.

<details>
<summary>Example: Portland cement pooled t-test</summary>

For the two mortar samples:

$$
n_1=n_2=10,
\qquad
s_p^2=0.081,
\qquad
s_p=0.284
$$

Substitution into the pooled t-statistic gives:

$$
t_0=-2.20,
\qquad
\nu=n_1+n_2-2=18
$$

For a two-sided test with $\alpha=0.05$, the critical value is:

$$
t_{0.025,18}=2.101
$$

Because $|t_0|=2.20>2.101$, reject $H_0$. There is statistically significant evidence of a difference between the two population means.

The two-sided P-value is:

$$
\text{P-value}
=P\left(|T_{18}|\geq2.20\right)
\approx0.042
$$

This is significant at the 5% level, but not at the stricter 1% level. A t-table brackets the result as follows:

$$
t_{0.025,18}=2.101<2.20<2.552=t_{0.01,18}
$$

so:

$$
0.02<\text{P-value}<0.05
$$

#### Computer output

Minitab defines the difference as $\mu_{\text{modified}}-\mu_{\text{unmodified}}$ and reports:

- Modified mortar: $n_1=10$, $\bar{y}_1=16.764$, $s_1=0.316$, and $SE(\bar{y}_1)=0.100$.
- Unmodified mortar: $n_2=10$, $\bar{y}_2=17.042$, $s_2=0.248$, and $SE(\bar{y}_2)=0.078$.
- Estimated difference: $-0.278$.
- Pooled standard deviation: $s_p=0.2843$.
- Test statistic: $t_0=-2.19$ with $18$ degrees of freedom.
- Two-sided P-value: $0.042$.
- 95% confidence interval: $(-0.545073,-0.010927)$.

JMP reverses the subtraction, so it reports an estimated difference of $0.278$, a t-ratio of $2.186876$, and the sign-reversed interval $(0.010927,0.545073)$. Reversing the subtraction changes the signs but not the absolute t-value, two-sided P-value, or conclusion.

</details>

## Checking the Pooled t-Test Assumptions

The pooled two-sample t-test assumes:

- The observations are independent.
- Each population is approximately normal.
- The two populations have equal variances.

### Normal Probability Plots

A normal probability plot can be drawn for each sample.

- Data that lie approximately along a straight line provide reasonable evidence for normality.
- The slope of a fitted line on a normal probability plot is proportional to the sample standard deviation.
- Similar slopes for the two samples support the equal-variance assumption.
- When judging straightness and slope by eye, emphasize the central part of the plot. A few tail observations can vary substantially in small samples.

<details>
<summary>Example: Checking the Portland cement assumptions</summary>

Both Portland cement samples follow approximately straight lines on their normal probability plots, so the normality assumption appears reasonable. Their slopes are also similar, supporting the equal-variance assumption.

</details>

### Importance of the Assumptions

The t-test is fairly robust to moderate departures from normality. It generally performs well when the population distributions are reasonably symmetric and unimodal.

The equal-variance assumption is more important for the pooled test. Substantially unequal variances can reduce the test's sensitivity and affect its error rate. When equal variances are doubtful, Welch's two-sample t-test is generally the appropriate alternative because it does not pool the variances.

## Why the t-Test Is Useful

For a simple comparative experiment, the t-test provides an objective rule for deciding whether an observed difference is larger than would reasonably be expected from random variation alone.

The method is versatile. For example, the effects in a two-level factorial design can be viewed as comparisons between mean responses on opposite sides of the experimental cube. Later procedures analyze all such effects more efficiently than running a separate t-test for each comparison.

A hypothesis test answers whether there is evidence of a difference, but it does not describe the likely size of that difference. A confidence interval supplies that additional information.

## Confidence Intervals

A confidence interval for a parameter $\theta$ has lower and upper limits $L$ and $U$:

$$
L\leq\theta\leq U
$$

The confidence procedure is constructed to have coverage probability:

$$
P(L\leq\theta\leq U)=1-\alpha
$$

Thus, a $100(1-\alpha)\%$ confidence procedure produces intervals that contain the true parameter in $100(1-\alpha)\%$ of repeated samples.

> For one interval already calculated, the parameter is fixed and the endpoints are random. A 95% confidence level describes the long-run success rate of the method, not a 95% posterior probability that this particular interval contains the parameter.

### Confidence Interval for the Difference in Two Means

Under the same assumptions as the pooled t-test, the $100(1-\alpha)\%$ confidence interval for $\mu_1-\mu_2$ is:

$$
(\bar{y}_1-\bar{y}_2)
\pm
t_{\alpha/2,n_1+n_2-2}
s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}
$$

Equivalently, the lower confidence limit is:

$$
L=(\bar{y}_1-\bar{y}_2)
-t_{\alpha/2,n_1+n_2-2}
s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}
$$

and the upper confidence limit is:

$$
U=(\bar{y}_1-\bar{y}_2)
+t_{\alpha/2,n_1+n_2-2}
s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}
$$

This has the familiar form:

$$
\text{point estimate}\pm\text{margin of error}
$$

where:

$$
\text{margin of error}
=t_{\alpha/2,n_1+n_2-2}
s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}
$$

<details>
<summary>Example: Portland cement 95% confidence interval</summary>

Define the difference in the same order as Minitab:

$$
\mu_1-\mu_2
=\mu_{\text{modified}}-\mu_{\text{unmodified}}
$$

The required values are:

- $\bar{y}_1-\bar{y}_2=16.764-17.042=-0.278$.
- $s_p=0.2843$.
- $n_1=n_2=10$.
- $\nu=18$.
- $t_{0.025,18}=2.101$ for 95% confidence.

The estimated standard error is:

$$
SE(\bar{y}_1-\bar{y}_2)
=0.2843\sqrt{\frac{1}{10}+\frac{1}{10}}
\approx0.1271
$$

The margin of error is:

$$
2.101(0.1271)\approx0.267\approx0.27
$$

Therefore:

$$
\mu_1-\mu_2
=-0.278\pm0.267
$$

Using the full-precision software values gives:

$$
-0.545073
\leq
\mu_1-\mu_2
\leq
-0.010927
$$

Rounded as in the lecture and textbook:

$$
-0.55
\leq
\mu_1-\mu_2
\leq
-0.01
\quad\text{kgf/cm}^2
$$

#### Interpretation

- The entire interval is negative because the modified-minus-unmodified mean difference is negative.
- The data estimate that modified mortar has a mean tension bond strength between $0.01$ and $0.55\ \text{kgf/cm}^2$ lower than unmodified mortar.
- Equivalently, unmodified mortar has a mean strength between $0.01$ and $0.55\ \text{kgf/cm}^2$ higher than modified mortar.
- The point estimate of the difference is $-0.278\ \text{kgf/cm}^2$, with a margin of error of approximately $0.27\ \text{kgf/cm}^2$.

#### Connection with the hypothesis test

For the two-sided test:

$$
H_0:\mu_1-\mu_2=0
$$

At matching levels, a two-sided hypothesis test with significance $\alpha$ and a $100(1-\alpha)\%$ confidence interval give equivalent decisions:

- If the confidence interval excludes zero, reject $H_0$.
- If the confidence interval includes zero, fail to reject $H_0$.

Here, the 95% confidence interval $(-0.545073,-0.010927)$ excludes zero. This agrees with the two-sided t-test result, $P\approx0.042<0.05$, so $H_0$ is rejected.

</details>

## When the Two Population Variances Differ

The pooled two-sample t-test assumes that the two unknown population variances are equal. When the sample spreads are substantially different, pooling them into one variance estimate is not appropriate.

The usual alternative is **Welch's two-sample t-test**. Welch's test keeps the two sample variances separate and adjusts the reference distribution's degrees of freedom.

It assumes:

- The two samples are independent random samples.
- Observations within each sample are independent.
- Each population is approximately normal, particularly when the samples are small.
- The population variances do **not** have to be equal.

### Welch Test Statistic

For a hypothesized difference $\Delta_0$, test:

$$
H_0:\mu_1-\mu_2=\Delta_0
$$

with the statistic:

$$
t_0=
\frac{(\bar{y}_1-\bar{y}_2)-\Delta_0}
{\sqrt{s_1^2/n_1+s_2^2/n_2}}
$$

For the usual null hypothesis of equal means, $\Delta_0=0$:

$$
t_0=
\frac{\bar{y}_1-\bar{y}_2}
{\sqrt{s_1^2/n_1+s_2^2/n_2}}
$$

Unlike the pooled statistic, this statistic does not have an exact t-distribution. Its distribution is well approximated by a t-distribution using the **Welch-Satterthwaite degrees of freedom**:

$$
\nu=
\frac{
\left(\dfrac{s_1^2}{n_1}+\dfrac{s_2^2}{n_2}\right)^2
}
{
\dfrac{(s_1^2/n_1)^2}{n_1-1}
+
\dfrac{(s_2^2/n_2)^2}{n_2-1}
}
$$

Software normally uses the fractional value of $\nu$. When only an integer-row t-table is available, rounding $\nu$ down is a conservative approximation.

### Confidence Interval With Unequal Variances

The $100(1-\alpha)\%$ two-sided confidence interval for $\mu_1-\mu_2$ is:

$$
(\bar{y}_1-\bar{y}_2)
\pm
t_{\alpha/2,\nu}
\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}
$$

The same Welch standard error and adjusted degrees of freedom are used for both the hypothesis test and the interval.

<details>
<summary>Example: Nerve and muscle fluorescence with Welch's t-test</summary>

Accidental nerve injury during surgery can cause pain, numbness, or paralysis. The study described in the lecture used a fluorescently labeled peptide that binds to nerves, potentially making nerves easier for surgeons to identify.

Normalized fluorescence after two hours was recorded for nerve and muscle tissue. The lecture data, read from a graph in the original paper, are:

| Observation | Nerve | Muscle |
| ---: | ---: | ---: |
| 1 | 6625 | 3900 |
| 2 | 6000 | 3500 |
| 3 | 5450 | 3450 |
| 4 | 5200 | 3200 |
| 5 | 5175 | 2980 |
| 6 | 4900 | 2800 |
| 7 | 4750 | 2500 |
| 8 | 4500 | 2400 |
| 9 | 3985 | 2200 |
| 10 | 900 | 1200 |
| 11 | 450 | 1150 |
| 12 | 2800 | 1130 |

The sample summaries are:

| Tissue | $n$ | Mean | Standard deviation | Minimum | Median | Maximum |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Nerve | 12 | 4228 | 1918 | 450 | 4825 | 6625 |
| Muscle/non-nerve | 12 | 2534 | 961 | 1130 | 2650 | 3900 |

The sample standard deviation for nerve tissue is about twice the muscle standard deviation:

$$
\frac{s_{\text{nerve}}}{s_{\text{muscle}}}
=\frac{1918}{961}
\approx2.00
$$

The normal probability plots are approximately linear, so normality is not the main concern. Their very different slopes indicate very different standard deviations, making the pooled t-test unsuitable.

![Nerve and muscle fluorescence data, normal probability comparison, and Welch test result](images/nerve_muscle_welch_test.png)

#### Hypotheses

Let $\mu_1$ be mean normalized fluorescence for nerve tissue and $\mu_2$ be the mean for muscle tissue. The research question is one-sided:

$$
H_0:\mu_1=\mu_2
$$

$$
H_1:\mu_1>\mu_2
$$

#### Welch test calculation

The estimated mean difference is:

$$
\bar{y}_1-\bar{y}_2=4228-2534=1694
$$

The estimated standard error is:

$$
SE=
\sqrt{\frac{1918^2}{12}+\frac{961^2}{12}}
=619.29
$$

Therefore:

$$
t_0=
\frac{4228-2534}
{\sqrt{1918^2/12+961^2/12}}
=2.7354
$$

The Welch-Satterthwaite degrees of freedom are:

$$
\nu=
\frac{
\left(1918^2/12+961^2/12\right)^2
}
{
\dfrac{(1918^2/12)^2}{11}
+
\dfrac{(961^2/12)^2}{11}
}
=16.1955
$$

For hand calculation with a t-table, use $\nu=16$. The software output reports:

- Estimated difference: $1694$.
- Test statistic: $t_0\approx2.74$.
- Degrees of freedom: approximately $16$.
- One-sided P-value: $0.007$.
- 95% lower confidence bound for $\mu_1-\mu_2$: approximately $613$.

Because $0.007<0.05$, reject $H_0$. There is strong evidence that mean normalized fluorescence is greater for nerve tissue than for muscle tissue.

</details>

## Inference on a Single Mean

Some experiments compare one population mean $\mu$ with a specified or target value $\mu_0$. The target may come from previous evidence, a scientific model, an engineering specification, or a contract.

For a two-sided question, the hypotheses are:

$$
H_0:\mu=\mu_0
$$

$$
H_1:\mu\ne\mu_0
$$

The procedure depends on whether the population standard deviation $\sigma$ is known.

| Population variance | Test | Statistic | Reference distribution |
| --- | --- | --- | --- |
| $\sigma^2$ known | One-sample Z-test | $z_0=(\bar{y}-\mu_0)/(\sigma/\sqrt{n})$ | Standard normal $N(0,1)$ |
| $\sigma^2$ unknown | One-sample t-test | $t_0=(\bar{y}-\mu_0)/(s/\sqrt{n})$ | t-distribution with $n-1$ degrees of freedom |

### One-Sample Z-Test: Variance Known

When $\sigma$ is known:

$$
z_0=
\frac{\bar{y}-\mu_0}{\sigma/\sqrt{n}}
$$

If $H_0$ is true, then $Z_0\sim N(0,1)$. For a two-sided alternative, reject $H_0$ when:

$$
|z_0|>z_{\alpha/2}
$$

The $100(1-\alpha)\%$ confidence interval for $\mu$ is:

$$
\bar{y}
-z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
\leq\mu\leq
\bar{y}
+z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

or, more compactly:

$$
\bar{y}\pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

<details>
<summary>Example: Fabric breaking strength with a one-sample Z-test</summary>

A textile manufacturer will accept a fabric lot only if there is evidence that its mean breaking strength exceeds $200$ psi. Past experience supports a known population variance of:

$$
\sigma^2=100\ \text{psi}^2
$$

so:

$$
\sigma=10\ \text{psi}
$$

The upper-tail hypotheses are:

$$
H_0:\mu=200
$$

$$
H_1:\mu>200
$$

Four randomly selected specimens give:

$$
n=4,
\qquad
\bar{y}=214\ \text{psi}
$$

The Z statistic is:

$$
z_0=
\frac{214-200}{10/\sqrt{4}}
=\frac{14}{5}
=2.80
$$

![Known-variance and unknown-variance single-mean tests, with the fabric Z-test](images/single_mean_inference.png)

For an upper-tail test with $\alpha=0.05$:

$$
z_{0.05}=1.645
$$

Since:

$$
2.80>1.645
$$

the observed statistic is in the rejection region. The one-sided P-value is:

$$
P(Z\geq2.80)
=1-\Phi(2.80)
=1-0.99744
=0.00256
$$

Do not double this probability because the alternative hypothesis is one-sided. Since $0.00256<0.05$, reject $H_0$ and conclude that the data provide strong evidence that the lot's mean breaking strength exceeds $200$ psi.

</details>

### One-Sample t-Test: Variance Unknown

When the population variance is unknown, replace $\sigma$ with the sample standard deviation $s$:

$$
t_0=
\frac{\bar{y}-\mu_0}{s/\sqrt{n}}
$$

Under $H_0$, this statistic follows a t-distribution with:

$$
\nu=n-1
$$

degrees of freedom. For a two-sided alternative, reject $H_0$ when:

$$
|t_0|>t_{\alpha/2,n-1}
$$

The corresponding $100(1-\alpha)\%$ confidence interval is:

$$
\bar{y}
-t_{\alpha/2,n-1}\frac{s}{\sqrt{n}}
\leq\mu\leq
\bar{y}
+t_{\alpha/2,n-1}\frac{s}{\sqrt{n}}
$$

or:

$$
\bar{y}\pm t_{\alpha/2,n-1}\frac{s}{\sqrt{n}}
$$

For a small sample, this procedure assumes that the population is approximately normal. Moderate departures from normality usually do not seriously affect the result, but strong skewness or outliers require care.

## Paired Experiments and the Paired t-Test

The independent two-sample procedures above are appropriate when the observations in one group have no natural connection to observations in the other group. Some two-treatment experiments have a different structure: the two measurements are made on the **same experimental unit**, or units in the two groups are deliberately matched. These observations form pairs.

Examples include:

- Before-and-after measurements on the same person.
- Two instruments used on the same specimen.
- Two treatments applied to different portions of the same batch or material sample.
- Subjects matched by age, baseline condition, or another important characteristic.

Pairing can remove variability caused by differences among experimental units. The analysis therefore focuses on the **within-pair differences**, rather than treating the two sets of measurements as independent samples.

<details>
<summary>Example: Hardness-testing experiment and paired design</summary>

A Rockwell-type hardness tester presses a pointed tip into a metal specimen under a known force. The resulting indentation is used to determine relative hardness. The machine has two tips, and the experiment asks whether the tips produce different mean hardness readings.

One possible design would randomly assign 10 of 20 specimens to Tip 1 and the other 10 to Tip 2. This is a completely randomized, independent-samples design. However, specimens cut from different pieces of bar stock or produced in different heats may have different hardness. That specimen-to-specimen variation would enter the experimental error and could hide a real tip effect.

A paired design provides better control of this nuisance variation:

1. Select 10 specimens, each large enough for two hardness measurements.
2. Divide each specimen into two comparable portions.
3. Apply Tip 1 to one portion and Tip 2 to the other.
4. Randomize which portion receives each tip and randomize the testing order.

Each specimen is now a **block**, and the two tip readings within that specimen form a pair.

#### Observed paired data

Define the difference consistently as:

$$
d_j=y_{1j}-y_{2j}
$$

where $y_{1j}$ and $y_{2j}$ are the Tip 1 and Tip 2 readings on specimen $j$.

| Specimen $j$ | Tip 1, $y_{1j}$ | Tip 2, $y_{2j}$ | Difference, $d_j=y_{1j}-y_{2j}$ |
| ---: | ---: | ---: | ---: |
| 1 | 7 | 6 | 1 |
| 2 | 3 | 3 | 0 |
| 3 | 3 | 5 | -2 |
| 4 | 4 | 3 | 1 |
| 5 | 8 | 8 | 0 |
| 6 | 3 | 2 | 1 |
| 7 | 2 | 4 | -2 |
| 8 | 9 | 9 | 0 |
| 9 | 5 | 4 | 1 |
| 10 | 4 | 5 | -1 |
| **Total** | **48** | **49** | **-1** |
| **Mean** | **4.80** | **4.90** | **-0.10** |

The signs depend on the chosen subtraction order. Had the differences been defined as Tip 2 minus Tip 1, the estimate and test statistic would change sign, but a two-sided P-value and the final decision would not change.

</details>

### Statistical Model and the Blocking Effect

A model for the response is:

$$
y_{ij}=\mu_i+\beta_j+\varepsilon_{ij},
\qquad
i=1,2,
\quad
j=1,2,\ldots,n
$$

where:

- $\mu_i$ is the mean response associated with treatment $i$.
- $\beta_j$ is the effect of block $j$.
- $\varepsilon_{ij}$ is random measurement error, assumed independent with mean zero and common variance $\sigma^2$ in this model.

For the $j$th pair:

$$
d_j=y_{1j}-y_{2j}
$$

Taking its expected value gives:

$$
\begin{aligned}
\mu_d
=E(d_j)
&=E(y_{1j}-y_{2j})\\
&=E(y_{1j})-E(y_{2j})\\
&=(\mu_1+\beta_j)-(\mu_2+\beta_j)\\
&=\mu_1-\mu_2
\end{aligned}
$$

The block effect $\beta_j$ cancels because both treatments are compared within the same block. Consequently, inference about $\mu_1-\mu_2$ can be based on the population mean of the differences, $\mu_d$.

This is the central benefit of pairing: comparison is made **within homogeneous blocks**, so variation between blocks does not obscure the treatment comparison.

### Hypotheses

Testing whether the two treatments have the same mean is equivalent to testing whether the mean paired difference is zero:

$$
H_0:\mu_1=\mu_2
\quad\Longleftrightarrow\quad
H_0:\mu_d=0
$$

For a two-sided comparison:

$$
H_0:\mu_d=0
$$

$$
H_1:\mu_d\ne0
$$

More generally, a paired test may compare the mean difference with a nonzero reference value $\Delta_0$:

$$
H_0:\mu_d=\Delta_0
$$

### Paired t-Test Statistic

Once the differences have been calculated, the paired t-test is simply a **one-sample t-test applied to the $n$ differences**.

Their sample mean is:

$$
\bar{d}=\frac{1}{n}\sum_{j=1}^{n}d_j
$$

Their sample standard deviation is:

$$
S_d=
\sqrt{
\frac{\sum_{j=1}^{n}(d_j-\bar{d})^2}{n-1}
}
$$

An equivalent computational form is:

$$
S_d=
\sqrt{
\frac{
\displaystyle\sum_{j=1}^{n}d_j^2
-\dfrac{1}{n}\left(\displaystyle\sum_{j=1}^{n}d_j\right)^2
}{n-1}
}
$$

For $H_0:\mu_d=\Delta_0$, the test statistic is:

$$
t_0=
\frac{\bar{d}-\Delta_0}{S_d/\sqrt{n}}
$$

If the differences are normally distributed and $H_0$ is true, then $t_0$ follows a t-distribution with:

$$
\nu=n-1
$$

degrees of freedom. For the usual two-sided test at significance level $\alpha$, reject $H_0$ when:

$$
|t_0|>t_{\alpha/2,n-1}
$$

Equivalently, reject when the two-sided P-value is less than $\alpha$.

### Confidence Interval for the Mean Paired Difference

The $100(1-\alpha)\%$ confidence interval for $\mu_d=\mu_1-\mu_2$ is:

$$
\bar d
\pm
t_{\alpha/2,n-1}\frac{S_d}{\sqrt n}
$$

<details>
<summary>Example: Hardness-test calculation and confidence interval</summary>

#### Hypothesis test

For the 10 observed differences:

$$
\sum_{j=1}^{10}d_j=-1,
\qquad
\sum_{j=1}^{10}d_j^2=13
$$

Therefore:

$$
\bar{d}
=\frac{1}{10}\sum_{j=1}^{10}d_j
=\frac{-1}{10}
=-0.10
$$

and:

$$
\begin{aligned}
S_d
&=
\sqrt{
\frac{
13-\dfrac{1}{10}(-1)^2
}{10-1}
}\\
&=1.1972
\approx1.20
\end{aligned}
$$

The estimated standard error of $\bar d$ is:

$$
SE(\bar d)=\frac{S_d}{\sqrt n}
=\frac{1.1972}{\sqrt{10}}
=0.3786
$$

For $H_0:\mu_d=0$:

$$
t_0=
\frac{-0.10}{1.1972/\sqrt{10}}
=-0.264
\approx-0.26
$$

There are $10-1=9$ degrees of freedom. For a two-sided test with $\alpha=0.05$:

$$
t_{0.025,9}=2.262
$$

Since:

$$
|t_0|=0.264<2.262
$$

the statistic is not in the rejection region. The two-sided P-value is approximately $0.798$, which is also much larger than $0.05$. Therefore, **fail to reject $H_0$**. The experiment provides no statistically significant evidence that the two tips have different mean hardness readings.

Failing to reject $H_0$ does not prove that the tips are identical. It means that differences still compatible with the data cannot be ruled out. A confidence interval describes those plausible differences.

#### Confidence interval

For the hardness data, the 95% interval is:

$$
\begin{aligned}
-0.10
&\pm
(2.262)\frac{1.1972}{\sqrt{10}}\\
&=-0.10\pm0.856\\
&\approx-0.10\pm0.86
\end{aligned}
$$

Thus:

$$
-0.956\leq\mu_1-\mu_2\leq0.756
$$

or, after rounding to two decimal places:

$$
(-0.96,\ 0.76)
$$

The interval includes zero, agreeing with the hypothesis-test decision. Here $0.86$ is the **margin of error**, or interval half-width; the total interval width is approximately $1.72$.

</details>

## Why Pairing Can Increase Precision

Pairing can reduce the standard error by removing nuisance variation between matched units or blocks. Its benefit is greatest when measurements within a pair are strongly and positively related.

<details>
<summary>Example: Precision gained by pairing the hardness data</summary>

To see what is gained by pairing, suppose the same observations were incorrectly analyzed as two independent samples with equal variances. The sample means would still be:

$$
\bar y_1=4.80,
\qquad
\bar y_2=4.90,
\qquad
\bar y_1-\bar y_2=-0.10
$$

The separate sample variances and pooled standard deviation are approximately:

$$
s_1^2=5.733,
\qquad
s_2^2=4.989
$$

$$
S_p=
\sqrt{
\frac{(10-1)s_1^2+(10-1)s_2^2}{10+10-2}
}
=2.315
\approx2.32
$$

The independent-samples 95% confidence interval would be:

$$
(\bar y_1-\bar y_2)
\pm
t_{0.025,18}S_p
\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}
$$

$$
\begin{aligned}
-0.10
&\pm
(2.101)(2.315)
\sqrt{\frac{1}{10}+\frac{1}{10}}\\
&=-0.10\pm2.18\\
&=(-2.28,\ 2.08)
\end{aligned}
$$

The point estimate remains $-0.10$, but the independent interval's margin of error is $2.18$, compared with only $0.86$ for the paired interval. It is approximately:

$$
\frac{2.18}{0.86}\approx2.5
$$

times as large.

| Analysis | Standard deviation used | Degrees of freedom | 95% interval | Margin of error |
| --- | ---: | ---: | ---: | ---: |
| Paired | $S_d\approx1.20$ | 9 | $(-0.96,0.76)$ | $0.86$ |
| Treating readings as independent | $S_p\approx2.32$ | 18 | $(-2.28,2.08)$ | $2.18$ |

The apparently larger number of degrees of freedom in the independent analysis does not compensate for its inflated variance estimate.

</details>

### Variance Explanation

Under the paired model, block effects contribute to the variation of readings across blocks. If the block effects are treated as fixed and centered around their mean, the expected pooled variance from an independent-samples analysis contains both measurement error and block variation:

$$
E(S_p^2)
=
\sigma^2
+
\frac{1}{n-1}
\sum_{j=1}^{n}(\beta_j-\bar\beta)^2
$$

With the common constraint $\bar\beta=0$, this becomes:

$$
E(S_p^2)
=
\sigma^2
+
\frac{1}{n-1}
\sum_{j=1}^{n}\beta_j^2
$$

The second term is nuisance variation among blocks. It inflates the error estimate when the blocking is ignored. In the paired differences, the block effect cancels, leaving the comparison to depend only on within-block variation. This is why blocking is called a **noise-reduction design technique**.

Another way to express the same idea is through within-pair correlation. If the two measurements have standard deviations $\sigma_1$ and $\sigma_2$ and correlation $\rho$, then:

```math
\mathrm{Var}(Y_1 - Y_2)
=
\sigma_1^2 + \sigma_2^2 - 2\rho\sigma_1\sigma_2
```

Good matching usually creates positive correlation, so the last term reduces the variance of the differences. Pairing provides little benefit when the match is weak and may be inefficient when the within-pair correlation is negative.

### Assumptions of the Paired t-Test

The paired t-test assumes:

- The data genuinely form meaningful pairs established by the design, not pairs created after examining the responses.
- Different pairs are independent of one another.
- The paired differences are a random sample from the population of relevant differences.
- The response is quantitative and the differences are approximately normally distributed when $n$ is small.
- The differences contain no severe outliers that dominate $\bar d$ and $S_d$.

Normality concerns the distribution of the **differences**, not the two sets of raw measurements separately. With a larger number of pairs, the procedure is reasonably robust to moderate nonnormality, but severe skewness and influential outliers still require investigation.

If normality of the differences is doubtful, useful alternatives may include a paired randomization test or the Wilcoxon signed-rank test, provided the assumptions of the selected alternative are appropriate.
