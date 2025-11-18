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

import subprocess
import prompt_toolkit

class MainMenuNavigation:
    def __init__(self):
        pass
    
    def main(self):
        print("+---------------------------------------------+")
        print("|               Git-DIT > 主菜单              |")
        print("+---------------------------------------------+")
        print(f"| {option[0]}                             |")
        print(f"| {option[1]}                             |")
        print(f"| {option[2]}                           |")
        print(f"| {option[3]}                             |")
        print(f"| {option[4]}                             |")
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

    def select_option():
        # 当前选中的索引
        selected_index = 0
    
        # 创建自定义样式
        style = Style.from_dict({
            'highlight': 'bg:#00aa00 #ffffff bold',
            'normal': '#ansigray',
        })

        # 创建键绑定
        kb = KeyBindings()
        
        @kb.add('up')
        def move_up(event):
            nonlocal selected_index
            selected_index = (selected_index - 1) % len(options)
        
        @kb.add('down')
        def move_down(event):
            nonlocal selected_index
            selected_index = (selected_index + 1) % len(options)
        
        @kb.add('enter')
        def select(event):
            event.app.exit(result=selected_index)

    # 构建显示文本
    def get_formatted_text():
        result = []
        for i, option in enumerate(options):
            if i == selected_index:
                result.append(HTML(f'<highlight>▶ {option}</highlight>\n'))
            else:
                result.append(HTML(f'<normal>  {option}</normal>\n'))
        return result

if __name__ == "__main__":
    menu = MainMenuNavigation()
    menu.main()
    option = ["1.仓库状态查看", "2.文件操作管理", "3.分支与提交历史", "4.远程仓库操作", "5.直接命令输入"]