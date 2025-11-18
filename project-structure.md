<<<<<<< HEAD
## 📁 `git-dit` 完整项目结构

```
git-dit/                               # 项目根目录
├── src/git_dit/                       # 主包（使用 src 布局）
│   ├── __init__.py                    # 版本号: __version__ = "1.0.0"
│   ├── py.typed                       # 支持类型提示
│   │
│   ├── core/                          # 核心引擎
│   │   ├── __init__.py
│   │   ├── history.py                 # 历史图渲染引擎（ASCII/Unicode）
│   │   ├── parser.py                  # Git 输出解析器
│   │   └── models.py                  # 数据模型（Commit, Branch, Merge）
│   │
│   ├── commands/                      # Git 命令封装层
│   │   ├── __init__.py
│   │   ├── base.py                    # 命令基类
│   │   ├── executor.py                # Git 命令执行器（安全封装）
│   │   ├── log.py                     # git log 增强
│   │   ├── branch.py                  # git branch 图形化管理
│   │   ├── merge.py                   # git merge 可视化
│   │   ├── rebase.py                  # git rebase 交互式
│   │   └── diff.py                    # git diff 高亮
│   │
│   ├── cli/                           # 命令行接口
│   │   ├── __init__.py
│   │   ├── main.py                    # 主入口: git-dit
│   │   ├── plugins.py                 # 插件注册与管理
│   │   └── interactive.py             # 交互式 shell (git-dit shell)
│   │
│   ├── plugins/                       # 插件系统（扩展所有 Git 命令）
│   │   ├── __init__.py
│   │   ├── builtin/                   # 内置插件
│   │   │   ├── __init__.py
│   │   │   ├── alias.py               # git alias 管理
│   │   │   ├── stash.py               # git stash 可视化
│   │   │   ├── tag.py                 # git tag 管理
│   │   │   ├── remote.py              # git remote 图形化
│   │   │   ├── submodule.py           # git submodule 管理
│   │   │   ├── bisect.py              # git bisect 可视化
│   │   │   ├── blame.py               # git blame 热力图
│   │   │   └── cherry_pick.py         # git cherry-pick 交互式
│   │   │
│   │   └── custom/                    # 用户自定义插件目录
│   │
│   ├── interactive/                   # 交互式 TUI 界面
│   │   ├── __init__.py
│   │   ├── app.py                     # Textual 或 urwid 主应用
│   │   ├── widgets/                   # 自定义组件
│   │   │   ├── __init__.py
│   │   │   ├── graph_view.py          # 历史图组件
│   │   │   ├── branch_list.py         # 分支列表
│   │   │   ├── commit_detail.py       # 提交详情面板
│   │   │   └── command_palette.py     # 命令面板（Ctrl+P）
│   │   └── keybindings.py             # 快捷键配置
│   │
│   ├── utils/                         # 工具集
│   │   ├── __init__.py
│   │   ├── git.py                     # Git 仓库检测与低级操作
│   │   ├── formatting.py              # 颜色、表格、符号格式化
│   │   ├── config.py                  # 配置文件管理 (~/.git-dit/config.toml)
│   │   └── exceptions.py              # 自定义异常
│   │
│   └── vendor/                        # 可选： vendored 依赖
│       └── git_exec.py                # 嵌入式 Git 执行（极端环境）
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # pytest fixtures
│   ├── unit/
│   │   ├── test_history.py
│   │   ├── test_parser.py
│   └── integration/
│       ├── test_cli.py
│       └── test_interactive.py
│
├── scripts/
│   ├── dev_setup.sh                 # 开发环境初始化
│   ├── release.py                   # 自动发布脚本
│   └── benchmark.py                 # 性能测试
│
├── docs/
│   ├── index.md
│   ├── commands.md                  # 所有支持的 Git 命令文档
│   ├── plugins.md                   # 插件开发指南
│   └── api/
│       └── git_dit.rst
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
│
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── test.txt
│
├── pyproject.toml                   # 现代 Python 配置中心
├── .pre-commit-config.yaml
├── .gitignore
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── Dockerfile
```

---

## 🎯 核心设计思路

### 1. **插件化架构**（整合所有 Git 命令）
```python
# src/git_dit/plugins/builtin/stash.py
from git_dit.commands.base import GitCommand

class StashPlugin(GitCommand):
    name = "stash"
    description = "可视化 stash 管理"
    
    def execute(self, args):
        # 1. 执行 git stash list
        # 2. 解析输出
        # 3. 用 ASCII 绘制 stash 栈
        # 4. 支持交互式 apply/pop
        pass

# 自动注册
PLUGINS = [StashPlugin, TagPlugin, ...]
```

**优势**：每个 Git 子命令封装为独立插件，可插拔、易扩展。

### 2. **双层 CLI 接口**
```bash
# 1. 快速命令: git-dit log --oneline --graph
git-dit <command> [options]

# 2. 交互式模式: 进入全屏 TUI
git-dit shell
# 内置命令面板，支持所有 Git 操作（类似 lazygit）
```

**融合方式**：
- `git-dit log` → 调用 `commands/log.py` → 增强的 ASCII 图
- `git-dit branch` → 调用 `plugins/builtin/branch.py` → 可视化分支管理
- `git-dit remote add` → 透传原生 Git 但增加可视化确认

### 3. **智能命令分发**
```python
# src/git_dit/cli/main.py
def main():
    args = sys.argv[1:]
    
    # 先检查是否为 git-dit 内置命令
    if args[0] in BUILTIN_COMMANDS:
        dispatch_to_plugin(args[0], args[1:])
    else:
        # 未识别命令 → 透传给原生 Git
        # git-dit commit -m "msg" → git commit -m "msg"
        pass_to_git(args)
```

---

## 🔧 `pyproject.toml` 关键配置

```toml
[project]
name = "git-dit"
version = "1.0.0"
description = "Git 命令的图形化增强中心"
dependencies = [
    "click>=8.0",           # CLI 框架
    "gitpython>=3.1",       # Git 操作（备选）
    "rich>=13.0",           # 终端美化
    "textual>=0.41",        # 交互式 TUI
    "toml>=0.10",           # 配置解析
    "typing-extensions>=4.5",
]

[project.optional-dependencies]
full = [
    "pygit2>=1.13",         # 高性能 Git 操作（可选）
    "watchdog>=3.0",        # 文件监听（实时刷新）
]

[project.scripts]
git-dit = "git_dit.cli.main:main"
# 可选：创建 git 别名，实现 git dit log
git-dit-alias = "git_dit.cli.alias:install_alias"  

[tool.git_dit]
# 自定义配置段
default_graph_style = "unicode"  # ascii 或 unicode
interactive_theme = "dark"
auto_refresh = true
```

---

## 📦 核心功能模块

| 模块 | 职责 | 关键技术 |
|------|------|----------|
| `core/history.py` | 生成 ASCII/Unicode 提交图 | 自定义布局算法 |
| `commands/executor.py` | 安全执行 Git 命令 | `subprocess` + 超时控制 |
| `plugins/` | 扩展所有 Git 子命令 | 插件注册表 + 动态加载 |
| `interactive/` | 全屏交互式界面 | Textual (Rich) |
| `utils/git.py` | Git 仓库状态检测 | `git rev-parse --git-dir` |

---

## 🚀 使用示例

```bash
# 安装
pip install git-dit[full]

# 1. 图形化 log（核心功能）
git-dit log --oneline --all --graph

# 2. 交互式分支管理（插件）
git-dit branch --interactive

# 3. 可视化 stash 栈
git-dit stash list

# 4. 进入全能交互模式（整合所有命令）
git-dit shell
# 在 TUI 内按 'p' 打开命令面板，输入任何 Git 命令

# 5. 原生 Git 透传（未识别命令自动转发）
git-dit commit -a -m "feat: add new feature"

# 6. 插件扩展
git-dit plugin install git-dit-jira  # 第三方插件
```

---

## ✅ 设计亮点

1. **100% Git 命令覆盖**：内置插件 + 原生透传，确保无功能缺失
2. **渐进式使用**：既可快速执行单命令，也可进入交互式环境
3. **可视化优先**：每个命令都增加图形化反馈
4. **插件生态**：社区可轻松扩展 `git-dit bisect` 等高级功能
5. **类型安全**：全程类型提示，mypy 严格模式
=======
## 📁 `git-dit` 完整项目结构

```
git-dit/                               # 项目根目录
├── src/git_dit/                       # 主包（使用 src 布局）
│   ├── __init__.py                    # 版本号: __version__ = "1.0.0"
│   ├── py.typed                       # 支持类型提示
│   │
│   ├── core/                          # 核心引擎
│   │   ├── __init__.py
│   │   ├── history.py                 # 历史图渲染引擎（ASCII/Unicode）
│   │   ├── parser.py                  # Git 输出解析器
│   │   └── models.py                  # 数据模型（Commit, Branch, Merge）
│   │
│   ├── commands/                      # Git 命令封装层
│   │   ├── __init__.py
│   │   ├── base.py                    # 命令基类
│   │   ├── executor.py                # Git 命令执行器（安全封装）
│   │   ├── log.py                     # git log 增强
│   │   ├── branch.py                  # git branch 图形化管理
│   │   ├── merge.py                   # git merge 可视化
│   │   ├── rebase.py                  # git rebase 交互式
│   │   └── diff.py                    # git diff 高亮
│   │
│   ├── cli/                           # 命令行接口
│   │   ├── __init__.py
│   │   ├── main.py                    # 主入口: git-dit
│   │   ├── plugins.py                 # 插件注册与管理
│   │   └── interactive.py             # 交互式 shell (git-dit shell)
│   │
│   ├── plugins/                       # 插件系统（扩展所有 Git 命令）
│   │   ├── __init__.py
│   │   ├── builtin/                   # 内置插件
│   │   │   ├── __init__.py
│   │   │   ├── alias.py               # git alias 管理
│   │   │   ├── stash.py               # git stash 可视化
│   │   │   ├── tag.py                 # git tag 管理
│   │   │   ├── remote.py              # git remote 图形化
│   │   │   ├── submodule.py           # git submodule 管理
│   │   │   ├── bisect.py              # git bisect 可视化
│   │   │   ├── blame.py               # git blame 热力图
│   │   │   └── cherry_pick.py         # git cherry-pick 交互式
│   │   │
│   │   └── custom/                    # 用户自定义插件目录
│   │
│   ├── interactive/                   # 交互式 TUI 界面
│   │   ├── __init__.py
│   │   ├── app.py                     # Textual 或 urwid 主应用
│   │   ├── widgets/                   # 自定义组件
│   │   │   ├── __init__.py
│   │   │   ├── graph_view.py          # 历史图组件
│   │   │   ├── branch_list.py         # 分支列表
│   │   │   ├── commit_detail.py       # 提交详情面板
│   │   │   └── command_palette.py     # 命令面板（Ctrl+P）
│   │   └── keybindings.py             # 快捷键配置
│   │
│   ├── utils/                         # 工具集
│   │   ├── __init__.py
│   │   ├── git.py                     # Git 仓库检测与低级操作
│   │   ├── formatting.py              # 颜色、表格、符号格式化
│   │   ├── config.py                  # 配置文件管理 (~/.git-dit/config.toml)
│   │   └── exceptions.py              # 自定义异常
│   │
│   └── vendor/                        # 可选： vendored 依赖
│       └── git_exec.py                # 嵌入式 Git 执行（极端环境）
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # pytest fixtures
│   ├── unit/
│   │   ├── test_history.py
│   │   ├── test_parser.py
│   └── integration/
│       ├── test_cli.py
│       └── test_interactive.py
│
├── scripts/
│   ├── dev_setup.sh                 # 开发环境初始化
│   ├── release.py                   # 自动发布脚本
│   └── benchmark.py                 # 性能测试
│
├── docs/
│   ├── index.md
│   ├── commands.md                  # 所有支持的 Git 命令文档
│   ├── plugins.md                   # 插件开发指南
│   └── api/
│       └── git_dit.rst
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
│
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── test.txt
│
├── pyproject.toml                   # 现代 Python 配置中心
├── .pre-commit-config.yaml
├── .gitignore
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── Dockerfile
```

---

## 🎯 核心设计思路

### 1. **插件化架构**（整合所有 Git 命令）
```python
# src/git_dit/plugins/builtin/stash.py
from git_dit.commands.base import GitCommand

class StashPlugin(GitCommand):
    name = "stash"
    description = "可视化 stash 管理"
    
    def execute(self, args):
        # 1. 执行 git stash list
        # 2. 解析输出
        # 3. 用 ASCII 绘制 stash 栈
        # 4. 支持交互式 apply/pop
        pass

# 自动注册
PLUGINS = [StashPlugin, TagPlugin, ...]
```

**优势**：每个 Git 子命令封装为独立插件，可插拔、易扩展。

### 2. **双层 CLI 接口**
```bash
# 1. 快速命令: git-dit log --oneline --graph
git-dit <command> [options]

# 2. 交互式模式: 进入全屏 TUI
git-dit shell
# 内置命令面板，支持所有 Git 操作（类似 lazygit）
```

**融合方式**：
- `git-dit log` → 调用 `commands/log.py` → 增强的 ASCII 图
- `git-dit branch` → 调用 `plugins/builtin/branch.py` → 可视化分支管理
- `git-dit remote add` → 透传原生 Git 但增加可视化确认

### 3. **智能命令分发**
```python
# src/git_dit/cli/main.py
def main():
    args = sys.argv[1:]
    
    # 先检查是否为 git-dit 内置命令
    if args[0] in BUILTIN_COMMANDS:
        dispatch_to_plugin(args[0], args[1:])
    else:
        # 未识别命令 → 透传给原生 Git
        # git-dit commit -m "msg" → git commit -m "msg"
        pass_to_git(args)
```

---

## 🔧 `pyproject.toml` 关键配置

```toml
[project]
name = "git-dit"
version = "1.0.0"
description = "Git 命令的图形化增强中心"
dependencies = [
    "click>=8.0",           # CLI 框架
    "gitpython>=3.1",       # Git 操作（备选）
    "rich>=13.0",           # 终端美化
    "textual>=0.41",        # 交互式 TUI
    "toml>=0.10",           # 配置解析
    "typing-extensions>=4.5",
]

[project.optional-dependencies]
full = [
    "pygit2>=1.13",         # 高性能 Git 操作（可选）
    "watchdog>=3.0",        # 文件监听（实时刷新）
]

[project.scripts]
git-dit = "git_dit.cli.main:main"
# 可选：创建 git 别名，实现 git dit log
git-dit-alias = "git_dit.cli.alias:install_alias"  

[tool.git_dit]
# 自定义配置段
default_graph_style = "unicode"  # ascii 或 unicode
interactive_theme = "dark"
auto_refresh = true
```

---

## 📦 核心功能模块

| 模块 | 职责 | 关键技术 |
|------|------|----------|
| `core/history.py` | 生成 ASCII/Unicode 提交图 | 自定义布局算法 |
| `commands/executor.py` | 安全执行 Git 命令 | `subprocess` + 超时控制 |
| `plugins/` | 扩展所有 Git 子命令 | 插件注册表 + 动态加载 |
| `interactive/` | 全屏交互式界面 | Textual (Rich) |
| `utils/git.py` | Git 仓库状态检测 | `git rev-parse --git-dir` |

---

## 🚀 使用示例

```bash
# 安装
pip install git-dit[full]

# 1. 图形化 log（核心功能）
git-dit log --oneline --all --graph

# 2. 交互式分支管理（插件）
git-dit branch --interactive

# 3. 可视化 stash 栈
git-dit stash list

# 4. 进入全能交互模式（整合所有命令）
git-dit shell
# 在 TUI 内按 'p' 打开命令面板，输入任何 Git 命令

# 5. 原生 Git 透传（未识别命令自动转发）
git-dit commit -a -m "feat: add new feature"

# 6. 插件扩展
git-dit plugin install git-dit-jira  # 第三方插件
```

---

## ✅ 设计亮点

1. **100% Git 命令覆盖**：内置插件 + 原生透传，确保无功能缺失
2. **渐进式使用**：既可快速执行单命令，也可进入交互式环境
3. **可视化优先**：每个命令都增加图形化反馈
4. **插件生态**：社区可轻松扩展 `git-dit bisect` 等高级功能
5. **类型安全**：全程类型提示，mypy 严格模式
>>>>>>> 50e3cca1cfe181572fa4b4ab62a676af7b5e083d
