# This cheatsheet is under development


### **Setting Up**
- `git config --global user.name "Your Name"`: Sets your name for commits.
- `git config --global user.email "you@example.com"`: Sets your email for commits.
- `git config --list`: Displays the current Git configuration.

### **Basic Commands**
- `git init`: Initializes a new Git repository.
- `git clone <repository_url>`: Clones an existing repository to your local machine.
- `git status`: Shows the status of changes in the working directory.
- `git add <file>`: Stages a specific file for commit.
- `git add .`: Stages all changes for commit.
- `git commit -m "message"`: Commits staged changes with a descriptive message.

### **Branching and Merging**
- `git branch`: Lists all branches in the repository.
- `git branch <branch_name>`: Creates a new branch.
- `git checkout <branch_name>`: Switches to a different branch.
- `git switch <branch_name>`: Alternative to `git checkout` for switching branches.
- `git merge <branch_name>`: Merges the specified branch into the current branch.
- `git branch -d <branch_name>`: Deletes a branch.

### **Working with Remotes**
- `git remote -v`: Lists remote repositories.
- `git remote add origin <repository_url>`: Adds a remote repository.
- `git pull origin <branch_name>`: Fetches and merges changes from the remote branch.
- `git push origin <branch_name>`: Pushes local changes to the remote branch.

### **Undoing Changes**
- `git checkout -- <file>`: Reverts changes to a specific file (unstaged changes).
- `git reset <file>`: Unstages a staged file.
- `git reset --soft HEAD~1`: Removes the last commit but keeps changes staged.
- `git reset --hard HEAD~1`: Removes the last commit and discards changes.
- `git revert <commit_hash>`: Reverts changes made by a specific commit (creates a new commit).

### **Viewing History**
- `git log`: Displays the commit history.
- `git log --oneline`: Shows a condensed commit history.
- `git diff`: Shows differences between working directory and staging area.
- `git diff <branch_name>`: Compares the current branch with another branch.

### **Stashing**
- `git stash`: Temporarily saves changes.
- `git stash push -m "Work in progress on feature X"`: Stash with a comment.
- `git stash --keep-index`: Stash only the changes that are not staged for commit
  
- `git stash list`: Lists stashed changes.
- `git stash apply`: Applies stashed changes without removing them from stash.
- `git stash apply stash@{1}` Apply a specific stash.

- `git stash pop`: Applies and removes stashed changes.
- `git stash clear`: Clear them all.

### **Tagging**
- `git tag`: Lists all tags.
- `git tag <tag_name>`: Creates a new tag.
- `git push origin <tag_name>`: Pushes a tag to the remote repository.

### **Collaboration**
- `git fetch`: Fetches updates from the remote repository without merging.
- `git cherry-pick <commit_hash>`: Applies a specific commit to the current branch.
- `git rebase <branch_name>`: Reapplies commits on top of another branch.

### **Cleaning Up**
- `git clean -f`: Removes untracked files.
- `git clean -fd`: Removes untracked files and directories.


### What is a Git Tag?

A **Git tag** is a reference that points to a specific commit in the Git history. Tags are typically used to mark important milestones in a project's development, making it easier to reference specific versions of the code.

There are two main types of tags in Git:

1. **Lightweight Tags**: A simple reference to a commit, like a pointer.
2. **Annotated Tags**: A tag that stores extra metadata, including a message, the tagger's name, email, and date. These are often preferred for releases **releases** (e.g., `v1.0`, `v2.3`).

### Why Use Tags?
- **Versioning**: Tags are commonly used to mark specific releases (e.g., `v1.0`, `v2.1-beta`).
- **Rollbacks**: If an issue arises, you can easily revert to a specific version of your code.
- **Reference Points**: Tags make it easy to find and compare specific commits in the Git history.

### How to Work with Git Tags

#### **1. List Tags**
- `git tag`: Lists all existing tags in your repository.
- `git tag --list "v1.*"`: Filters and lists tags matching a specific pattern.

#### **2. Create Tags**
- **Lightweight Tag**:
  ```bash
  git tag <tag_name>
  ```
  Example:
  ```bash
  git tag v1.0
  ```

- **Annotated Tag**:
  ```bash
  git tag -a <tag_name> -m "Message describing the tag"
  ```
  Example:
  ```bash
  git tag -a v1.0 -m "First stable release"
  ```

#### **3. View a Specific Tag**
- `git show <tag_name>`: Displays details of the tagged commit, including the message for annotated tags.

#### **4. Push Tags to a Remote Repository**
By default, tags are not automatically pushed to the remote repository. You need to push them explicitly:
- Push a single tag:
  ```bash
  git push origin <tag_name>
  ```
- Push all tags:
  ```bash
  git push origin --tags
  ```

#### **5. Delete Tags**
- Delete a local tag:
  ```bash
  git tag -d <tag_name>
  ```
  Example:
  ```bash
  git tag -d v1.0
  ```

- Delete a remote tag:
  ```bash
  git push origin --delete <tag_name>
  ```
  Example:
  ```bash
  git push origin --delete v1.0
  ```

#### **6. Checkout a Tag**
If you want to check out the code associated with a tag:
```bash
git checkout <tag_name>
```
However, this puts your repository into a **detached HEAD state**, meaning you’re not on any branch. If you want to create a branch from this tag:
```bash
git checkout -b <new_branch_name> <tag_name>
```

---

### What is `git stash`?

`git stash` is a Git command used to temporarily save changes in your working directory without committing them. It is helpful when you need to switch branches or work on something else without losing your current progress. Stashing saves your changes on a "stack," allowing you to come back and restore them later.

---

### Key Features of `git stash`:
- Temporarily saves **uncommitted changes** (both staged and unstaged).
- Clears your working directory, allowing you to work on other tasks.
- Can restore stashed changes at any time.

---

### Common Use Cases:
1. **Switching branches**: You are working on a feature but need to switch to another branch to address an urgent issue.
2. **Experimentation**: You want to test something out but don’t want to risk losing your current changes.
3. **Clean workspace**: You want to quickly stash your changes and pull the latest updates.

---

### Basic Commands and Examples:



#### **3. Apply Stash**
- To restore the most recent stash:
  ```bash
  git stash apply
  ```
  This restores the stashed changes but **keeps the stash in the list**.

- To apply a specific stash:
  ```bash
  git stash apply stash@{1}
  ```

---

#### **4. Remove Stash After Applying**
- If you’ve restored your stash and no longer need it, use:
  ```bash
  git stash drop stash@{0}
  ```
  Or combine applying and dropping in one command:
  ```bash
  git stash pop
  ```
  This applies the most recent stash and **removes it from the list**.

---

#### **5. Stash Only Unstaged Changes**
- If you want to stash only **unstaged changes** while keeping staged changes:
  ```bash
  git stash --keep-index
  ```

---

#### **6. Stash Specific Files**
- If you don’t want to stash all changes, you can stash specific files:
  ```bash
  git stash push <file>
  ```
  Example:
  ```bash
  git stash push file1.txt
  ```

---

#### **7. Clear All Stashes**
- To delete all stashed changes:
  ```bash
  git stash clear
  ```

---

#### **8. Show Stash Details**
- To see what’s inside a stash:
  ```bash
  git stash show stash@{0}
  ```
  Add `-p` for a detailed view of changes:
  ```bash
  git stash show -p stash@{0}
  ```

---

### Workflow Example:

1. You're working on `main` and make changes to `file1.txt` and `file2.txt`.
2. You need to quickly fix an issue in another branch (`hotfix`):
   ```bash
   git stash
   git checkout hotfix
   ```
3. After fixing the issue, return to `main` and restore your changes:
   ```bash
   git checkout main
   git stash apply
   git stash drop
   ```

---

### Key Tips:
- Always provide descriptive messages when stashing (`git stash push -m "message"`) so you can track what’s in each stash.
- Remember that stashing only saves **uncommitted changes**. Committed changes are safe and do not need stashing.
