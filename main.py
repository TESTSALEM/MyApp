from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

# لضبط حجم النافذة عند التشغيل على الكمبيوتر (اختياري)
Window.size = (360, 640)

KV = """
ScreenManager:
    MenuScreen:
    Page1Screen:
    Page2Screen:
    Page3Screen:

<MenuScreen>:
    name: "menu"
    FloatLayout:
        Label:
            text: "مرحباً بك في التطبيق"
            font_size: "28sp"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
        Button:
            text: "الانتقال إلى الصفحة 1"
            size_hint: 0.6, 0.12
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release: app.change_screen("page1")
        Button:
            text: "الانتقال إلى الصفحة 2"
            size_hint: 0.6, 0.12
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
            on_release: app.change_screen("page2")
        Button:
            text: "الانتقال إلى الصفحة 3"
            size_hint: 0.6, 0.12
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_release: app.change_screen("page3")

<Page1Screen>:
    name: "page1"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "هذه الصفحة الأولى"
            font_size: "30sp"
        Button:
            text: "عودة للقائمة الرئيسية"
            size_hint_y: 0.2
            on_release: app.change_screen("menu")

<Page2Screen>:
    name: "page2"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "هذه الصفحة الثانية"
            font_size: "30sp"
        Button:
            text: "عودة للقائمة الرئيسية"
            size_hint_y: 0.2
            on_release: app.change_screen("menu")

<Page3Screen>:
    name: "page3"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "هذه الصفحة الثالثة"
            font_size: "30sp"
        Button:
            text: "عودة للقائمة الرئيسية"
            size_hint_y: 0.2
            on_release: app.change_screen("menu")
"""

class MenuScreen(Screen):
    pass

class Page1Screen(Screen):
    pass

class Page2Screen(Screen):
    pass

class Page3Screen(Screen):
    pass

class MyApp(App):
    def build(self):
        self.title = "تطبيقي"
        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.current = screen_name

if __name__ == "__main__":
    MyApp().run()
