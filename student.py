"""
student.py —— 学生类模块
定义 Student 类，封装单个学生的基本信息和格式化输出方法。
"""


class Student:
    """学生类，用于存储和展示单个学生的详细信息。"""

    def __init__(self, index: int, name: str, gender: str, class_name: str,
                 student_id: str, college: str):
        """
        初始化学生对象。

        参数:
            index: 序号
            name: 姓名
            gender: 性别
            class_name: 班级
            student_id: 学号
            college: 学院
        """
        self.index = index          # 序号
        self.name = name            # 姓名
        self.gender = gender        # 性别
        self.class_name = class_name  # 班级
        self.student_id = student_id  # 学号
        self.college = college      # 学院

    def __str__(self) -> str:
        """返回学生信息的格式化字符串，用于屏幕输出。"""
        return (f"序号: {self.index}\t姓名: {self.name}\t性别: {self.gender}\t"
                f"班级: {self.class_name}\t学号: {self.student_id}\t学院: {self.college}")

    def to_arrangement_line(self, seat_number: int) -> str:
        """
        生成考试安排表中的一行记录。

        参数:
            seat_number: 考试座位号

        返回:
            格式为 "座位号,姓名,学号" 的字符串
        """
        return f"{seat_number},{self.name},{self.student_id}"

    def to_ticket_text(self, seat_number: int) -> str:
        """
        生成准考证文件的文本内容。

        参数:
            seat_number: 考试座位号

        返回:
            包含座位号、姓名、学号的多行文本
        """
        return f"考试座位号: {seat_number}\n姓名: {self.name}\n学号: {self.student_id}\n"
