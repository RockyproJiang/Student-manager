# Student-management-system

本目录是 Student-manager 项目的实际代码主体，此处仅提供简短运行指引；完整项目说明见仓库根目录的 `README.md`。

- 克隆地址：`https://github.com/RockyproJiang/Student-manager.git`
- 程序入口：`python run.py`（先执行 `pip install -r requirements.txt` 安装 pymysql==1.0.2，并确保 MySQL 5.7+ 已启动）。
- 业务主体位于 `src/`，即 `src/student_management.py`（Tkinter 界面与数据库操作，含用户注册登录、学生信息新增、列表加载与多条件搜索）。
- 数据库连接参数在 `config.py` 的 `DB_CONFIG`，支持 `MYSQL_HOST` / `MYSQL_PORT` / `MYSQL_USER` / `MYSQL_PASSWORD` 环境变量覆盖，请勿把真实密码提交到仓库。
- 主界面截图：`doc/main_page.png`；数据库相关截图：`doc/database.png`。

本子目录另含 `LICENSE.txt`，采用 MIT 许可证。
