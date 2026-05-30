"""
main.py —— 程序入口模块
创建 ExamSys 实例并启动系统主控制循环。
"""

import os
import sys

from exam_system import ExamSys


def main():
    """
    程序主入口函数。
    1. 定位学生名单文件（默认为程序所在目录下的「人工智能编程语言学生名单.txt」）
    2. 创建 ExamSys 实例
    3. 启动交互式菜单循环
    """
    # 学生名单文件路径：默认与 main.py 位于同一目录
    student_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "人工智能编程语言学生名单.txt"
    )

    # 如果默认路径不存在，尝试在上级目录和桌面查找
    if not os.path.exists(student_file):
        # 尝试当前工作目录
        alt_path = "人工智能编程语言学生名单.txt"
        if os.path.exists(alt_path):
            student_file = alt_path
        else:
            print("[!] 未找到「人工智能编程语言学生名单.txt」文件。")
            print("  请将该文件复制到程序所在目录后重新运行。")
            sys.exit(1)

    # 创建考试系统实例并启动
    exam_sys = ExamSys(student_file)
    exam_sys.run()


if __name__ == "__main__":
    main()
