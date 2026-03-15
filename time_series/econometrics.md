# 1. Simple Returns

## Simple Gross Return

$$
1 + R_t = \frac{P_t}{P_{t-1}}
$$

- \(P_t\): price at time \(t\)
- \(P_{t-1}\): price at time \(t-1\)

Interpretation:  
Final price divided by initial price.

---

## Simple Net Return

$$
R_t = \frac{P_t - P_{t-1}}{P_{t-1}}
$$

Interpretation:  
Percentage price change over one period.

---

# 2. Multiperiod Simple Returns

## Compound Return

$$
1 + R_t[k] =
(1 + R_t)(1 + R_{t-1}) \cdots (1 + R_{t-k+1})
$$

Interpretation:  
Simple returns **multiply across time**.

---

# 3. Annualized Return

## Exact Formula (Geometric Mean)

$$
\text{Annualized} =
\left(\prod_{j=0}^{k-1}(1+R_{t-j})\right)^{1/k} - 1
$$

---

## Approximation (Small Returns)

$$
\text{Annualized} \approx
\frac{1}{k} \sum_{j=0}^{k-1} R_{t-j}
$$

Interpretation:  
When returns are small, the geometric mean can be approximated by the arithmetic mean.

---

# 4. Log (Continuously Compounded) Returns

## Definition

$$
r_t = \ln(1 + R_t)
$$

Equivalent form:

$$
r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$

Log-price form:

$$
r_t = p_t - p_{t-1}
$$

where

$$
p_t = \ln(P_t)
$$

---

## Convert Log Return to Simple Return

$$
R_t = e^{r_t} - 1
$$

---

# 5. Multiperiod Log Returns

$$
r_t[k] =
r_t + r_{t-1} + \cdots + r_{t-k+1}
$$

Interpretation:  
Log returns **add across time**.

---

# 6. Continuous Compounding

## Future Value

$$
A = C e^{rn}
$$

## Present Value

$$
C = A e^{-rn}
$$

Where:

- \(C\) = initial capital
- \(A\) = future value
- \(r\) = interest rate
- \(n\) = number of years

---

# 7. Portfolio Returns

## Simple Portfolio Return

$$
R_{p,t} =
\sum_{i=1}^{N} w_i R_{i,t}
$$

Where:

- \(w_i\): weight of asset \(i\)
- \(R_{i,t}\): return of asset \(i\)

Interpretation:  
Portfolio return is the **weighted average of asset returns**.

---

## Log Portfolio Return (Approximation)

$$
r_{p,t} \approx
\sum_{i=1}^{N} w_i r_{i,t}
$$

Valid when returns are small.

---

# 8. Returns with Dividends

## Simple Return with Dividends

$$
R_t =
\frac{P_t + D_t}{P_{t-1}} - 1
$$

Where:

- \(D_t\) = dividend payment

---

## Log Return with Dividends

$$
r_t =
\ln(P_t + D_t) - \ln(P_{t-1})
$$

Interpretation:  
Dividends must be included because they are part of the investor's total gain.

---

# 9. Excess Return

## Simple Excess Return

$$
Z_t = R_t - R_{0t}
$$

## Log Excess Return

$$
z_t = r_t - r_{0t}
$$

Where:

- \(R_{0t}\) = reference asset return (often risk-free rate)

Interpretation:  
Excess return measures how much an asset outperforms the reference asset.

---

# Key Rules to Remember

| Concept | Property |
|------|------|
| Simple returns | Multiply across time |
| Log returns | Add across time |
| Continuous compounding | Uses exponential growth |
| Portfolio simple return | Weighted average of asset returns |
| Excess return | Asset return minus risk-free return |
