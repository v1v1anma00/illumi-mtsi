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

# Update the font path to the location of Open Sans font on your system
font_path = 'C:\\M&TSI\\Open_Sans\\OpenSans-VariableFont_wdth,wght.ttf'  # Change this to your actual font path

class LogoDisplayScreen(Screen):
    def build(self):
        root = FloatLayout()

        # Container to maintain 9:16 aspect ratio
        container = FloatLayout(size_hint=(0.5625, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Center the logo display GIF
        self.logo_display = Image(source='C:/M&TSI/ILLUMI.gif', size_hint=(None, None), size=(800, 450))
        self.logo_display.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        container.add_widget(self.logo_display)
        root.add_widget(container)
        self.add_widget(root)
class WeatherScreen(Screen):
    def build(self):
        layout = FloatLayout()

        # Add an Image widget, with size_hint to fill the height and keep the aspect ratio
        img = Image(source="C:/M&TSI/P00.png", allow_stretch=True, keep_ratio=True)
        img.size_hint = (5, None)
        img.height = Window.height
        img.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(img)

        # Add a Label for the real-time clock display
        self.time_label = Label(text=self.get_time(), font_size='40sp', size_hint=(None, None),
                                pos_hint={'top': 0.8, 'center_x': 0.5})
        layout.add_widget(self.time_label)

        Clock.schedule_interval(self.update_time, 1)

        self.add_widget(layout)

    def get_time(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    def update_time(self, *args):
        self.time_label.text = self.get_time()

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
        text_label = Label(text="Acne,Dark circle", font_size='20sp', halign='center', valign='middle', size_hint=(1, None), font_name=font_path)
        text_label.bind(size=text_label.setter('text_size'))
        container.add_widget(text_label)

        # Logo at the bottom
        logo_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        self.logo = Image(source='C:/M&TSI/illumi logo.png', size_hint=(None, None), size=(450, 450))
        logo_layout.add_widget(self.logo)
        container.add_widget(logo_layout)

        root.add_widget(container)
        self.add_widget(root)

class CenteredImageApp(Screen):
    def build(self):
        layout = FloatLayout()

        # Add an Image widget, with size_hint to fill the height and keep the aspect ratio
        img = Image(source="C:/M&TSI/fiveone.png", allow_stretch=True, keep_ratio=True)
        img.size_hint = (1.2, 1.2)  # Adjust size_hint to control the image size
        img.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(img)

        # Add a Label for the Timer
        self.timer_label = Label(text="60", font_size='40sp', size_hint=(None, None),
                                 pos_hint={'right': 0.65, 'top': 0.9})
        layout.add_widget(self.timer_label)

        # Initialize countdown time and timer running flag
        self.countdown_time = 60
        self.timer_running = False

        # Bind mouse click event
        Window.bind(on_mouse_down=self.on_mouse_down)

        self.add_widget(layout)

    def on_mouse_down(self, window, pos, button, *args):
        if not self.timer_running:
            self.timer_running = True
            Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.timer_label.text = str(self.countdown_time)
        else:
            Clock.unschedule(self.update_timer)

class CenteredImageApp2(Screen):
    def build(self):
        layout = FloatLayout()

        # Add an Image widget, with size_hint to fill the height and keep the aspect ratio
        img = Image(source="C:/M&TSI/5.2.png", allow_stretch=True, keep_ratio=True)
        img.size_hint = (1.2, 1.2)  # Adjust size_hint to control the image size
        img.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(img)

        # Add a Label for the Timer
        self.timer_label = Label(text="60", font_size='40sp', size_hint=(None, None),
                                 pos_hint={'right': 0.6, 'top': 0.77})
        layout.add_widget(self.timer_label)

        # Initialize countdown time and timer running flag
        self.countdown_time = 60
        self.timer_running = False

        # Bind mouse click event
        Window.bind(on_mouse_down=self.on_mouse_down)

        self.add_widget(layout)

    def on_mouse_down(self, window, pos, button, *args):
        if not self.timer_running:
            self.timer_running = True
            Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.timer_label.text = str(self.countdown_time)
        else:
            Clock.unschedule(self.update_timer)

class CenteredImageApp3(Screen):
    def build(self):
        layout = FloatLayout()

        # Add an Image widget, with size_hint to fill the height and keep the aspect ratio
        img = Image(source="C:/M&TSI/5.3.png", allow_stretch=True, keep_ratio=True)
        img.size_hint = (1.2, 1.2)  # Adjust size_hint to control the image size
        img.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(img)

        # Add a Label for the Timer
        self.timer_label = Label(text="60", font_size='40sp', size_hint=(None, None),
                                 pos_hint={'right': 0.6, 'top': 0.77})
        layout.add_widget(self.timer_label)

        # Initialize countdown time and timer running flag
        self.countdown_time = 60
        self.timer_running = False

        # Bind mouse click event
        Window.bind(on_mouse_down=self.on_mouse_down)

        self.add_widget(layout)

    def on_mouse_down(self, window, pos, button, *args):
        if not self.timer_running:
            self.timer_running = True
            Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.timer_label.text = str(self.countdown_time)
        else:
            Clock.unschedule(self.update_timer)

class TimeMissionLogoScreen(Screen):
    def build(self):
        layout = FloatLayout()

        # Time display
        self.time_label = Label(text=self.get_time(), font_size='40sp', size_hint=(None, None), pos_hint={'top': 1, 'center_x': 0.5})
        layout.add_widget(self.time_label)

        # Mission display
        mission_layout = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.75})
        mission_text = "\"Your skin. Your way\"\n- illumi \n \n - Do you want illumi GPT help? -"
        mission_label = Label(text=mission_text, font_size='30sp', markup=True, halign='center', valign='middle')
        mission_label.bind(size=mission_label.setter('text_size'))
        mission_layout.add_widget(mission_label)
        layout.add_widget(mission_layout)

        # Logo display
        logo_layout = AnchorLayout(anchor_x='center', anchor_y='bottom', size_hint=(None, None), pos_hint={'center_x': 0.5, 'y': 0})
        self.logo = Image(source='C:/M&TSI/illumi logo.png', size_hint=(None, None), size=(450, 450))
        logo_layout.add_widget(self.logo)
        layout.add_widget(logo_layout)

        Clock.schedule_interval(self.update_time, 1)

        self.add_widget(layout)

    def get_time(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    def update_time(self, *args):
        self.time_label.text = self.get_time()

class P7Screen(Screen):
    def build(self):
        layout = FloatLayout()

        # Add an Image widget, with size_hint to fill the height and keep the aspect ratio
        img = Image(source="C:/M&TSI/P7.png", allow_stretch=True, keep_ratio=True)
        img.size_hint = (5, None)
        img.height = Window.height
        img.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(img)

        self.add_widget(layout)

class P8Screen(Screen):
    def build(self):
        layout = FloatLayout()

        # Add an Image widget, with size_hint to fill the height and keep the aspect ratio
        img = Image(source="C:/M&TSI/P8.png", allow_stretch=True, keep_ratio=True)
        img.size_hint = (5, None)
        img.height = Window.height
        img.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(img)

        self.add_widget(layout)

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

        centered_image_screen = CenteredImageApp(name='centered_image_screen')
        centered_image_screen.build()
        sm.add_widget(centered_image_screen)

        centered_image_screen2 = CenteredImageApp2(name='centered_image_screen2')
        centered_image_screen2.build()
        sm.add_widget(centered_image_screen2)

        centered_image_screen3 = CenteredImageApp3(name='centered_image_screen3')
        centered_image_screen3.build()
        sm.add_widget(centered_image_screen3)

        time_mission_logo_screen = TimeMissionLogoScreen(name='time_mission_logo_screen')
        time_mission_logo_screen.build()
        sm.add_widget(time_mission_logo_screen)

        p7_screen = P7Screen(name='p7_screen')
        p7_screen.build()
        sm.add_widget(p7_screen)

        p8_screen = P8Screen(name='p8_screen')
        p8_screen.build()
        sm.add_widget(p8_screen)

        sm.current = 'logo_display_screen'

        Window.bind(on_mouse_down=self.switch_screen)

        self.sm = sm
        return sm

    def switch_screen(self, *args):
        screen_order = [
            'logo_display_screen', 'weather_screen', 'scanner_screen',
            'image_display_screen', 'centered_image_screen', 'centered_image_screen2', 'centered_image_screen3',
            'time_mission_logo_screen', 'p7_screen', 'p8_screen'
        ]
        current_index = screen_order.index(self.sm.current)
        next_index = (current_index + 1) % len(screen_order)
        self.sm.current = screen_order[next_index]

if __name__ == '__main__':
    MainApp().run()
