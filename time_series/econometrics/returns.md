# Simple Returns

**Simple Gross Return**: Final price divided by initial price.

$$
1 + R_t = \frac{P_t}{P_{t-1}}
$$


**Simple Net Return**: Percentage price change over one period.

$$
R_t = \frac{P_t - P_{t-1}}{P_{t-1}}
$$


# Multiperiod Simple Returns

**Compound Return**: Simple returns multiply across time.

$$
1 + R_t[k] =
(1 + R_t)(1 + R_{t-1}) \cdots (1 + R_{t-k+1})
$$

# Annualized Return

**Exact Formula (Geometric Mean):

$$
\text{Annualized} =
\left(\prod_{j=0}^{k-1}(1+R_{t-j})\right)^{1/k} - 1
$$

**Approximation (Small Returns)**:

$$
\text{Annualized} \approx
\frac{1}{k} \sum_{j=0}^{k-1} R_{t-j}
$$


# Log (Continuously Compounded) Returns

$$
r_t = \ln(1 + R_t) = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$

Log-price form:

$$
r_t = p_t - p_{t-1}
$$

where

$$
p_t = \ln(P_t)
$$


Note:

$$
R_t = e^{r_t} - 1
$$

# Multiperiod Log Returns

Log returns add across time.

$$
r_t[k] =
r_t + r_{t-1} + \cdots + r_{t-k+1}
$$


# Continuous Compounding

Future Value:

$$
A = C e^{rn}
$$

Present Value:

$$
C = A e^{-rn}
$$

Where:

- $C$ = initial capital
- $A$ = future value
- $r$ = interest rate
- $n$ = number of years

# Portfolio Returns

**Simple Portfolio Return**: the weighted average of asset returns.

$$
R_{p,t} =
\sum_{i=1}^{N} w_i R_{i,t}
$$

Where: $w_i$: weight of asset $i$ with return of asset $R_{i,t}$.


**Log Portfolio Return (Approximation)**

Valid when returns are small.

$$
r_{p,t} \approx
\sum_{i=1}^{N} w_i r_{i,t}
$$

# 8. Returns with Dividends
Dividends must be included because they are part of the investor's total gain.

**Simple Return with Dividends**:

$$
R_t =
\frac{P_t + D_t}{P_{t-1}} - 1
$$

Where: $D_t$ = dividend payment

**Log Return with Dividends**:

$$
r_t =
\ln(P_t + D_t) - \ln(P_{t-1})
$$

# Excess Return:

**Simple Excess Return**

$$
Z_t = R_t - R_{0t}
$$

**Log Excess Return**

It measures how much an asset outperforms the reference asset.

$$
z_t = r_t - r_{0t}
$$

Where: $R_{0t}$ = reference asset return (often risk-free rate)

# Key Rules to Remember

| Concept | Property |
|------|------|
| Simple returns | Multiply across time |
| Log returns | Add across time |
| Continuous compounding | Uses exponential growth |
| Portfolio simple return | Weighted average of asset returns |
| Excess return | Asset return minus risk-free return |
