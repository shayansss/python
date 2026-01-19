### Example: `git restore -p <file>` (interactive discard)

Assume you modified `example.py` in **two different places**, but you want to **discard only part of the changes**, not all of them.

#### 1. Check the current status

```bash
git status
```

Output (simplified):

```
modified: example.py
```

#### 2. Run interactive restore

```bash
git restore -p example.py
```

Git now shows changes **hunk by hunk**:

```
diff --git a/example.py b/example.py
index 3a2f1c1..9b8d7e4 100644
--- a/example.py
+++ b/example.py
@@ -10,7 +10,7 @@ def compute(x):
-    return x * 2
+    return x * 3
```

Git asks:

```
Discard this hunk from worktree [y,n,q,a,d,e,?]?
```

#### 3. Choose what to discard

* `y` → discard **this** change
* `n` → keep this change
* `a` → discard **all remaining hunks**
* `d` → keep **all remaining hunks**
* `e` → manually edit the hunk
* `q` → quit
