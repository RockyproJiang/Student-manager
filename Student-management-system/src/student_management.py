import pymysql
import tkinter as tk
from tkinter import ttk, messagebox


class Student_man_sys:
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'passwd': '****',#换成自己的mysql账号密码
            'charset': 'utf8'
        }
        self.database_name = "student_manage"
        self.create_database()
        
        self.root = tk.Tk()  
        self.root.title("Student Manage System")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffffff")
        
        self.current_page = None
        self.login_page()

    def create_database(self):
        try:
            connection = pymysql.connect(
                host=self.db_config['host'],
                port=self.db_config['port'],
                user=self.db_config['user'],
                password=self.db_config['passwd'],
                charset=self.db_config['charset']
            )
            cursor = connection.cursor()
            
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database_name}")
            cursor.execute(f"USE {self.database_name}")
            
            # login table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS login_table (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    st_username VARCHAR(50) UNIQUE NOT NULL,
                    st_password VARCHAR(50) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # info table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS info_table (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    student_name VARCHAR(50) NOT NULL,
                    student_id VARCHAR(20) UNIQUE NOT NULL,
                    student_age INT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            connection.commit()
            cursor.close()
            connection.close()
            print("Database created successfully")
        except Exception as e:
            print(f"Failed to create database: {e}")
            messagebox.showerror("Database Error", f"Failed to create database: {e}")

    def get_connection(self):
        try:
            connection = pymysql.connect(
                host=self.db_config['host'],
                port=self.db_config['port'],
                user=self.db_config['user'],
                password=self.db_config['passwd'],
                database=self.database_name,
                charset=self.db_config['charset']
            )
            return connection
        except Exception as e:
            messagebox.showerror("Database Error", f"Unable to connect: {e}")
            return None

    def login_page(self):
        if self.current_page:
            self.current_page.destroy()
        
        self.current_page = tk.Frame(self.root, bg="#ffffff")
        self.current_page.pack(fill="both", expand=True)
        
        # title
        title_label = tk.Label(
            self.current_page,
            text="Student Manage System",
            font=("Microsoft YaHei", 24, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=30)
        
        # login frame
        login_frame = tk.Frame(self.current_page, bg='#f0f0f0')
        login_frame.pack(pady=50)
        
        # username
        username_label = tk.Label(
            login_frame,
            text="Username:",
            font=("Microsoft YaHei", 12),
            bg='#f0f0f0',
            fg='#333333'
        )
        username_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        
        self.username_entry = tk.Entry(
            login_frame,
            font=("Microsoft YaHei", 12),
            width=25
        )
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # password
        password_label = tk.Label(
            login_frame,
            text="Password:",
            font=("Microsoft YaHei", 12),
            bg='#f0f0f0',
            fg='#333333'
        )
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        
        self.password_entry = tk.Entry(
            login_frame,
            font=("Microsoft YaHei", 12),
            width=25,
            show="*"
        )
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # button frame
        button_frame = tk.Frame(self.current_page, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        # registration button
        register_btn = tk.Button(
            button_frame,
            text="Register",
            font=("Microsoft YaHei", 12, "bold"),
            bg='#2196F3',
            fg='white',
            width=10,
            height=2,
            command=self.register
        )
        register_btn.grid(row=0, column=0, padx=20)
        
        # login button
        login_btn = tk.Button(
            button_frame,
            text="Login",
            font=("Microsoft YaHei", 12, "bold"),
            bg='#f44336',
            fg='white',
            width=10,
            height=2,
            command=self.login
        )
        login_btn.grid(row=0, column=1, padx=20)

    def register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showwarning("Input Error", "Username or password shouldn't be empty")
            return
        
        connection = self.get_connection()
        if not connection:
            return
        
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM login_table WHERE st_username = %s",
                (username,)
            )
            existing_user = cursor.fetchone()
            
            if existing_user:
                messagebox.showinfo("Warning", "Username already exists")
            else:
                cursor.execute(
                    "INSERT INTO login_table (st_username, st_password) VALUES (%s, %s)",
                    (username, password)
                )
                connection.commit()
                messagebox.showinfo("Success", "Registration completed")
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to register: {e}")
        finally:
            cursor.close()
            connection.close()

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showwarning("Input Error", "Username or password shouldn't be empty")
            return
        
        connection = self.get_connection()
        if not connection:
            return
        
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM login_table WHERE st_username = %s AND st_password = %s",
                (username, password)
            )
            user = cursor.fetchone()
            
            if user:
                self.current_user = username
                self.query_page()
            else:
                messagebox.showerror("Error", "Wrong username or password")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to login: {e}")
        finally:
            cursor.close()
            connection.close()

    def query_page(self):
        if self.current_page:
            self.current_page.destroy()
        
        self.current_page = tk.Frame(self.root, bg='#f0f0f0')
        self.current_page.pack(fill='both', expand=True)
        
        # toolbar
        toolbar = tk.Frame(self.current_page, bg='#e0e0e0', height=50)
        toolbar.pack(fill='x', padx=10, pady=10)
        
        add_btn = tk.Button(
            toolbar,
            text="+ Add Data",
            font=("Microsoft YaHei", 11, "bold"),
            bg='#2196F3',
            fg='white',
            command=self.show_add_dialog
        )
        add_btn.pack(side='left', padx=10, pady=10)
        
        # table frame
        table_frame = tk.Frame(self.current_page, bg='#f0f0f0')
        table_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # create treeview
        columns = ('name', 'id', 'age')
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show='headings',
            height=15
        )
        
        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=200, anchor='center')
        
        # scrollbar
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side='right', fill='y')
        self.tree.pack(side='left', fill='both', expand=True)
        
        # search frame
        search_frame = tk.Frame(self.current_page, bg='#f0f0f0')
        search_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(search_frame, text="Name:", bg='#f0f0f0', font=("Microsoft YaHei", 10)).pack(side='left', padx=(0, 5))
        self.search_name = tk.Entry(search_frame, width=20, font=("Microsoft YaHei", 10))
        self.search_name.pack(side='left', padx=5)
        
        tk.Label(search_frame, text="ID:", bg='#f0f0f0', font=("Microsoft YaHei", 10)).pack(side='left', padx=(20, 5))
        self.search_id = tk.Entry(search_frame, width=20, font=("Microsoft YaHei", 10))
        self.search_id.pack(side='left', padx=5)
        
        tk.Label(search_frame, text="Age:", bg='#f0f0f0', font=("Microsoft YaHei", 10)).pack(side='left', padx=(20, 5))
        self.search_age = tk.Entry(search_frame, width=10, font=("Microsoft YaHei", 10))
        self.search_age.pack(side='left', padx=5)
        
        # search button
        search_btn = tk.Button(
            search_frame,
            text="Search",
            font=("Microsoft YaHei", 10, "bold"),
            bg='#9e9e9e',
            fg='white',
            command=self.search_students
        )
        search_btn.pack(side='left', padx=20)
        
        # refresh button
        refresh_btn = tk.Button(
            search_frame,
            text="Refresh",
            font=("Microsoft YaHei", 10, "bold"),
            bg='#4CAF50',
            fg='white',
            command=self.load_students
        )
        refresh_btn.pack(side='left', padx=10)
        
        # logout button
        logout_btn = tk.Button(
            search_frame,
            text="Logout",
            font=("Microsoft YaHei", 10, "bold"),
            bg='#f44336',
            fg='white',
            command=self.login_page
        )
        logout_btn.pack(side='right', padx=10)
        
        self.load_students()

    def show_add_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Student Info")
        dialog.geometry("400x300")
        dialog.configure(bg='#f0f0f0')
        dialog.transient(self.root)
        dialog.grab_set()
        
        # center window
        dialog.update_idletasks()
        width = dialog.winfo_width()
        height = dialog.winfo_height()
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
        
        tk.Label(dialog, text="Name:", font=("Microsoft YaHei", 12), bg='#f0f0f0').pack(pady=10)
        name_entry = tk.Entry(dialog, font=("Microsoft YaHei", 12), width=30)
        name_entry.pack(pady=5)
        
        tk.Label(dialog, text="ID:", font=("Microsoft YaHei", 12), bg='#f0f0f0').pack(pady=10)
        id_entry = tk.Entry(dialog, font=("Microsoft YaHei", 12), width=30)
        id_entry.pack(pady=5)
        
        tk.Label(dialog, text="Age:", font=("Microsoft YaHei", 12), bg='#f0f0f0').pack(pady=10)
        age_entry = tk.Entry(dialog, font=("Microsoft YaHei", 12), width=30)
        age_entry.pack(pady=5)
        
        def add_student():
            name = name_entry.get().strip()
            student_id = id_entry.get().strip()
            age = age_entry.get().strip()
            
            if not name or not student_id or not age:
                messagebox.showwarning("Input Error", "All fields are required")
                return
            
            if not age.isdigit():
                messagebox.showwarning("Input Error", "Age should be a number")
                return
            
            connection = self.get_connection()
            if not connection:
                return
            
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO info_table (student_name, student_id, student_age) VALUES (%s, %s, %s)",
                    (name, student_id, int(age))
                )
                connection.commit()
                messagebox.showinfo("Success", "Data added successfully")
                dialog.destroy()
                self.load_students()
            except pymysql.err.IntegrityError:
                messagebox.showerror("Error", "Student ID already exists")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add data: {e}")
            finally:
                cursor.close()
                connection.close()
        
        add_btn = tk.Button(
            dialog,
            text="Add",
            font=("Microsoft YaHei", 12, "bold"),
            bg='#2196F3',
            fg='white',
            width=10,
            command=add_student
        )
        add_btn.pack(pady=20)

    def load_students(self, search_params=None):
        # clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        connection = self.get_connection()
        if not connection:
            return
        
        try:
            cursor = connection.cursor()
            
            if search_params and any(search_params.values()):
                conditions = []
                params = []
                
                if search_params.get('name'):
                    conditions.append("student_name LIKE %s")
                    params.append(f"%{search_params['name']}%")
                
                if search_params.get('student_id'):
                    conditions.append("student_id LIKE %s")
                    params.append(f"%{search_params['student_id']}%")
                
                if search_params.get('age'):
                    conditions.append("student_age = %s")
                    params.append(int(search_params['age']))
                
                if conditions:
                    query = f"SELECT * FROM info_table WHERE {' AND '.join(conditions)} ORDER BY created_at DESC"
                    cursor.execute(query, params)
                else:
                    cursor.execute("SELECT * FROM info_table ORDER BY created_at DESC LIMIT 100")
            else:
                cursor.execute("SELECT * FROM info_table ORDER BY created_at DESC LIMIT 100")
            
            students = cursor.fetchall()
            
            for student in students:
                self.tree.insert('', 'end', values=(
                    student[1],  # student_name
                    student[2],  # student_id
                    student[3]   # student_age
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
        finally:
            cursor.close()
            connection.close()

    def search_students(self):
        search_params = {
            'name': self.search_name.get().strip(),
            'student_id': self.search_id.get().strip(),
            'age': self.search_age.get().strip()
        }
        
        if search_params['age'] and not search_params['age'].isdigit():
            messagebox.showwarning("Input Error", "Age should be a number")
            return
        
        self.load_students(search_params)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Student_man_sys()
    app.run()