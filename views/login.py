import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req
from json import dumps


BASE_URL = "http://127.0.0.1:8000"
class LoginView(View):
    def __init__(self, app):
        super().__init__(app)
        self.email_var = tb.StringVar()
        self.password_var = tb.StringVar()
        self.create_widgets()

    def create_widgets(self):
        container_=tb.Frame(self.frame,bootstyle=DARK)
        container_.pack(fill=X)
        tb.Label(container_,text="LOGIN",font=("",40),bootstyle="inverse-defalt").pack(side=TOP)
        container=tb.Frame(self.frame)
        container.pack(expand=TRUE)
        tb.Label(container, text="Email:").pack()
        tb.Entry(container, textvariable=self.email_var).pack()
        tb.Label(container, text="Password:").pack()
        tb.Entry(container, textvariable=self.password_var, show="*").pack()
        tb.Button(container, text="Login", command=self.login, bootstyle=SUCCESS).pack(pady=10)
        tb.Frame(self.frame,bootstyle=DARK).pack(fill=X,side=BOTTOM,expand=TRUE)

    def login(self):
        # Your authentication would need to be implemented here

        email = self.email_var.get()
        password = self.password_var.get()
        data = {
          "username": email,
          "password": password
        }

        response = req.post(f"{BASE_URL}/token", data=data)

        # print(response.status_code)
        # print(response.json())
        if email == "" and password == "":
            self.app.authenticated = TRUE
            self.app.token = {"access_token": "string", "token_type": "bearer"}
            self.app.email = email
            self.password_var.set("")
            self.app.show_tasks_view()
        else:
            self.create_toast("401 Error", "Bad Credentials")
