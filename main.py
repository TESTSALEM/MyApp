from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ListProperty


# ويدجت يمثل الخلفية بلون متغير
class Background(Widget):
    color = ListProperty([0, 0, 0, 1])


# صفحة رئيسية
class HomePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.bg = Background()
        self.bg.color = self.manager.app_bg_color if hasattr(self.manager, 'app_bg_color') else [0.1, 0.2, 0.3, 1]
        self.layout.add_widget(self.bg)

        label = Label(text="Welcome to Home Page", font_size=35, color=(1,1,1,1))
        self.layout.add_widget(label)

        self.layout.add_widget(bottom_nav(self))
        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.bg.color = self.manager.app_bg_color


# صفحة حول
class AboutPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.bg = Background()
        self.bg.color = self.manager.app_bg_color if hasattr(self.manager, 'app_bg_color') else [0.1, 0.2, 0.3, 1]
        self.layout.add_widget(self.bg)

        label = Label(text="About This App", font_size=35, color=(1,1,1,1))
        self.layout.add_widget(label)

        self.layout.add_widget(bottom_nav(self))
        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.bg.color = self.manager.app_bg_color


# صفحة الإعدادات + تغيير الخلفية
class SettingsPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        self.bg = Background()
        self.layout.add_widget(self.bg)

        self.label = Label(text="Change Background Color", font_size=32, color=(1,1,1,1))
        self.layout.add_widget(self.label)

        btns = BoxLayout(size_hint=(1, 0.3), spacing=10)

        btn_red = Button(text="Red", background_normal='', background_color=(1,0,0,1), color=(1,1,1,1))
        btn_blue = Button(text="Blue", background_normal='', background_color=(0,0.4,1,1), color=(1,1,1,1))
        btn_green = Button(text="Green", background_normal='', background_color=(0,1,0.5,1), color=(1,1,1,1))

        btn_red.bind(on_release=lambda x: self.change_color([1, 0, 0, 1]))
        btn_blue.bind(on_release=lambda x: self.change_color([0, 0.4, 1, 1]))
        btn_green.bind(on_release=lambda x: self.change_color([0, 1, 0.5, 1]))

        btns.add_widget(btn_red)
        btns.add_widget(btn_blue)
        btns.add_widget(btn_green)

        self.layout.add_widget(btns)
        self.layout.add_widget(bottom_nav(self))
        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.bg.color = self.manager.app_bg_color

    def change_color(self, color):
        self.manager.app_bg_color = color
        for screen in self.manager.screens:
            if hasattr(screen, 'bg'):
                screen.bg.color = color


# شريط التنقل السفلي
def bottom_nav(screen):
    bar = BoxLayout(size_hint=(1, 0.15), spacing=10)

    home = Button(text="Home")
    about = Button(text="About")
    settings = Button(text="Settings")

    home.bind(on_release=lambda x: screen.manager.current == "home" or setattr(screen.manager, 'current', "home"))
    about.bind(on_release=lambda x: screen.manager.current == "about" or setattr(screen.manager, 'current', "about"))
    settings.bind(on_release=lambda x: screen.manager.current == "settings" or setattr(screen.manager, 'current', "settings"))

    bar.add_widget(home)
    bar.add_widget(about)
    bar.add_widget(settings)
    return bar


# التطبيق الرئيسي
class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # اللون الافتراضي للخلفية
        sm.app_bg_color = [0, 0.3, 0.7, 1]

        sm.add_widget(HomePage(name="home"))
        sm.add_widget(AboutPage(name="about"))
        sm.add_widget(SettingsPage(name="settings"))

        return sm


if __name__ == "__main__":
    MyApp().run()