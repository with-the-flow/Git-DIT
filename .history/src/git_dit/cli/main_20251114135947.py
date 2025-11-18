# """git-dit CLI 主入口（最小实现）。"""
# import argparse
# import sys

# def main(argv=None) -> int:
#     argv = argv or sys.argv[1:]
#     parser = argparse.ArgumentParser(prog="git-dit", description="git-dit: visualize git history in terminal")
#     parser.add_argument("--version", action="store_true", help="show version")
#     args = parser.parse_args(argv)
#     if args.version:
#         try:
#             from git_dit import __version__
#             print(__version__)
#         except Exception:
#             print("unknown")
#         return 0
#     # 默认行为：展示帮助
#     parser.print_help()
#     return 0

# if __name__ == "__main__":
#     raise SystemExit(main())

"""
+---------------------------------------------+ 
| Git-DIT Terminal UI | | 
| | A simple and powerful ASCII-based Git client | 
| for your terminal environment. | | 
| | Current Repository: [未初始化] | 
| Git Version: 2.37.1 ✓ | | 
| | Press [ENTER] to begin... | 
+---------------------------------------------+
"""
try:
    # The GitPython package is installed from pip as "GitPython",
    # but the importable module name is "git" (lowercase). Prefer that.
    import git as GitPython
except Exception:
    # Fall back to trying the `GitPython` name (older/alternate setups),
    # and finally provide a minimal fallback so the UI can still run.
    try:
        import GitPython
    except Exception:
        class GitPython:
            __version__ = "unknown"

print("+---------------------------------------------+")
print("|             Git-DIT Terminal UI             |")
print("| A simple and powerful ASCII-based Git client|")
print("| for your terminal environment.              |")
print("| Current Repository: [未初始化]               |")
print(f"| Git Version: {GitPython.__version__} |")
print("| Press [ENTER] to begin... |")
print("+---------------------------------------------+")

input()  # 等待用户按下回车键

# # 查看解释器的位置
# import sys
# print(sys.executable)
# # 查看 sys.path 路径
# print(sys.path)
