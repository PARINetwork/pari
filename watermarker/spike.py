import pywt
import numpy
from PIL import Image

class Watermarker:

    def spike(self):
        original_image = Image.open('watermarked_image/weavers-image-4.jpg')
        original_image_array = numpy.asarray(original_image)
        dwt_image = pywt.wavedecn(original_image_array, 'db3')
        dwt_retransform_db3 = pywt.waverecn(dwt_image, 'db3')
        dwt_image_db3 = Image.fromarray(dwt_retransform_db3, 'RGB')
        dwt_image_db3.save('watermarked_image/dwt_image_db3.jpg')
        water_mark_string = "People's archive of rural India"
        water_string_to_ascii_array = numpy.array(water_mark_string)
