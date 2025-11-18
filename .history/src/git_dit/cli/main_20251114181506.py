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
    import GitPython
except ImportError:
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

users_input = input()  # 等待用户按下回车键

# # 查看解释器的位置
# import sys
# print(sys.executable)
# # 查看 sys.path 路径
# print(sys.path)

if users_input == "":
    print("Starting Git-DIT...")
    print("Try to return Navigation Interface...")
    try:
        # Prefer package-relative import when running as a package
        from .command import main_menu_navigation
    except Exception:
        try:
            # Try absolute package import (when run from project root)
            from git_dit.cli.command import main_menu_navigation
        except Exception:
            # Fallback: import by file path (works when running as a script)
            import importlib.util
            import os
            module_path = os.path.join(os.path.dirname(__file__), "command", "main_menu_navigation.py")
            spec = importlib.util.spec_from_file_location("git_dit.cli.command.main_menu_navigation", module_path)
            if spec and spec.loader:
                main_menu_navigation = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(main_menu_navigation)
            else:
                raise ImportError(f"Cannot import main_menu_navigation from {module_path}")

    try:
        # Module-level main() is provided in the command module
        main_menu_navigation.main()
    except Exception as e:
        print(f"Error launching navigation: {e}")
        print("Exiting...")