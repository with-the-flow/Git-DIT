# 界面
"""
+---------------------------------------------+ 
| Git-DIT > 主菜单 | 
+---------------------------------------------+ 
| 仓库状态查看 | 
| 文件操作管理 | 
| 分支与提交历史 | 
| 远程仓库操作 | 
| 直接命令输入 | | 
| | [S] 设置 [H] 帮助 [Q] 退出 | 
+----------------------------------------------+
"""

import GitPython

class MainMenuNavigation:
    def __init__(self):
        pass
    
    def main(self):
        print("+---------------------------------------------+")
        print("|               Git-DIT > 主菜单              |")
        print("+---------------------------------------------+")
        print("| 1. 仓库状态查看                             |")
        print("| 2. 文件操作管理                             |")
        print("| 3. 分支与提交历史                           |")
        print("| 4. 远程仓库操作                             |")
        print("| 5. 直接命令输入                             |")
        print("|                                             |")
        print("| [S] 设置  [H] 帮助  [Q] 退出                |")
        print("+---------------------------------------------+")
        
        choice = input("")
        print(f"您选择了: {choice}")
        # 在这里可以添加更多的逻辑来处理用户的选择
        if choice == "1":
            print("仓库状态查看")
        elif choice == "2":
            print("文件操作管理")
        elif choice == "3":
            print("分支与提交历史")
        elif choice == "4":
            print("远程仓库操作")
        elif choice == "5":
            print("直接命令输入")
        elif choice == "S":
            print("设置")
        elif choice == "H":
            print("帮助")
        elif choice == "Q":
            print("退出")
        else:
            print("没有这个选项")

if __name__ == "__main__":
    menu = MainMenuNavigation()
    menu.main()