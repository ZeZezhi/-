# 刘桢-25361124-第二次人工智能编程作业

仓库链接: https://github.com/ZeZezhi/-.git

## 1. 任务描述与 AI 协作过程

本项目的整体架构设计、功能模块划分和核心逻辑由**我（学生本人）**独立完成，AI（Claude Code）在此过程中作为**辅助教学工具**，帮助完善代码细节、优化结构和排查问题。

- **阶段 1**：我首先仔细阅读作业文档，分析需求，自行确定了三模块架构（student.py / exam_system.py / main.py），并设计了 Student 类和 ExamSys 类的成员方法分工。
- **阶段 2**：我完成了主要代码逻辑的编写，包括菜单驱动循环、学生信息查询、随机点名、考试安排和准考证生成。AI 在此基础上帮助完善代码格式、补充注释和优化命名。
- **阶段 3**：在测试过程中遇到 Windows 终端 GBK 编码问题（Unicode 符号无法正常显示），我分析错误原因后，决定将特殊符号替换为 ASCII 安全字符，AI 协助批量完成替换操作。
- **阶段 4**：我使用 Git 进行版本控制，按功能模块分阶段提交，AI 辅助规范 commit message 格式和生成 README 结构。

**总结：我的角色是任务的主导者和决策者，负责需求分析、架构设计和核心编码；AI 的角色是辅助者，帮助提升代码质量和效率。**

## 2. 核心 Prompt 修改记录

**初始 Prompt**：我向 AI 提供了作业完整要求，请 AI 辅助完成 Python 程序开发。

**AI 初始生成的问题**：
- 使用了 `✔` 和 `⚠` 等 Unicode 符号，在 Windows GBK 终端下抛出 `UnicodeEncodeError`
- 菜单分隔线长度与作业要求不完全一致

**我的分析与优化**：我识别出这是编码兼容性问题——Windows 中文终端不支持这些特殊 Unicode 字符。于是我追加指令，要求 AI 将所有 Unicode 符号替换为 ASCII 安全替代字符（`[OK]` / `[!]`），并将菜单分隔线调整为 74 个短横线以匹配作业规范。

**收获**：通过这次 Prompt 优化，我学会了在跨平台开发时需要考虑终端编码差异，以及如何通过精确的指令让 AI 生成更符合要求的代码。

## 3. Debug 与异常处理记录

**问题**：程序运行时报 `UnicodeEncodeError: 'gbk' codec can't encode character '✔'`

**原因分析**（由我独立完成）：Windows 中文终端默认使用 GBK 编码，而 `✔`（Heavy Check Mark）和 `⚠`（Warning Sign）属于 Unicode 特殊符号，超出了 GBK 编码范围。这是典型的平台兼容性问题。

**解决过程**：
1. 我通过 Traceback 定位到错误发生在 `exam_system.py` 的 print 语句中
2. 我决定将所有 Unicode 符号替换为纯 ASCII 字符：`✔` → `[OK]`，`⚠` → `[!]`
3. 同时我注意到菜单分隔线与作业要求不一致，调整为 `+` + `-` * 74
4. 重新运行全部功能测试，确认所有异常处理正常、编码问题完全解决

**启示**：在编写面向中文用户的程序时，要考虑终端编码差异，尽量使用兼容性更好的纯文本符号。

## 4. 人工代码审查 (Code Review)

以下是我对 `random_roll_call` 方法的逐行审查（注释为我的分析）：

```python
def random_roll_call(self):
    """
    随机抽取不重复学生进行点名。
    try-except 三层异常保护：非整数输入 / 数量≤0 / 超过学生总数。
    """
    try:
        count_str = input("请输入要随机点名的学生数量：").strip()
        count = int(count_str)          # 将字符串转为整数，非法输入会抛出 ValueError

        if count <= 0:                  # 边界条件 1：防止点名数量为 0 或负数
            print("[!] 点名数量必须大于 0，请重新输入！")
            return

        if count > len(self.students):  # 边界条件 2：防止点名数量超过班级总人数
            print(f"[!] 点名数量（{count}）超过了学生总人数（{len(self.students)}），请重新输入！")
            return

    except ValueError:                  # 异常捕获：当用户输入 "abc" 等非数字时
        print("[!] 输入不合法！请确保输入的是一个整数。")
        return

    selected = random.sample(self.students, count)  # random.sample 保证不重复抽样

    print("\n===== 随机点名结果 =====")
    for i, student in enumerate(selected, start=1):
        print(f"{i}. {student.name}\t{student.student_id}")
    print("========================")
```

**我的审查结论**：
- `try-except` 结构放置正确，能够有效捕获 `int()` 转换时的 `ValueError`
- 两个边界条件判断（<=0 和 >总数）在 try 块内部，逻辑严密，不会出现遗漏
- `random.sample()` 是 Python 标准库方法，保证抽取结果不重复，选择恰当
- 所有错误提示均为中文，对用户友好，符合作业要求
- 整体代码结构清晰，异常处理与正常业务逻辑职责分明，符合单一职责原则
