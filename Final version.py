'''
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from P0 import get_p0_layout
from UI_design import get_ui_design_layout
from P2 import get_p2_layout
from P3 import get_p3_layout
from P4 import get_p4_layout

class P0Screen(Screen):
    def __init__(self, **kwargs):
        super(P0Screen, self).__init__(**kwargs)
        self.add_widget(get_p0_layout())

class UIScreen(Screen):
    def __init__(self, **kwargs):
        super(UIScreen, self).__init__(**kwargs)
        self.add_widget(get_ui_design_layout())

class P2Screen(Screen):
    def __init__(self, **kwargs):
        super(P2Screen, self).__init__(**kwargs)
        self.add_widget(get_p2_layout())

class P3Screen(Screen):
    def __init__(self, **kwargs):
        super(P3Screen, self).__init__(**kwargs)
        self.add_widget(get_p3_layout())

class P4Screen(Screen):
    def __init__(self, **kwargs):
        super(P4Screen, self).__init__(**kwargs)
        self.add_widget(get_p4_layout())

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(P0Screen(name='p0_screen'))
        sm.add_widget(UIScreen(name='ui_screen'))
        sm.add_widget(P2Screen(name='p2_screen'))
        sm.add_widget(P3Screen(name='p3_screen'))
        sm.add_widget(P4Screen(name='p4_screen'))

        sm.current = 'p0_screen'

        Window.bind(on_touch_down=self.on_touch_down)

        self.sm = sm
        return sm

    def on_touch_down(self, window, touch):
        if touch.button == 'left':
            screen_names = ['p0_screen', 'ui_screen', 'p2_screen', 'p3_screen', 'p4_screen']
            current_index = screen_names.index(self.sm.current)
            next_index = (current_index + 1) % len(screen_names)
            self.sm.current = screen_names[next_index]

if __name__ == '__main__':
    MainApp().run()
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from datetime import datetime


class LogoDisplayScreen(Screen):
    def build(self):
        root = FloatLayout()

        # Container to maintain 9:16 aspect ratio
        container = FloatLayout(size_hint=(0.5625, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Center the logo display GIF
        self.logo_display = Image(source='C:/M&TSI/Logo display.gif', size_hint=(None, None), size=(800, 450))
        self.logo_display.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        container.add_widget(self.logo_display)
        root.add_widget(container)
        self.add_widget(root)


class WeatherScreen(Screen):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.layout.size_hint = (0.5625, 1)  # Adjust for 9:16 aspect ratio

        # Top bar layout
        top_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10)

        # Mission label
        mission_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        self.mission_label = Label(text="- Your skin. Our universe. -", font_size='20sp')
        mission_layout.add_widget(self.mission_label)

        # Date and time labels
        date_time_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        date_layout = BoxLayout(orientation='vertical')
        self.date_label = Label(text=self.get_date(), font_size='20sp', size_hint=(1, 0.5))
        self.time_label = Label(text=self.get_time(), font_size='40sp', size_hint=(1, 0.5))
        date_layout.add_widget(self.date_label)
        date_layout.add_widget(self.time_label)
        date_time_layout.add_widget(date_layout)

        # Weather label and icon
        weather_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        weather_inner_layout = BoxLayout(orientation='horizontal', spacing=5)
        self.weather_label = Label(text="Philadelphia: 27°C\nSunny", font_size='20sp')
        self.sunny_image = Image(source='C:/M&TSI/Sunny logo.jpg', size_hint=(None, None), size=(50, 50))
        weather_inner_layout.add_widget(self.weather_label)
        weather_inner_layout.add_widget(self.sunny_image)
        weather_layout.add_widget(weather_inner_layout)

        # Add widgets to top bar
        top_bar.add_widget(mission_layout)
        top_bar.add_widget(date_time_layout)
        top_bar.add_widget(weather_layout)

        self.layout.add_widget(top_bar)

        # Face label
        face_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        self.face_label = Label(text="[color=ffffff] [/color]", font_size='100sp', markup=True)
        face_layout.add_widget(self.face_label)
        self.layout.add_widget(face_layout)

        # Logo at the bottom
        logo_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        self.logo = Image(source='C:/M&TSI/illumi logo.png', size_hint=(None, None), size=(400, 400))
        logo_layout.add_widget(self.logo)
        self.layout.add_widget(logo_layout)

        Clock.schedule_interval(self.update_time, 1)
        self.add_widget(self.layout)

    def get_date(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d")

    def get_time(self):
        now = datetime.now()
        return now.strftime("%H:%M")

    def update_time(self, *args):
        self.time_label.text = self.get_time()
        self.date_label.text = self.get_date()


class ScannerWidget(Widget):
    def __init__(self, **kwargs):
        super(ScannerWidget, self).__init__(**kwargs)
        self.scan_line_y = self.height
        self.bind(size=self.update_rect)
        self.bind(pos=self.update_rect)

    def update_rect(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 0, 1)  # Black background
            self.rect = Rectangle(pos=self.pos, size=self.size)
            Color(1, 1, 1, 1)  # White border
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

    def move_scan_line(self, dt):
        self.canvas.after.clear()
        with self.canvas.after:
            Color(1, 1, 1, 1)  # White scan line
            Line(points=[self.x, self.scan_line_y, self.right, self.scan_line_y], width=2)
        self.scan_line_y -= 5
        if self.scan_line_y < self.y:
            self.scan_line_y = self.top


class ScannerScreen(Screen):
    def build(self):
        root = FloatLayout()

        container = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint=(0.5625, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Scanner widget
        self.scanner = ScannerWidget(size_hint=(1, 1.8))
        container.add_widget(self.scanner)

        # Camera symbol below the scanner
        camera_layout = AnchorLayout(anchor_x='center', anchor_y='top')
        self.camera_symbol = Image(source='C:/M&TSI/photo symbol.png', size_hint=(None, None), size=(100, 100))
        camera_layout.add_widget(self.camera_symbol)
        container.add_widget(camera_layout)

        # illumi logo at the bottom
        logo_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        self.logo = Image(source='C:/M&TSI/illumi logo.png', size_hint=(None, None), size=(400, 400))
        logo_layout.add_widget(self.logo)
        container.add_widget(logo_layout)

        root.add_widget(container)
        self.add_widget(root)

        Clock.schedule_interval(self.scanner.move_scan_line, 1 / 60)  # 60 FPS


class ImageDisplayScreen(Screen):
    def build(self):
        root = FloatLayout()

        container = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint=(0.5625, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Image in the center
        image_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        self.image = Image(source='C:/M&TSI/detection results.png', size_hint=(None, None), size=(800, 450))  # Adjust size if needed
        image_layout.add_widget(self.image)
        container.add_widget(image_layout)

        # Text immediately below the image
        text_label = Label(text="pustule, nevus, papule, atrophic scar", font_size='20sp', halign='center', valign='middle', size_hint=(1, None))
        text_label.bind(size=text_label.setter('text_size'))
        container.add_widget(text_label)

        # Logo at the bottom
        logo_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        self.logo = Image(source='C:/M&TSI/illumi logo.png', size_hint=(None, None), size=(450, 450))
        logo_layout.add_widget(self.logo)
        container.add_widget(logo_layout)

        root.add_widget(container)
        self.add_widget(root)


class MainApp(App):
    def build(self):
        sm = ScreenManager()

        logo_display_screen = LogoDisplayScreen(name='logo_display_screen')
        logo_display_screen.build()
        sm.add_widget(logo_display_screen)

        weather_screen = WeatherScreen(name='weather_screen')
        weather_screen.build()
        sm.add_widget(weather_screen)

        scanner_screen = ScannerScreen(name='scanner_screen')
        scanner_screen.build()
        sm.add_widget(scanner_screen)

        image_display_screen = ImageDisplayScreen(name='image_display_screen')
        image_display_screen.build()
        sm.add_widget(image_display_screen)

        sm.current = 'logo_display_screen'

        Window.bind(on_mouse_down=self.switch_screen)

        self.sm = sm
        return sm

    def switch_screen(self, *args):
        screen_order = ['logo_display_screen', 'weather_screen', 'scanner_screen', 'image_display_screen']
        current_index = screen_order.index(self.sm.current)
        next_index = (current_index + 1) % len(screen_order)
        self.sm.current = screen_order[next_index]


if __name__ == '__main__':
    MainApp().run()
