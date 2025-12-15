#!/usr/bin/env python3
"""
学生管理系统启动脚本
"""

import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from student_management import Student_man_sys

if __name__ == "__main__":
    print("正在启动学生管理系统...")
    app = Student_man_sys()
    app.run()