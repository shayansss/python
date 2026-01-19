# GIT

### Setting up repositories
- `git config` command is used to customize Git behavior with: 
  - `--global` for user-wide settings. 
  - `--local` for repository-specific settings. 
  - `--system` (admin access) for system-wide settings.
- `git config --list`: Displays the current Git configuration.
- For connecting to remote repo:
  - `git config --global user.name "Your Name"`.
  - `git config --global user.email "you@example.com"`.
  - Two ways to connect:
    - `git clone <repository_url>`: Downloads an existing repo.
      - Once changes are pushed, credentials (e.g., GitHub **access tokens**) are requested.
      - `git clone -b <branch_name> --single-branch <repository_url>`: Clones a branch.
      - `git clone --recurse-submodules <repository_url>`: Clones all **submodules** (other repositories inside it).
    - `git init`: Initializes a repo locally in the current dir, by creating `.git` dir, allowing tracking files. Then:
      - `git init <directory_name>`: Initializes in a dir.
      - `git remote add <remote repo alias like origin> <remote_url>`: Adds a remote repository.
      - `git remote rm origin`: Removes the repo.
      - `git remote -v`: Verifies it is added.
      - Exclude files or dirs from being tracked as specified in `.gitignore` [eg.1](https://github.com/shayansss/python/blob/main/git/eg1.md).

### Synching
- `git status`: Shows the status of changes in the working directory.
- `git add .`: Stages all changes for commit.
- `git commit -m "message"`: Commits staged changes with a descriptive message.
- `git commit --amend --no-edit`: Adds currently staged changes to the last commit (with no message change)
- `git show`: Shows the last commit (metadata + diff).
- `git pull origin <branch_name>`: Fetches and merges changes from the remote branch.
- `git push origin <branch_name>`: Pushes local changes to the remote branch.
- `git push -u origin main`:
  - Sets the **upstream branch**, i.e., link the local branch to origin/main.
  - After `git push` and `git pull` alone possible.

## Path shortcuts
* `.` : Current directory: (E.g., `git status .`: Status limited to current directory).
* `..` : Parent directory: (E.g., `git add ..`: Stage changes from parent directory).
* `../..` : Two levels up (E.g., `git diff ../..`).
* `--` : Separator between revisions and paths
  * Prevents ambiguity between branch names and file names.
  * E.g., `git checkout -- file.txt`: Restore file (not a branch named `file.txt`)
  * E.g., `git log -- src/`: History only for `src/`

## Pathspec magic
* `git add '*.py'`: All Python files.
* `git add :/pattern`: Search from repo root.
* `git add :(exclude)tests/`: Exclude path.
* `git add src/ :(exclude)src/tmp/`

### Adding/removing
- `git clean -f`: Removes untracked files.
- `git clean -fd`: Removes untracked files and directories.
- `git rm <file>`: Removes a file from both the working directory and Git.
- `git rm -r <dir>`: Removes directory from git + disk.
- `git blame <file>`: Shows who changed which line (and when).
- `git grep "pattern"`: Searches in tracked files (fast).
- `git rm --cached .`: Removes all from Git (used especially when we forget to add a file set in `.gitignore`).

### Branching
- `git branch -a`: Lists all branches in the repository.
  - `git branch`: Lists local branches.
  - `git branch -r`: Lists remote branches.
- `git branch <branch_name>`: Creates a new branch.
- `git branch -d <branch_name>`: Deletes a branch.
- `git branch -D <branch_name>`: Force-deletes a branch.
- `git remote -v`: Lists remote repositories.
  - `git remote -v`: More verbose as it also   
- `git checkout <branch_name>` or `git switch <branch_name>`: Switches to a branch.
  - `git checkout -b <branch_name>`: Creates and switches to a branch.

### Merging
- `git merge <branch_name>`: Merges the specified branch into the current branch.
- `git rebase <branch_name>`: Reapplies commits on top of another branch (more linear than merging).
- `git rebase -i <base>`: Interactively rewrite commit history starting from <base> [eg.3](https://github.com/shayansss/python/blob/main/git/eg3.md).

## Revision shortcuts
* `HEAD`: Current commit.
* `HEAD~1`: Parent of current commit.
  * E.g., `git diff HEAD~1`
  * E.g., `git reset --hard HEAD~1`
* `HEAD~2`: Two commits before HEAD.
* `HEAD^`: First parent (important in merges).
* `HEAD^2`: Second parent of a merge commit.
* `@`: Alias for `HEAD` (same thing).

## Range notation
* Double dot `A..B`: Commits in B that are NOT in A.
  * E.g., `git log --oneline --decorate --graph HEAD~5..HEAD`
  * Used to see what will be merged.
* Triple dot `A...B`: Commits reachable from either A or B but not both.
  * E.g., `git diff origin/main...HEAD`
  * Used understand how far branches diverged.

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
- `git restore -p <file>`: Shows or discards changes piece by piece: [eg2](https://github.com/shayansss/python/blob/main/git/eg2.md).

## Diff with ranges

* `git diff A..B`: Changes from A → B.
* `git diff A...B`: Changes from merge-base → B.
* `git diff HEAD -- file.py`: Diff file vs last commit.
* `git diff --cached`: Staged vs last commit.

### Stashing
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
