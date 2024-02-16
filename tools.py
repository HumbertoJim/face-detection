import os
from facenet_pytorch import MTCNN
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from kivy.core.image import Image as KivyCoreImage

mtcnn = MTCNN(keep_all=True)

def get_home_dir():
    if os.name == 'nt':
        return os.path.expanduser('~\\')
    elif os.name == 'posix':
        return os.path.expanduser('~')
    elif os.name == 'android':
        return '/sdcard/'
    elif os.name == 'darwin':
        return os.path.expanduser('~/')
    else:
        # Manejo de caso inesperado
        print("ADVERTENCIA: Sistema operativo no reconocido. Devolviendo None.")
        return None


def image_to_kivy_core_image(image: Image):
    buffer = BytesIO()
    image.save(buffer, format='jpeg')
    buffer.seek(0)
    kivy_image = KivyCoreImage(BytesIO(buffer.read()), ext='jpeg')
    return kivy_image

    
def detect_faces(image: Image) -> Image:
    im = image.convert('RGB')
    draw = ImageDraw.Draw(im)
    boxes, _ = mtcnn.detect(im)
    if boxes is not None:
        for box in boxes:
            draw.rectangle(box.tolist(), outline='red', width=2)
    else:
        draw.text(
            (0, 0),
            text='No face detected',
            fill='red',
            font=ImageFont.truetype("arial.ttf", int(min(im.size) * 0.07))
        )
    return im