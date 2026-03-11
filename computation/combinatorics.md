# Summary


| Concept                    | Python                                    | NumPy                          | PyTorch                               | TensorFlow                | Keras                   | Notes                  |
| --------------------------   | ----------------------------------------- | ------------------------------ | ------------------------------------- | ------------------------- | ----------------------- | ---------------------- |
| Imports                      | `import itertools`, `import math`         | `import numpy as np`           | `import torch`                        | `import tensorflow as tf` | `from keras import ops` | Used in examples       |
| Permutations                 | `itertools.permutations`                  | convert to array               | manual / `torch.permute` is different | manual                    | manual                  | Order matters          |
| Combinations w/o replacement | `itertools.combinations`                  | convert to array               | manual                                | manual                    | manual                  | Order does not matter  |
| Combinations w/ repetition   | `itertools.combinations_with_replacement` | convert to array               | manual                                | manual                    | manual                  | Multiset combinations  |
| Cartesian product            | `itertools.product`                       | `np.array(list(product(...)))` | `torch.cartesian_prod`                | meshgrid + reshape        | meshgrid + reshape      | All tuples across sets |
| nCk formula                  | `math.comb(n,k)`                          | same formula                   | factorial formula                     | factorial formula         | factorial formula       | Count only             |
| nPk formula                  | `math.perm(n,k)`                          | same formula                   | factorial formula                     | factorial formula         | factorial formula       | Ordered selections     |
| Power set                    | combinations loop                         | object array                   | manual                                | manual                    | manual                  | All subsets            |
| Random permutations          | `random.sample`                           | `np.random.permutation`        | `torch.randperm`                      | `tf.random.shuffle`       | `ops.random.shuffle`    | Shuffle elements       |


# Permutations

Ordered arrangements of elements.

$$
P(n,k)=\frac{n!}{(n-k)!}
$$

<details>
<summary>Python</summary>

```python
list(itertools.permutations([1,2,3],2))
```

Result

```
[(1,2),(1,3),
 (2,1),(2,3),
 (3,1),(3,2)]
```

Count

```python
math.perm(3,2)
```

Result

```
6
```

</details>

 

<details>
<summary>NumPy</summary>

```python
np.array(list(itertools.permutations([1,2,3],2)))
```

Result

```
array([[1,2],
       [1,3],
       [2,1],
       [2,3],
       [3,1],
       [3,2]])
```

shape → `(6,2)`

</details>

 

<details>
<summary>PyTorch</summary>

```python
torch.tensor(list(itertools.permutations([1,2,3],2)))
```

Result

```
tensor([[1,2],
        [1,3],
        [2,1],
        [2,3],
        [3,1],
        [3,2]])
```

</details>

 

<details>
<summary>TensorFlow</summary>

```python
tf.constant(list(itertools.permutations([1,2,3],2)))
```

Result

```
shape → (6,2)
```

</details>

 

<details>
<summary>Keras</summary>

```python
ops.convert_to_tensor(list(itertools.permutations([1,2,3],2)))
```

</details>

 

# Combinations

Selections **without order**.

$$
C(n,k)=\frac{n!}{k!(n-k)!}
$$

<details>
<summary>Python</summary>

```python
list(itertools.combinations([1,2,3],2))
```

Result

```
[(1,2),
 (1,3),
 (2,3)]
```

Count

```python
math.comb(3,2)
```

Result

```
3
```

</details>

 

<details>
<summary>NumPy</summary>

```python
np.array(list(itertools.combinations([1,2,3],2)))
```

Result

```
array([[1,2],
       [1,3],
       [2,3]])
```

shape → `(3,2)`

</details>

 

<details>
<summary>PyTorch</summary>

```python
torch.tensor(list(itertools.combinations([1,2,3],2)))
```

Result

```
tensor([[1,2],
        [1,3],
        [2,3]])
```

</details>

 

<details>
<summary>TensorFlow</summary>

```python
tf.constant(list(itertools.combinations([1,2,3],2)))
```

Result

```
shape → (3,2)
```

</details>

 

<details>
<summary>Keras</summary>

```python
ops.convert_to_tensor(list(itertools.combinations([1,2,3],2)))
```

</details>

 

# Combinations with repetition

Elements can repeat.

<details>
<summary>Python</summary>

```python
list(itertools.combinations_with_replacement([1,2,3],2))
```

Result

```
[(1,1),
 (1,2),
 (1,3),
 (2,2),
 (2,3),
 (3,3)]
```

</details>

 

<details>
<summary>NumPy</summary>

```python
np.array(list(itertools.combinations_with_replacement([1,2,3],2)))
```

Result

```
array([[1,1],
       [1,2],
       [1,3],
       [2,2],
       [2,3],
       [3,3]])
```

shape → `(6,2)`

</details>

 

# Cartesian product

All combinations across sets.

<details>
<summary>Python</summary>

```python
list(itertools.product(range(3),range(2)))
```

Result

```
[(0,0),(0,1),
 (1,0),(1,1),
 (2,0),(2,1)]
```

</details>

 

<details>
<summary>NumPy</summary>

```python
np.array(list(itertools.product(range(3),range(2))))
```

Result

```
array([[0,0],
       [0,1],
       [1,0],
       [1,1],
       [2,0],
       [2,1]])
```

shape → `(6,2)`

</details>

 

<details>
<summary>PyTorch</summary>

```python
torch.cartesian_prod(torch.arange(3),torch.arange(2))
```

Result

```
tensor([[0,0],
        [0,1],
        [1,0],
        [1,1],
        [2,0],
        [2,1]])
```

shape → `(6,2)`

</details>

 

<details>
<summary>TensorFlow</summary>

```python
tf.reshape(
    tf.stack(tf.meshgrid(tf.range(3),tf.range(2),indexing="ij"),axis=-1),
    (-1,2)
)
```

Result

```
shape → (6,2)
```

</details>


<details>
<summary>Keras</summary>

```python
ops.reshape(
    ops.stack(ops.meshgrid(ops.arange(3),ops.arange(2),indexing="ij"),axis=-1),
    (-1,2)
)
```

</details>

 

# Power set

All subsets.

<details>
<summary>Python</summary>

```python
items=[1,2,3]

powerset=[
    c
    for r in range(len(items)+1)
    for c in itertools.combinations(items,r)
]

print(powerset)
```

Result

```
[(),
 (1,),
 (2,),
 (3,),
 (1,2),
 (1,3),
 (2,3),
 (1,2,3)]
```

</details>


<details>
<summary>NumPy</summary>

```python
items=[1,2,3]

powerset=[
    c
    for r in range(len(items)+1)
    for c in itertools.combinations(items,r)
]

np.array(powerset,dtype=object)
```

Result

```
[() (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)]
```

Note: subsets have different lengths → `dtype=object`.

</details>


# Random permutations

Useful for ML shuffling / sampling.

<details>
<summary>Python</summary>

```python
import random

random.sample(range(5),5)
```

</details>

 

<details>
<summary>NumPy</summary>

```python
np.random.permutation(5)
```

Result

```
array([3,1,4,0,2])
```

</details>


<details>
<summary>PyTorch</summary>

```python
torch.randperm(5)
```

Result

```
tensor([2,0,4,1,3])
```

</details>


<details>
<summary>TensorFlow</summary>

```python
tf.random.shuffle(tf.range(5))
```

</details>


<details>
<summary>Keras</summary>

```python
ops.random.shuffle(ops.arange(5))
```

</details>


# Examples

<details>
<summary>All 3-letter codes from alphabet subset</summary>

```python
from itertools import permutations

letters=['A','B','C','D']

codes=list(permutations(letters,3))

print("Total:",len(codes))
```

Result

```
Total: 24
```

</details>
 

<details>
<summary>Feature subset search (ML)</summary>

```python
from itertools import combinations

features=['x1','x2','x3','x4']

for subset in combinations(features,2):
    pass
```

</details>
