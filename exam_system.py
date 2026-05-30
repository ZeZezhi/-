"""
exam_system.py —— 考试系统模块
定义 ExamSys 类，封装学生信息管理系统的全部核心功能。
"""

import os

from student import Student


class ExamSys:
    """学生信息与考试管理系统。"""

    def __init__(self, student_file: str):
        self.students: list[Student] = []
        self.student_file = student_file
        self.exam_seats: list[tuple] = []
        self.load_students()

    def load_students(self):
        """从学生名单文件读取数据并创建 Student 对象列表。"""
        if not os.path.exists(self.student_file):
            print(f"[!] 文件不存在: {self.student_file}")
            return

        with open(self.student_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines[1:]:  # 跳过标题行
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 6:
                continue
            student = Student(
                index=int(parts[0]), name=parts[1], gender=parts[2],
                class_name=parts[3], student_id=parts[4], college=parts[5],
            )
            self.students.append(student)

        print(f"[OK] 已成功加载 {len(self.students)} 名学生的信息。")

    def run(self):
        """主控制循环。"""
        if not self.students:
            print("系统中没有学生数据，无法运行。")
            return

        while True:
            self._print_menu()
            choice = input("请输入功能编号：").strip()

            if choice == "0":
                print("感谢使用，系统已退出。再见！")
                break
            elif choice == "1":
                self.find_student()
            elif choice == "2":
                self.random_roll_call()
            elif choice == "3":
                self.generate_exam_arrangement()
            elif choice == "4":
                self.generate_admission_tickets()
            else:
                print("[!] 功能编号不存在，请输入正确的功能编号（0~4）！")

    def _print_menu(self):
        """打印功能菜单。"""
        print()
        print("===== 学生信息与考试安排系统 =====")
        print("1. 查询学生信息")
        print("2. 随机点名")
        print("3. 生成考试安排表")
        print("4. 生成准考证文件")
        print("+" + "-" * 74)
        print("0. 退出系统")

    def find_student(self):
        """根据学号查询并显示学生信息，学号不存在时给出友好提示。"""
        student_id = input("请输入要查询的学生学号：").strip()

        for student in self.students:
            if student.student_id == student_id:
                print("\n[OK] 查询结果：")
                print(student)
                return

        print(f"[!] 未找到学号为「{student_id}」的学生，请检查学号是否输入正确！")

    def random_roll_call(self):
        """随机点名（待实现）。"""
        pass

    def generate_exam_arrangement(self):
        """生成考试安排表（待实现）。"""
        pass

    def generate_admission_tickets(self):
        """生成准考证文件（待实现）。"""
        pass
