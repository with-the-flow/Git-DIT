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
import subprocess

def get_git_version():
    try:
        # 执行git version命令
        result = subprocess.run(
            ["git", "version"], 
            capture_output=True, 
            text=True, 
            check=True  # 如果命令失败会抛出异常
        )
        
        # 获取输出并去除首尾空白（如"git version 2.50.1.windows.1"）
        version_output = result.stdout.strip()
        
        # 移除"git version "前缀
        version = version_output.replace("git version ", "")
        
        # 提取主要版本号（如"2.50.1"）
        # 按'.'分割，取前三个部分
        version_parts = version.split('.')
        if len(version_parts) >= 3:
            return '.'.join(version_parts[:3])
        
        return version  # 如果格式不符合预期，返回原始版本
        
    except Exception:
        return "unknown"

# 获取版本号
version = get_git_version()

print("+---------------------------------------------+")
print("|             Git-DIT Terminal UI             |")
print("| A simple and powerful ASCII-based Git client|")
print("| for your terminal environment.              |")
print(f"| Git Version: {version} |")
print("| Press [ENTER] to begin...                  |")
print("+---------------------------------------------+")

users_input = input()  # 等待用户按下回车键

if users_input == "":
    print("Starting Git-DIT...")
    print("Try to return Navigation Interface...")
    try:
        from .command.main_menu_navigation import main
        main()
        pass
    except Exception as e:
        print(f"Error: {e}")
        print("Exiting...")