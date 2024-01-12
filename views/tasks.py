import ttkbootstrap as tb
from ttkbootstrap.constants import *
import requests as req
from json import dumps
from views.helper import View

# the code is not complete
fakedata=[
    {   "id":1,
        "title":"doing final project",
        "author":"Richard",
        "description":"doing python final project",
        "priority":5,
        "complete":False,
        "created_on":"22:45"
    },
    {   "id":2,
        "title":"sleep",
        "author":"Richard",
        "description":"get enough sleep",
        "priority":4,
        "complete":True,
        "created_on":"1:24"
    },
    {   "id":3,
        "title":"review calculus",
        "author":"Richard",
        "description":"review chapter 5,7 and 8 of calculus",
        "priority":4,
        "complete":False,
        "created_on":"23:10"
    },
    {   "id":4,
        "title":"get some food",
        "author":"Richard",
        "description":"get some food to eat, little hungry",
        "priority":3,
        "complete":False,
        "created_on":"23:50"
    }
]

class TasksView(View):
    def __init__(self, app):
        super().__init__(app)
        self.tasks_widgets = []
        self.page=0
        self.task=fakedata[0]
        self.button_complete = tb.Button()
        self.button_delete = tb.Button()
        self.delete_mode = False
        self.create_widgets()


    def create_widgets(self):
        # Add code to display a list of tasks here
        container_b = tb.Frame(self.frame)
        container_b.pack(fill=X, pady=5, side=BOTTOM)
        container_ = tb.Frame(self.frame, bootstyle=DARK)
        container_.pack(fill=X)
        tb.Label(container_, text="TASK LIST", font=("", 20), bootstyle="inverse-defalt").pack(side=TOP)
        tb.Label(self.frame,text='',).pack(pady=10)
        for self.task in fakedata:
            row = {}
            if self.task["complete"]:row["container"] = tb.Frame(self.frame,bootstyle=SECONDARY)
            else:row["container"] = tb.Frame(self.frame,bootstyle=DARK)
            row["container"].pack(fill=X, pady=5,padx=20)
            if self.task["complete"]:row["label"] = tb.Label(row["container"], text=self.task["title"],bootstyle="inverse-secondary")
            else:row["label"] = tb.Label(row["container"], text=self.task["title"],bootstyle="inverse-dark")
            row["label"].pack(side=LEFT, expand=TRUE)
            row["button"] = tb.Button(row["container"], text=f"task detail'{self.task['id']}'", command=self.button_function, bootstyle=PRIMARY)
            row["button"].pack(side=LEFT, padx=5)

            self.tasks_widgets.append(row)

        tb.Button(container_b, text="Create Task", command=self.app.show_create_task_view, bootstyle = SUCCESS).pack(side=RIGHT,padx=5)

        self.button_delete = (tb.Button(container_b, text="delete task", bootstyle=DANGER, command=self.change_button_purpose))
        self.button_delete.pack(side=RIGHT)


    def change_button_purpose(self):
        if self.delete_mode:
            self.delete_mode = False
            for row in self.tasks_widgets:
                row["button"].configure(text="task detail", bootstyle=PRIMARY)
            self.button_delete.configure(text="delete task", bootstyle=DANGER)
        else:
            self.delete_mode = True
            for row in self.tasks_widgets:
                row["button"].configure(text="delete", bootstyle=DANGER)
            self.button_delete.configure(text="detail", bootstyle=PRIMARY)

    def button_function(self):
        if self.delete_mode:
            pass#删除当前任务，调用api中delete功能
        else:
            print(self.task["id"])
            # self.page=id
            self.app.show_task_view()





class TaskView(View):
    def __init__(self, app):
        super().__init__(app)
        self.create_widgets()

    def create_widgets(self):
        container_ = tb.Frame(self.frame, bootstyle=DARK)
        container_.pack(fill=X)
        tb.Label(container_, text="TASK MANAGER", font=("", 20), bootstyle="inverse-defalt").pack(side=TOP)
        ctn_title = tb.Frame(self.frame)
        ctn_title.pack(fill=X)
        ctn_id = tb.Frame(self.frame)
        ctn_id.pack(fill=X)
        ctn_description = tb.Frame(self.frame)
        ctn_description.pack(fill=X)
        ctn_prtority = tb.Frame(self.frame)
        ctn_prtority.pack(fill=X)
        ctn_created_on = tb.Frame(self.frame)
        ctn_created_on.pack(fill=X)
        tb.Label(ctn_id, text="Task id:").pack(side=LEFT)
        tb.Label(ctn_title, text="Task title:").pack(side=LEFT)
        tb.Label(ctn_description, text="Task description:").pack(side=LEFT)
        tb.Label(ctn_prtority, text="prtority:").pack(side=LEFT)
        tb.Label(ctn_created_on, text="created on:").pack(side=LEFT)

        container_b=tb.Frame(self.frame)
        container_b.pack()
        tb.Button(container_b, text="Back to View Tasks", command=self.app.show_tasks_view).pack(side=RIGHT,padx=10)
        # if self.task["complete"]:self.button_complete = (tb.Button(container_b, text="complete", command=self.button_function,bootstyle=SUCCESS))
        # else: self.button_complete = (tb.Button(container_b, text="reopen", command=self.button_function,bootstyle=SECONDARY))
        # self.button_complete.pack(side=RIGHT)
    #
    # def button_function(self):
    #     if self.task["complete"]:#something that show this task
    #         self.button_complete.configure(text="reopen",bootstyle=SECONDARY)
    #         self.task["complete"]=False
    #     else:
    #         self.button_complete.configure(text="complete", bootstyle=SUCCESS)
    #         self.task["complete"] = True
class CreateTaskView(View):
    def __init__(self, app):
        super().__init__(app)
        self.task_name_var = tb.StringVar()
        self.task_description_var = tb.StringVar()
        self.task_priority_var = tb.StringVar()
        self.create_widgets()

    def create_widgets(self):
        container_ = tb.Frame(self.frame, bootstyle=DARK)
        container_.pack(fill=X)
        tb.Label(container_, text="CREATE TASK", font=("", 20), bootstyle="inverse-defalt").pack(side=TOP)
        tb.Label(self.frame, text="Task Name:").pack()
        tb.Entry(self.frame, textvariable=self.task_name_var).pack()
        tb.Label(self.frame, text="Description:").pack()
        tb.Entry(self.frame, textvariable=self.task_description_var).pack()
        tb.Label(self.frame, text="priority:").pack()
        combobox = tb.Combobox(self.frame, textvariable=self.task_priority_var)
        combobox.config(
            values=[1, 2, 3, 4, 5],  # 设置下拉框中的选项列表
            state="readonly",  # 设置 Combobox 为只读模式，防止手动输入
            width=5,  # 设置 Combobox 的宽度
            takefocus=True,  # 设置 Combobox 是否接受焦点，默认为 True
            cursor="hand2"  # 设置鼠标悬停在 Combobox 上时的光标样式
        )
        combobox.pack()

        tb.Button(self.frame, text="Create Task", command=self.create_task).pack()
        tb.Button(self.frame, text="Back", command=self.app.show_tasks_view).pack()

    def create_task(self):
        # Add your code to create a task here
        task_name = self.task_name_var.get()
        task_description = self.task_description_var.get()
        task_priority = self.task_priority_var.get()

        data = {
            "title": task_name,
        }
        self.create_toast("Task Created",f"Task '{task_name}','{task_description}','{task_priority}' created successfully")
        # response = req.post("URL", data=dumps(data))
        # if response.status_code == 201:
        #     self.create_toast("Task Created", f"Task '{task_name}','{task_description}','{task_priority}' created successfully")
        # else:
        #     pass



        # After creating the task, show the task page
        self.app.show_task_view()
