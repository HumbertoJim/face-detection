from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from PIL import Image

from tools import get_home_dir, detect_faces, image_to_kivy_core_image


class HomeScreen(Screen):
    pass


class SelectImageScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.file_chooser.path = get_home_dir()

    def select_image(self, file_chooser, files, touch):
        file = files[0]
        try:
            image = detect_faces(Image.open(file))
            kivy_image = image_to_kivy_core_image(image)
            
            face_detection_screen = self.manager.get_screen('face_detection')
            face_detection_screen.ids.image_widget.texture = kivy_image.texture
            
            self.manager.transition.direction = 'left'
            self.manager.current = 'face_detection'
        except:
            self.manager.transition.direction = 'right'
            self.manager.current = 'home'


class FaceDetectionScreen(Screen):
    pass


class FaceDetectorApp(App):
    kv_file = 'template.kv'

    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SelectImageScreen(name='select_image'))
        sm.add_widget(FaceDetectionScreen(name='face_detection'))
        return sm

if __name__ == '__main__':
    FaceDetectorApp().run()
