### Combining commits

Combine the last 3 commits:

```bash
git rebase -i HEAD~3
```

Editor opens:

```text
pick a1b2c3d Add SSI preprocessing
pick e4f5g6h Fix edge case
pick i7j8k9l Cleanup logs
```

Change to:

```text
pick a1b2c3d Add SSI preprocessing
squash e4f5g6h Fix edge case
squash i7j8k9l Cleanup logs
```

Save and exit → Git combines them into **one commit**.

Push with cleaned history:

```bash
git push --force-with-lease
```
