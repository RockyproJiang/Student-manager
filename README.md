[README.md](https://github.com/user-attachments/files/24157700/README.md)
# 学生管理系统 (Student Management System)

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![MySQL](https://img.shields.io/badge/database-MySQL-orange)

一个基于 Python 和 MySQL 的学生信息管理系统，使用 Tkinter 构建图形界面。

## 功能特性

- ✅ 用户注册和登录系统
- ✅ 学生信息的增删改查
- ✅ 多条件搜索和筛选
- ✅ 美观的用户界面
- ✅ MySQL 数据库支持
- ✅ 右键菜单操作
- ✅ 数据导出功能

## 界面预览

![登录界面](docs/screenshots/login.png)
![主界面](docs/screenshots/main.png)

## 系统要求

- Python 3.7 或更高版本
- MySQL 5.7 或更高版本
- Tkinter（通常随 Python 安装）

## 安装步骤

### 1. 克隆仓库
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
2. 安装 Python 依赖
bash
pip install -r requirements.txt
3. 安装 MySQL
Windows: 下载并安装 MySQL Installer

macOS: brew install mysql

Ubuntu/Debian: sudo apt-get install mysql-server

4. 配置数据库
启动 MySQL 服务

编辑配置文件：

bash
cp config.py.example config.py
修改 config.py 中的数据库配置：

python
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'your_password_here',
    'charset': 'utf8mb4'
}
5. 运行程序
bash
# 方式一：直接运行主程序
python src/student_management.py

# 方式二：使用启动脚本
python run.py

# 方式三：双击运行（Windows）
双击 run.pyw（无控制台窗口）
使用方法
注册账号
首次运行程序会显示登录界面

点击"注册账号"按钮

输入用户名和密码（用户名至少3字符，密码至少4字符）

点击"注册"完成

登录系统
输入注册的用户名和密码

点击"登录系统"或按回车键

管理学生信息
添加学生：点击工具栏的"＋ 添加学生"按钮

搜索学生：使用姓名、学号、年龄进行搜索

编辑学生：双击表格行或右键选择"编辑"

删除学生：右键选择"删除"

刷新数据：点击"刷新"按钮或右键菜单

导出数据
在主界面右键点击表格

选择"导出数据"

选择导出格式（CSV/Excel）

选择保存位置

数据库结构
用户表 (login_table)
字段名	类型	说明
id	INT	主键，自增
st_username	VARCHAR(50)	用户名，唯一
st_password	VARCHAR(255)	密码
created_at	TIMESTAMP	创建时间
学生信息表 (info_table)
字段名	类型	说明
id	INT	主键，自增
student_name	VARCHAR(50)	学生姓名
student_id	VARCHAR(20)	学号，唯一
student_age	INT	年龄
created_at	TIMESTAMP	创建时间
