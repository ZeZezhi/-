# ZeZezhi-学号-第二次人工智能编程作业

仓库链接: https://github.com/ZeZezhi/-.git

## 1. 任务描述与 AI 协作过程

在编写本程序前，我将作业要求完整提供给 AI（Claude Code），由 AI 完成整体架构设计和代码编写。

- **阶段 1**：AI 分析作业文档，读取学生名单文件，确定三模块架构（student.py / exam_system.py / main.py）。
- **阶段 2**：AI 依次编写 Student 类、ExamSys 基础框架、各功能方法。
- **阶段 3**：AI 进行端到端测试，修复 Windows 终端 GBK 编码兼容性问题（将 Unicode 符号替换为 ASCII 安全字符）。
- **阶段 4**：AI 初始化 Git 仓库，按功能增量提交，生成 README。

## 2. 核心 Prompt 修改记录

**初始 Prompt**：请根据作业要求完成 Python 程序开发。

**AI 初始生成的问题**：
- 使用了 `✔` 和 `⚠` 等 Unicode 符号，在 Windows GBK 终端下抛出 `UnicodeEncodeError`
- 菜单分隔线长度与作业要求不完全一致

**优化后的 Prompt（追加）**：要求将 Unicode 符号替换为 ASCII 安全替代字符，调整菜单分隔线格式为 74 个短横线。

## 3. Debug 与异常处理记录

**问题**：程序运行时报 `UnicodeEncodeError: 'gbk' codec can't encode character '✔'`

**原因**：Windows 中文终端默认使用 GBK 编码，无法编码 Unicode 重号字符（✔）和警告符号（⚠）。

**解决过程**：
1. 观察到 Traceback 指向 print 语句中的 `✔` 字符
2. 将 `✔` 全部替换为 `[OK]`，`⚠` 全部替换为 `[!]`
3. 将菜单分隔线 `+------------------------------------------` 调整为 `+` + `-` * 74
4. 重新运行测试，确认所有功能正常，编码问题解决

## 4. 人工代码审查 (Code Review)

以下是对 `random_roll_call` 方法的审查：

```python
def random_roll_call(self):
    """
    随机抽取不重复学生进行点名。
    try-except 三层异常保护：非整数输入 / 数量≤0 / 超过学生总数。
    """
    try:
        count_str = input("请输入要随机点名的学生数量：").strip()
        count = int(count_str)          # 可能抛出 ValueError

        if count <= 0:                  # 边界条件 1：数量 <= 0
            print("[!] 点名数量必须大于 0，请重新输入！")
            return

        if count > len(self.students):  # 边界条件 2：超过学生总数
            print(f"[!] 点名数量（{count}）超过了学生总人数（{len(self.students)}），请重新输入！")
            return

    except ValueError:                  # 异常捕获：非整数输入（如 "abc"）
        print("[!] 输入不合法！请确保输入的是一个整数。")
        return

    selected = random.sample(self.students, count)  # 不重复随机抽样

    print("\n===== 随机点名结果 =====")
    for i, student in enumerate(selected, start=1):
        print(f"{i}. {student.name}\t{student.student_id}")
    print("========================")
```

**审查结论**：
- `try-except` 放置在正确的位置，能够有效捕获 `int()` 转换时的 `ValueError`
- 两个边界条件（<=0 和 >总数）在 `try` 块内部进行判断，逻辑正确
- `random.sample()` 保证不重复抽样，语义清晰
- 错误提示均为中文，对用户友好
- 代码结构清晰，异常处理和正常逻辑分离良好
