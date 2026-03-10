## Summary

| Concept | NumPy | PyTorch | TensorFlow | Keras | Notes |
|---|---|---|---|---|---|
| Imports | `import numpy as np` | `import torch` | `import tensorflow as tf` | `from keras import ops` | Used in examples |
| Dense coordinate grid | `np.meshgrid` | `torch.meshgrid` | `tf.meshgrid` | `ops.meshgrid` | Same concept everywhere |
| Indexing modes | `"xy", "ij"` | `"xy", "ij"` | `"xy", "ij"` | `"xy", "ij"` | `"ij"` recommended for scientific computing |
| Cartesian product (points list) | `itertools.product` / `stack(meshgrid).reshape(-1,k)` | `torch.cartesian_prod` | `reshape(stack(meshgrid), (-1,k))` | same as TF | Distinguish from grid-shaped output |
| Sparse grid | `meshgrid(..., sparse=True)` | broadcasting | broadcasting | broadcasting | Avoid full grids for large dimensions |
| Broadcast alternative | `np.ogrid` / reshape | reshape + broadcast | reshape + broadcast | reshape + broadcast | Often preferred |
| Dense grid generator | `np.mgrid` | — | — | — | NumPy convenience feature |
| Index grid | `np.indices` | `torch.arange + reshape` | `tf.range + reshape` | same as TF | Used for tensor coordinates |
| Flatten grid to points | `stack(...).reshape(-1,k)` | same | same | same | Convert grid → list of points |


# Dense coordinate grid

<details>
<summary>NumPy</summary>

Note: `indexing="ij"` is usually clearer for scientific computing because axis order matches array dimensions.

```python
x, y = np.meshgrid(np.arange(3), np.arange(4), indexing="ij")
````

Key result

```
x =
[[0 0 0 0]
 [1 1 1 1]
 [2 2 2 2]]

y =
[[0 1 2 3]
 [0 1 2 3]
 [0 1 2 3]]
```

shape → `(3,4)`

</details>

<details>
<summary>PyTorch</summary>

```python
x, y = torch.meshgrid(torch.arange(3), torch.arange(4), indexing="ij")
```

Key result

```
x.shape → torch.Size([3,4])
y.shape → torch.Size([3,4])
```

Same coordinate grid behavior as NumPy.

</details>

<details>
<summary>TensorFlow</summary>

```python
x, y = tf.meshgrid(tf.range(3), tf.range(4), indexing="ij")
```

Key result

```
x.shape → (3,4)
y.shape → (3,4)
```

</details>

<details>
<summary>Keras (v3 ops)</summary>

```python
x, y = ops.meshgrid(ops.arange(3), ops.arange(4), indexing="ij")
```

Key result

```
x.shape → (3,4)
y.shape → (3,4)
```

Backend-agnostic API.

</details>

# Cartesian product (points list)

<details>
<summary>NumPy / Python</summary>

```python
from itertools import product
list(product(range(3), range(4)))
```

Result

```
[(0,0),(0,1),(0,2),(0,3),
 (1,0),(1,1),(1,2),(1,3),
 (2,0),(2,1),(2,2),(2,3)]
```

shape → `(12 pairs)`

</details>

<details>
<summary>PyTorch</summary>

```python
torch.cartesian_prod(torch.arange(3), torch.arange(4))
```

Result

```
tensor([[0,0],
        [0,1],
        ...
        [2,3]])
```

shape → `(12,2)`

</details>

<details>
<summary>TensorFlow</summary>

For TensorFlow/Keras, `stack(meshgrid(...), axis=-1)` gives a **grid representation** with shape `(n1,...,nk,k)`, not yet a flat Cartesian-product list; use `reshape(-1, k)` for that.

```python
tf.reshape(
    tf.stack(tf.meshgrid(tf.range(3), tf.range(4), indexing="ij"), axis=-1),
    (-1, 2),
)
```

Result

```
shape → (12,2)
```

</details>

<details>
<summary>Keras</summary>

```python
ops.reshape(
    ops.stack(ops.meshgrid(ops.arange(3), ops.arange(4), indexing="ij"), axis=-1),
    (-1, 2),
)
```

Result

```
shape → (12,2)
```

</details>

# Sparse / memory-efficient grid

<details>
<summary>NumPy</summary>

```python
x, y = np.meshgrid(np.arange(3), np.arange(4), sparse=True)
```

Result

```
x.shape → (3,1)
y.shape → (1,4)
```

Broadcasted grid (memory efficient).

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.arange(3)[:, None]
y = torch.arange(4)[None, :]
z = x + y
```

Result

```
x.shape → (3,1)
y.shape → (1,4)
z.shape → (3,4)
```

Broadcast grid without meshgrid.

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.range(3)[:, None]
y = tf.range(4)[None, :]
z = x + y
```

Result

```
z.shape → (3,4)
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.arange(3)[:, None]
y = ops.arange(4)[None, :]
z = x + y
```

Result

```
z.shape → (3,4)
```

</details>


# Broadcast alternative (open grid)

Creates coordinate grids using **broadcasting instead of dense meshgrid**.

<details>
<summary>NumPy</summary>

```python
x, y = np.ogrid[0:3, 0:4]
z = x + y
````

Result

```
x.shape → (3,1)
y.shape → (1,4)
z.shape → (3,4)
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.arange(3)[:,None]
y = torch.arange(4)[None,:]
z = x + y
```

Result

```
x.shape → (3,1)
y.shape → (1,4)
z.shape → (3,4)
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.range(3)[:,None]
y = tf.range(4)[None,:]
z = x + y
```

Result

```
z.shape → (3,4)
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.arange(3)[:,None]
y = ops.arange(4)[None,:]
z = x + y
```

</details>

# Dense grid generator

<details>
<summary>NumPy</summary>

```python
np.mgrid[0:3, 0:4]
```

Result

```
array([[[0,0,0,0],
        [1,1,1,1],
        [2,2,2,2]],

       [[0,1,2,3],
        [0,1,2,3],
        [0,1,2,3]]])
```

Equivalent to `meshgrid(indexing="ij")`.

</details>

# Index grid

Creates tensors containing the **grid indices**.

<details>
<summary>NumPy</summary>

```python
np.indices((3,4))
````

Result

```
array([[[0,0,0,0],
        [1,1,1,1],
        [2,2,2,2]],

       [[0,1,2,3],
        [0,1,2,3],
        [0,1,2,3]]])
```

shape → `(2,3,4)`
first axis = coordinate dimension

</details>

<details>
<summary>PyTorch</summary>

```python
i = torch.arange(3)[:,None]
j = torch.arange(4)[None,:]

I = i.expand(3,4)
J = j.expand(3,4)
```

Result

```
I =
[[0,0,0,0],
 [1,1,1,1],
 [2,2,2,2]]

J =
[[0,1,2,3],
 [0,1,2,3],
 [0,1,2,3]]
```

</details>

<details>
<summary>TensorFlow</summary>

```python
i = tf.range(3)[:,None]
j = tf.range(4)[None,:]

I = tf.broadcast_to(i,(3,4))
J = tf.broadcast_to(j,(3,4))
```

Result

```
shape → (3,4)
```

</details>

<details>
<summary>Keras</summary>

```python
i = ops.arange(3)[:,None]
j = ops.arange(4)[None,:]

I = ops.broadcast_to(i,(3,4))
J = ops.broadcast_to(j,(3,4))
```

</details>

# Flatten grid to points

<details>
<summary>NumPy</summary>

```python
points = np.stack((x, y), axis=-1).reshape(-1, 2)
```

Result

```
shape → (12,2)
```

Convert grid → list of coordinates.

</details>

<details>
<summary>PyTorch</summary>

```python
points = torch.stack((x, y), dim=-1).reshape(-1, 2)
```

Result

```
shape → (12,2)
```

</details>

<details>
<summary>TensorFlow</summary>

```python
points = tf.reshape(tf.stack((x, y), axis=-1), (-1, 2))
```

Result

```
shape → (12,2)
```

</details>

<details>
<summary>Keras</summary>

```python
points = ops.reshape(ops.stack((x, y), axis=-1), (-1, 2))
```

Result

```
shape → (12,2)
```

</details>

# Examples


<details>
<summary>Contour plotting</summary>

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)

X, Y = np.meshgrid(x, y, indexing="ij")
Z = np.sin(X) * np.cos(Y)

plt.figure()
plt.contourf(X, Y, Z, levels=30)
plt.colorbar()
plt.title("Contour plot of sin(x)*cos(y)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
````

<img width="562" height="455" alt="image" src="https://github.com/user-attachments/assets/9601691b-5040-4c48-bb2f-f2969cfcfeef" />

</details>

<details>
<summary>Distance matrix (broadcasting)</summary>

```python
import numpy as np

a = np.array([1.0, 3.5, 7.2])[:, None]
b = np.array([0.8, 2.9, 7.5, 9.0])[None, :]

D = np.abs(a - b)

print("Distance matrix:")
print(D)
print("Shape:", D.shape)
````

Results:

```
Distance matrix:
...
Distance matrix:
[[0.2 1.9 6.5 8. ]
 [2.7 0.6 4.  5.5]
 [6.4 4.3 0.3 1.8]]
Shape: (3, 4)
```

</details>

<details>
<summary>Voxel coordinates</summary>

```python
import numpy as np

D, H, W = 4, 5, 6

z, y, x = np.indices((D, H, W))

print("z shape:", z.shape)
print("Example voxel coordinate:")
print("z,y,x =", z[2,3,4], y[2,3,4], x[2,3,4])
````

Results:

```
z shape: (4, 5, 6)
Example voxel coordinate:
z,y,x = 2 3 4
```

</details>


<details>
<summary>Surface plotting and interpolation</summary>

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator

x = np.linspace(0, 5, 20)
y = np.linspace(0, 5, 20)
X, Y = np.meshgrid(x, y, indexing="ij")
Z = np.sin(X) * np.cos(Y)

interp = RegularGridInterpolator((x, y), Z)

points = np.array([
    [1.3, 2.7],
    [3.2, 4.1],
    [0.8, 1.5]
])

values = interp(points)

print("Interpolated values:")
print(values)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_title("Surface plot")

plt.show()
````

Results:

````
Interpolated values:
[-0.86357599  0.03295481  0.05012175]
````
<img width="415" height="421" alt="image" src="https://github.com/user-attachments/assets/48e04c45-e376-4c43-8e83-770e7b3e61ad" />

</details>
