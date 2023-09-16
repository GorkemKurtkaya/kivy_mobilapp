from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import json
from datetime import datetime

Window.size = (300,500)


Builder.load_file("loginscreen.kv")


class MainApp(App):
    def on_start(self):
        self.title = "English Puzzle"

    def build(self):
       return ScreenManager()

class ScreenManager(ScreenManager):
    pass

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, username, password):
        with open("users.json") as file:
            data = json.load(file)
        if username in data.keys() and data[username]["password"] == password:
            self.ids.wrong.text = ""
            self.manager.current = "home_screen"
        else:
            self.ids.wrong.text = "Wrong Username or Password!"
        

class SignUpScreen(Screen):
    def add_user(self,username,password):
        with open("users.json") as file:
            data = json.load(file)
        
        data[username] = {"username":username, "password":password, 
                            "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
        with open("users.json", "w") as file:
            json.dump(data, file)

        self.manager.current = "sign_up_success_screen"
    
class SignUpSuccessScreen(Screen):
    def go_to_login_page(self):
        self.manager.current = "login_screen"

class HomeScreen(Screen):
    def logout(self):
        self.manager.current = "login_screen"

    def go_to_homescreen(self):
        self.manager.current = "home_screen02"

class HomeScreen02(Screen):
    def logout(self):
        self.manager.current = "login_screen"

    def go_to_homescreen2(self):
        self.manager.current = "home_screen03"

class HomeScreen03(Screen):
    def logout(self):
        self.manager.current = "login_screen"

    def go_to_homescreen4(self):
        self.manager.current = "home_screen04"

class HomeScreen04(Screen):
    def logout(self):
        self.manager.current = "login_screen"
    
    def go_to_homescreen5(self):
        self.manager.current = "home_screen05"

class HomeScreen05(Screen):
    def logout(self):
        self.manager.current = "login_screen"










MainApp().run()