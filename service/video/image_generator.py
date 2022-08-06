from datetime import datetime

import cv2
import numpy as np
from textwrap3 import wrap


def generate_image(text):
    img = np.zeros((1920, 1080, 3), dtype=np.uint8)
    img[:, :] = (255, 255, 255)
    height, width, channel = img.shape

    text_img = np.ones((height, width))
    print(text_img.shape)
    font = cv2.FONT_HERSHEY_SIMPLEX

    wrapped_text = wrap(text, width=50)
    font_size = 1
    font_thickness = 1

    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

        gap = textsize[1] + 10

        y = int((img.shape[0] + textsize[1]) / 25) + i * gap
        x = int((img.shape[1] - textsize[0]) / 2)

        cv2.putText(img, line, (x, y), font,
                    font_size,
                    (0, 0, 0),
                    font_thickness,
                    lineType=cv2.LINE_AA)
    cv2.imwrite(f"media/temp/text_{datetime.now().strftime('%Y%m%d%H%M%S%z')}.jpg", img)
