Here is the English translation of the Chinese README:

```markdown
# Git-GUI-CLI

## Introduction
`git-dit` is an open-source command-line tool designed to display Git commit history through a graphical interface. It uses ASCII characters and simple text formatting to draw history graphs of branches, merges, and other Git operations, allowing developers to intuitively understand the project's version control status without leaving the terminal.

## Main Features

- 🎨 **Branch Visualization**: Clearly displays branch creation, merging, rebasing, and other operations
- 🎯 **Interactive Browsing**: Supports keyboard navigation for free exploration of commit history
- 📊 **Multiple View Modes**: Provides various layout algorithms and display styles
- 🔍 **Smart Filtering**: Filter commits by author, date, commit message, etc.
- 🎭 **Color Customization**: Supports custom color schemes
- ⚡ **High Performance**: Runs smoothly even with large repositories
- 📦 **Zero Dependencies**: Pure text interface, no graphical environment required

## Installation

### Method 1: Use Precompiled Binary Directly
```bash
# Linux/macOS
curl -sSL https://gitee.com/with-the-flow/git-dit/releases/latest/download/git-dit-$(uname -s)-$(uname -m) -o git-dit
chmod +x git-dit
sudo mv git-dit /usr/local/bin/
```

### Method 2: Build from Source
```bash
git clone https://gitee.com/with-the-flow/git-dit.git
cd git-dit
cargo build --release
sudo cp target/release/git-dit /usr/local/bin/
```

### Method 3: Install via Cargo
```bash
cargo install git-dit
```

## Detailed Usage Instructions

### 1. Basic Usage

#### View Current Branch History
```bash
# Simplest usage, shows commit history of current branch
git dit

# Result: Displays commit chain starting from current HEAD in graphical format
```

#### View All Branches
```bash
# Shows history of all local branches and their relationships
git dit --all

# Alias: git dit -a
```

#### Limit Number of Commits
```bash
# Show only the latest 20 commits
git dit -n 20

# Or: git dit --max-count=20
```

### 2. Branch Filtering and Selection

#### View Specific Branches Only
```bash
# Show history of main and develop branches
git dit main develop

# Exclude certain branches
git dit --all --exclude=feature/temp --exclude=bugfix/test
```

#### Filter by Author
```bash
# Show only commits by John Doe
git dit --author="John Doe"

# Supports regular expressions
git dit --author="^(John|Jane)"
```

#### Filter by Date Range
```bash
# Commits from the last week
git dit --since="1 week ago"

# Specific date range
git dit --since="2024-01-01" --until="2024-03-31"

# Last month
git dit --since="last month"
```

#### Filter by Commit Message Keywords
```bash
# Search for commits containing "fix"
git dit --grep="fix"

# Search multiple keywords
git dit --grep="fix" --grep="bug" --all-match  # Contains both
git dit --grep="feature" --or --grep="feat"      # Matches either
```

### 3. View Modes and Layouts

#### Classic View (Default)
```bash
git dit --mode=classic
# Shows complete branch merge history, similar to git log --graph
```

#### Compact View
```bash
git dit --mode=compact
# Better for narrow terminals, compresses whitespace
```

#### Timeline View
```bash
git dit --mode=timeline
# Arranged chronologically, ignores branch structure
```

### 4. Interactive Operations

Git-DIT supports interactive browsing mode (similar to less):

```bash
# Enter interactive mode (default)
git dit --interactive

# Or: git dit -i
```

**Interactive Mode Shortcuts:**
- `↑/↓` or `j/k`: Move cursor up/down to select commits
- `←/→` or `h/l`: Horizontal scroll (for wide graphs)
- `Enter`: View details of selected commit
- `b`: Highlight current branch
- `a`: Toggle showing all branches/current branch
- `t`: Toggle tag display
- `r`: Refresh view (fetch new commits)
- `/`: Enter search mode, search by commit message
- `n`/`N`: Jump to next/previous match
- `m`: Switch view mode (classic/compact/timeline)
- `q` or `Ctrl+C`: Exit
- `?`: Show help information

### 5. Output Formatting

#### Custom Information Columns
```bash
# Show commit hash, author, date, message (default)
git dit --format="%h %an %ad %s"

# Add change statistics
git dit --format="%h %an %ad %s" --stat
```

#### Show Additional Information
```bash
# Show file change statistics
git dit --stat

# Show patch content (use with caution, output will be very long)
git dit -p

# Show tag information
git dit --tags

# Show references (branches, HEAD position)
git dit --decorate
```

#### Minimal Output
```bash
# Show only graph and commit message
git dit --oneline
```

### 6. Advanced Queries

#### Find Modification History of Specific Files
```bash
# View modification history of src/main.rs (including all branches)
git dit --all -- src/main.rs

# View history of a function (works with git log's -L parameter)
git dit -L ':function_name:src/main.rs'
```

#### View Branch Fork Points
```bash
# Find where feature branch diverged from main branch
git dit main..feature/new-ui
```

#### View Merge Commits
```bash
# Show only merge commits
git dit --merges

# Exclude merge commits
git dit --no-merges
```

#### Find Lost Commits (reflog)
```bash
# View all operation records, including deleted branches
git dit --reflog
```

### 7. Colors and Themes

#### Built-in Themes
```bash
# Use dark theme (default)
git dit --theme=dark

# Use light theme
git dit --theme=light

# Use monochrome (for terminals without color support)
git dit --theme=mono
```

#### Custom Colors
```bash
# Customize via environment variables
export GIT_DIT_COLOR_BRANCH="cyan"
export GIT_DIT_COLOR_COMMIT="yellow"
export GIT_DIT_COLOR_MERGE="magenta"

# Or command-line parameters
git dit --color-branch=cyan --color-commit=yellow
```

#### Disable Colors
```bash
git dit --no-color
# Or: git dit --color=never
```

### 8. Performance Optimization

#### Speed Up Large Repository Queries
```bash
# Skip detailed diff calculation
git dit --no-diff

# Limit recursion depth
git dit --depth=10

# Use simplified topology (trade some accuracy for speed)
git dit --simplify-by-decoration
```

#### Parallel Processing
```bash
# Use multi-threading acceleration (if enabled at compile time)
git dit --threads=4
```

### 9. Integration with Other Tools

#### Pipe Output to Other Commands
```bash
# Count commits by a specific author
git dit --author="John Doe" --oneline | wc -l

# Find large file commits
git dit --all --name-only | sort | uniq -c | sort -nr

# Export to DOT format (for Graphviz)
git dit --export=dot > history.dot
dot -Tpng history.dot -o history.png
```

#### Use in Git Aliases
```bash
# Add to ~/.gitconfig
git config --global alias.dit 'dit --all --decorate'
git config --global alias.ditl 'dit --oneline --graph'
git config --global alias.dits 'dit --stat'
```

#### Use with less
```bash
# For super wide graphs, use less for horizontal scrolling
git dit --color=always | less -R -S
```

### 10. Configuration File

Git-DIT supports configuration file `~/.git-dit/config.toml`:

```toml
# Example configuration file
[display]
theme = "dark"
mode = "classic"
max-commits = 100

[behavior]
interactive = true
refresh-interval = 30  # seconds, 0 means no auto-refresh

[filter]
exclude-branches = ["feature/temp", "test/*"]
authors = ["@company.com"]  # Show only company emails

[colors]
branch = "cyan"
commit = "yellow"
merge = "magenta"
tag = "green"
```

### 11. Special Scenario Usage

#### Open Source Contribution Analysis
```bash
# View external contributors' commits (exclude internal members)
git dit --all --not --author="*@company.com" --author="*@internal.com"

# Count branch activity
git dit --all --format="%an %ad %s" | grep "2 weeks ago" | wc -l
```

#### Code Review Assistance
```bash
# View PR/merge request history
git dit origin/main..origin/feature-branch

# View all commits involved in a release
git dit --oneline v1.0.0..v2.0.0
```

#### Troubleshooting
```bash
# Visualize history during bisect
git bisect start
git dit --bisect  # Show bisect progress

# View possible bug-introducing commits
git dit --all --grep="bug\|fix" --since="1 month ago"
```

### 12. Common Combination Examples

```bash
# Check team progress before daily standup
git dit --all --since="yesterday" --author="@team.com" --oneline

# Check branch status before release
git dit --all --decorate --tags --simplify-by-decoration

# Prepare for Code Review
git dit origin/main...HEAD --stat --grep="TODO\|FIXME"

# Analyze before cleaning old branches
git dit --all --no-merges --since="6 months ago" --format="%an %ad %s"
```

## ⚙️ Configuration Options

Git-DIT automatically reads the following configuration files (in priority order):

1. `./.git-dit/config.toml` - Project-level configuration
2. `~/.git-dit/config.toml` - User-level configuration
3. `/etc/git-dit/config.toml` - System-level configuration

The environment variable `GIT_DIT_CONFIG` can specify an additional configuration file path.

## Contribution Guidelines

Issues and Pull Requests are welcome!

### Development Environment Setup
```bash
git clone https://gitee.com/with-the-flow/git-dit.git
cd git-dit
cargo test
cargo build --release
```

### Commit Conventions
- Use [Conventional Commits](https://www.conventionalcommits.org/)
- Add test cases
- Update relevant documentation

## License

MIT License - See [LICENSE](LICENSE) file for details

## Acknowledgments

Thanks to all contributors and the Git community for their support!

---

**Tip**: Use `git dit --help` to view complete command-line options, or press `?` in interactive mode to see shortcut key help.
```