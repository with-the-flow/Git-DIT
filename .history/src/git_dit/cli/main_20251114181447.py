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
        import main_menu_navigation
        main_menu_navigation.main()
    except Exception as e:
        print(f"Error: {e}")
        print("Exiting...")