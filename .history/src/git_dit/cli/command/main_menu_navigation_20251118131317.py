import subprocess
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl

class MainMenuNavigation:
    def __init__(self):
        self.options = [
            "仓库状态查看",
            "文件操作管理", 
            "分支与提交历史",
            "远程仓库操作",
            "直接命令输入"
        ]
    
    def select_option_interactive(self):
        """交互式选择菜单 - 渲染完整边框界面"""
        selected_index = 0
        
        # 创建自定义样式：标题不使用蓝色背景，高亮只改变文字为绿色，键提示保持白色
        style = Style.from_dict({
            'border': '#ansiblue',
            'title': '#ffffff bold',
            'highlight': '#00aa00 bold',
            'normal': '#ansigray',
            'keyhint': '#ffffff',
        })
        
        # 创建键绑定
        kb = KeyBindings()
        
        @kb.add('up')
        def move_up(event):
            nonlocal selected_index
            selected_index = (selected_index - 1) % len(self.options)
            event.app.invalidate()
        
        @kb.add('down')
        def move_down(event):
            nonlocal selected_index
            selected_index = (selected_index + 1) % len(self.options)
            event.app.invalidate()
        
        @kb.add('enter')
        def select(event):
            event.app.exit(result=selected_index)
        
        @kb.add('c-c')
        @kb.add('c-d')
        def exit_(event):
            event.app.exit(result=None)
        
        # 构建完整的带边框菜单文本
        def get_formatted_text():
            # 构建边框和标题
            fragments = [
                ('class:border', '+---------------------------------------------+\n'),
                ('class:title',  '|               Git-DIT > 主菜单              |\n'),
                ('class:border', '+---------------------------------------------+\n'),
            ]
            
            # 构建选项列表
            for i, option in enumerate(self.options):
                if i == selected_index:
                    # 高亮当前选中项
                    fragments.append(('class:highlight', f'| ▶ {i+1}. {option:<40} |\n'))
                else:
                    fragments.append(('class:normal', f'|   {i+1}. {option:<40} |\n'))
            
            # 构建底部提示
            fragments.extend([
                ('class:border', '|                                             |\n'),
                ('class:keyhint', '| [S] 设置  [H] 帮助  [Q] 退出                |\n'),
                ('class:border', '+---------------------------------------------+\n'),
                ('', '\n请使用↑↓方向键选择，回车确认...'),
            ])
            
            return fragments
        
        # 创建应用
        control = FormattedTextControl(get_formatted_text)
        window = Window(content=control, wrap_lines=False)  # 禁用自动换行保持边框整齐
        layout = Layout(window)
        
        app = Application(
            layout=layout,
            key_bindings=kb,
            style=style,
            mouse_support=False,
            full_screen=False,
        )
        
        return app.run()
    
    def main(self):
        # 直接启动交互式菜单，不再单独打印静态菜单
        selected = self.select_option_interactive()
        
        if selected is not None:
            print(f"\n您选择了: {self.options[selected]}")
            self.handle_selection(selected)
        else:
            print("\n操作被取消")
    
    def handle_selection(self, index):
        """处理用户选择"""
        actions = {
            0: self.check_repo_status,
            1: self.manage_files,
            2: self.view_branches,
            3: self.remote_operations,
            4: self.direct_command,
        }
        
        action = actions.get(index)
        if action:
            action()
    
    # 示例方法
    def check_repo_status(self): print("正在执行：仓库状态查看")
    def manage_files(self): print("正在执行：文件操作管理")
    def view_branches(self): print("正在执行：分支与提交历史")
    def remote_operations(self): print("正在执行：远程仓库操作")
    def direct_command(self): print("正在执行：直接命令输入")

if __name__ == "__main__":
    menu = MainMenuNavigation()
    menu.main()