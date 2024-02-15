from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    pass

class SelectImageScreen(Screen):
    def next_screen(self):
        # make some validations
        face_detection_screen = self.manager.get_screen('face_detection')
        face_detection_screen.ids.image_widget.source = '' # Modifica la fuente de la imagen
        self.manager.transition.direction = 'left'
        self.manager.current = 'face_detection'

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
