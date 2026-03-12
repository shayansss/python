| Concept | Python | NumPy | PyTorch | TensorFlow | Keras | Notes |
|---|---|---|---|---|---|---|
| Imports | built-in | `import numpy as np` | `import torch` | `import tensorflow as tf` | `from keras import ops` | Used in examples |
| Basic slicing | lists support slicing | `a[1:4]` | `x[1:4]` | `x[1:4]` | `x[1:4]` | Start inclusive, stop exclusive |
| Step slicing | lists support steps | `a[::2]` | `x[::2]` | `x[::2]` | `x[::2]` | Every k-th element |
| Negative indexing | `a[-1]` | `a[-1]` | `x[-1]` | `x[-1]` | `x[-1]` | Last element, etc. |
| Multi-axis indexing | nested indexing | `a[i,j]` | `x[i,j]` | `x[i,j]` | `x[i,j]` | Cleaner than chained indexing |
| Row / column selection | manual | `a[1,:]`, `a[:,2]` | same | same | same | Very common in matrices |
| Integer array indexing | manual/list comps | `a[[0,2]]` | `x[[0,2]]` | `tf.gather` | `ops.take` | Select arbitrary positions |
| Boolean masking | list comps | `a[a>0]` | `x[x>0]` | `tf.boolean_mask` | boolean mask / `ops.take` patterns | Filter by condition |
| Take by axis | manual | `np.take` | `torch.index_select` | `tf.gather` | `ops.take` | Framework-style indexed selection |
| Conditional selection | `x if c else y` | `np.where` | `torch.where` | `tf.where` | `ops.where` | Elementwise choose |
| Scatter / indexed write | manual | `a[idx]=...` | `index_put_`, `scatter_` | `tf.tensor_scatter_nd_update` | backend-dependent | Write into selected positions |
| Add new axis | n/a | `None`, `np.newaxis` | `None`, `unsqueeze` | `tf.newaxis`, `expand_dims` | `ops.expand_dims` | Useful for broadcasting |

# Basic slicing

<details>
<summary>Python</summary>

```python
a = [10, 20, 30, 40, 50]
a[1:4]
````

Result

```python
[20, 30, 40]
```

</details>

<details>
<summary>NumPy</summary>

```python
a = np.array([10, 20, 30, 40, 50])
a[1:4]
```

Result

```python
array([20, 30, 40])
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([10, 20, 30, 40, 50])
x[1:4]
```

Result

```python
tensor([20, 30, 40])
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([10, 20, 30, 40, 50])
x[1:4]
```

Result

```python
shape → (3,)
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.array([10, 20, 30, 40, 50])
x[1:4]
```

</details>

# Step slicing

<details>
<summary>Python</summary>

```python
a = [10, 20, 30, 40, 50, 60]
a[::2]
```

Result

```python
[10, 30, 50]
```

</details>

<details>
<summary>NumPy</summary>

```python
a = np.array([10, 20, 30, 40, 50, 60])
a[::2]
```

Result

```python
array([10, 30, 50])
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([10, 20, 30, 40, 50, 60])
x[::2]
```

Result

```python
tensor([10, 30, 50])
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([10, 20, 30, 40, 50, 60])
x[::2]
```

Result

```python
shape → (3,)
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.array([10, 20, 30, 40, 50, 60])
x[::2]
```

</details>

# Negative indexing

<details>
<summary>Python</summary>

```python
a = [10, 20, 30, 40]
a[-1], a[-2]
```

Result

```python
(40, 30)
```

</details>

<details>
<summary>NumPy</summary>

```python
a = np.array([10, 20, 30, 40])
a[-1], a[-2]
```

Result

```python
(40, 30)
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([10, 20, 30, 40])
x[-1], x[-2]
```

Result

```python
(tensor(40), tensor(30))
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([10, 20, 30, 40])
x[-1], x[-2]
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.array([10, 20, 30, 40])
x[-1], x[-2]
```

</details>

# Multi-axis indexing

<details>
<summary>Python</summary>

```python
a = [[1, 2, 3],
     [4, 5, 6]]

a[1][2]
```

Result

```python
6
```

</details>

<details>
<summary>NumPy</summary>

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

a[1, 2]
```

Result

```python
6
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])

x[1, 2]
```

Result

```python
tensor(6)
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([[1, 2, 3],
                 [4, 5, 6]])

x[1, 2]
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.array([[1, 2, 3],
               [4, 5, 6]])

x[1, 2]
```

</details>

# Row / column selection

<details>
<summary>NumPy</summary>

```python
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

a[1, :]
a[:, 2]
```

Result

```python
a[1, :] → array([4, 5, 6])
a[:, 2] → array([3, 6, 9])
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

x[1, :]
x[:, 2]
```

Result

```python
x[1, :] → tensor([4, 5, 6])
x[:, 2] → tensor([3, 6, 9])
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

x[1, :]
x[:, 2]
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

x[1, :]
x[:, 2]
```

</details>

# Integer indexing

<details>
<summary>Python</summary>

```python
a = ['a', 'b', 'c', 'd']
idx = [0, 2, 3]

[a[i] for i in idx]
```

Result

```python
['a', 'c', 'd']
```

</details>

<details>
<summary>NumPy</summary>

```python
a = np.array(['a', 'b', 'c', 'd'])
a[[0, 2, 3]]
```

Result

```python
array(['a', 'c', 'd'], dtype='<U1')
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([10, 20, 30, 40])
x[[0, 2, 3]]
```

Result

```python
tensor([10, 30, 40])
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([10, 20, 30, 40])
tf.gather(x, [0, 2, 3])
```

Result

```python
shape → (3,)
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.array([10, 20, 30, 40])
ops.take(x, ops.array([0, 2, 3]), axis=0)
```

</details>

# Boolean masking

<details>
<summary>Python</summary>

```python
a = [3, -1, 5, -2, 0]
[v for v in a if v > 0]
```

Result

```python
[3, 5]
```

</details>

<details>
<summary>NumPy</summary>

```python
a = np.array([3, -1, 5, -2, 0])
a[a > 0]
```

Result

```python
array([3, 5])
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([3, -1, 5, -2, 0])
x[x > 0]
```

Result

```python
tensor([3, 5])
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([3, -1, 5, -2, 0])
tf.boolean_mask(x, x > 0)
```

Result

```python
shape → (2,)
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.array([3, -1, 5, -2, 0])
mask = x > 0
ops.take(x, ops.where(mask)[:, 0], axis=0)
```

</details>

# Take by axis

<details>
<summary>NumPy</summary>

```python
a = np.array([[10, 11, 12],
              [20, 21, 22],
              [30, 31, 32]])

np.take(a, [0, 2], axis=1)
```

Result

```python
array([[10, 12],
       [20, 22],
       [30, 32]])
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([[10, 11, 12],
                  [20, 21, 22],
                  [30, 31, 32]])

torch.index_select(x, dim=1, index=torch.tensor([0, 2]))
```

Result

```python
tensor([[10, 12],
        [20, 22],
        [30, 32]])
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([[10, 11, 12],
                 [20, 21, 22],
                 [30, 31, 32]])

tf.gather(x, [0, 2], axis=1)
```

Result

```python
shape → (3,2)
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.array([[10, 11, 12],
               [20, 21, 22],
               [30, 31, 32]])

ops.take(x, ops.array([0, 2]), axis=1)
```

</details>

# Conditional selection with where

<details>
<summary>NumPy</summary>

```python
a = np.array([-2, -1, 0, 1, 2])
np.where(a > 0, a, 0)
```

Result

```python
array([0, 0, 0, 1, 2])
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([-2, -1, 0, 1, 2])
torch.where(x > 0, x, 0)
```

Result

```python
tensor([0, 0, 0, 1, 2])
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([-2, -1, 0, 1, 2])
tf.where(x > 0, x, 0)
```

</details>

<details>
<summary>Keras</summary>

```python
x = ops.array([-2, -1, 0, 1, 2])
ops.where(x > 0, x, 0)
```

</details>

# Indexed write / scatter

<details>
<summary>Python</summary>

```python
a = [10, 20, 30, 40]
a[1] = 99
a
```

Result

```python
[10, 99, 30, 40]
```

</details>

<details>
<summary>NumPy</summary>

```python
a = np.array([10, 20, 30, 40])
a[[1, 3]] = [99, 77]
a
```

Result

```python
array([10, 99, 30, 77])
```

</details>

<details>
<summary>PyTorch</summary>

```python
x = torch.tensor([10, 20, 30, 40])
x[[1, 3]] = torch.tensor([99, 77])
x
```

Result

```python
tensor([10, 99, 30, 77])
```

</details>

<details>
<summary>TensorFlow</summary>

```python
x = tf.constant([10, 20, 30, 40])
tf.tensor_scatter_nd_update(x, indices=[[1], [3]], updates=[99, 77])
```

Result

```python
shape → (4,)
```

</details>

# Examples

<details>
<summary>Swap two columns of a dataset</summary>

```python
import numpy as np

X = np.array([
    [1, 10, 100],
    [2, 20, 200],
    [3, 30, 300],
])

# swap column 0 and column 2
X[:, [0, 2]] = X[:, [2, 0]]

print(X)
```

Result

```
[[100  10   1]
 [200  20   2]
 [300  30   3]]
```

</details>

<details>
<summary>Subsample every third measurement</summary>

```python
import numpy as np

measurements = np.arange(15)

subsample = measurements[::3]

print(subsample)
```

Result

```
[0 3 6 9 12]
```

</details>

<details>
<summary>Reorder rows based on ranking</summary>

```python
import numpy as np

scores = np.array([82, 91, 76, 88])
names = np.array(["A", "B", "C", "D"])

order = np.argsort(scores)[::-1]

sorted_names = names[order]
sorted_scores = scores[order]

print(sorted_names)
print(sorted_scores)
```

Result

```
['B' 'D' 'A' 'C']
[91 88 82 76]
```

</details>
