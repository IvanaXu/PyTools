import random
from captcha.image import ImageCaptcha

image = ImageCaptcha(width=200, height=100)
image.write(
    f'{random.randint(1111, 9999)}', 
    '127.Test_captcha.png'
) 
