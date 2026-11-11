"""数据库连接配置。

优先读取环境变量（MYSQL_HOST / MYSQL_PORT / MYSQL_USER / MYSQL_PASSWORD），
未设置时回退到下面的默认值。请勿把真实密码提交到仓库。
"""
import os

DB_CONFIG = {
    'host': os.environ.get('MYSQL_HOST', 'localhost'),
    'port': int(os.environ.get('MYSQL_PORT', '3306')),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'passwd': os.environ.get('MYSQL_PASSWORD', 'your_password_here'),
    'charset': 'utf8',
}
