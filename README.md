# Student-manager

基于 Python Tkinter + MySQL 的桌面学生信息管理系统，支持用户注册登录、学生信息新增与按姓名/学号/年龄多条件组合搜索。

## 功能特性

- 用户注册与登录，登录账号存于 MySQL `login_table`（密码以明文存储，详见配置与安全说明）
- 学生信息新增（`show_add_dialog`）
- 学生列表加载与展示（`load_students`）
- 多条件组合搜索（`search_students`）：姓名、学号使用 `LIKE` 模糊匹配，年龄为精确匹配，条件以 `AND` 组合
- 程序启动时自动创建数据库 `student_manage` 及 `login_table`、`info_table` 两张表，无需手动建库建表
- Tkinter 桌面界面，连接参数集中在 `config.py` 并支持环境变量覆盖

## 技术栈与依赖

- Python 3、Tkinter（图形界面，随 Python 自带）、PyMySQL==1.0.2
- MySQL 5.7+（需本机或可访问的 MySQL 服务，账号需具备建库权限）
- 第三方依赖见 `Student-management-system/requirements.txt`：pymysql==1.0.2

## 目录结构

```text
Student-manager/
├── README.md                          # 项目完整说明（GitHub 仓库首页展示）
├── LICENSE                            # MIT 许可证
├── .gitignore
└── Student-management-system/         # 实际项目代码所在子目录
    ├── run.py                         # 程序入口
    ├── config.py                      # 数据库连接配置 DB_CONFIG
    ├── requirements.txt               # pymysql==1.0.2
    ├── setup.py                       # 占位文件（内容为空）
    ├── README.md                      # 内层简短指引
    ├── LICENSE.txt                    # 子目录许可证
    ├── doc/
    │   ├── database.png               # 数据库相关截图
    │   └── main_page.png              # 主界面截图
    └── src/
        └── student_management.py      # 主程序：界面与数据库业务逻辑
```

## 快速开始

先确保 MySQL 5.7+ 已安装并启动，然后：

```bash
git clone https://github.com/RockyproJiang/Student-manager.git
cd Student-manager/Student-management-system
pip install -r requirements.txt
python run.py
```

## 配置与安全说明

- 数据库连接参数位于 `config.py` 的 `DB_CONFIG`，支持环境变量覆盖：`MYSQL_HOST`、`MYSQL_PORT`、`MYSQL_USER`、`MYSQL_PASSWORD`。
- **不要把真实密码写进代码或提交仓库**；密码请通过 `MYSQL_PASSWORD` 环境变量提供，并使用最小权限的数据库账号。
- 程序启动会自动创建数据库 `student_manage` 与 `login_table`（登录用户表）、`info_table`（学生信息表）。
- **安全说明（重要）**：登录密码以**明文**存于 `login_table.st_password`，登录时以明文比对，仅用于本地学习演示，**切勿用于生产环境、不要使用真实密码**。正式使用应改为加盐哈希（如 bcrypt / argon2），并使用最小权限数据库账号与参数化查询。
- 子目录 `Student-management-system/README.md` 仅提供简短运行指引，完整文档以仓库根目录的本文件为准。

## 许可证

本项目采用 MIT 许可证，详见 LICENSE（子目录另附 LICENSE.txt）。
