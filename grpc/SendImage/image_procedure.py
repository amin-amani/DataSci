# A procedure which decodes base64 image, runs some machine learning model/ operation(s) (in our case we'll just return the mean of the pixel value)

import numpy as np 
import base64
import zlib
import numpy as np
import cv2

def predict(b64img_compressed, w, h):
    b64decoded = base64.b64decode(b64img_compressed)

    decompressed = b64decoded #zlib.decompress(b64decoded)

    imgarr = np.frombuffer(decompressed, dtype=np.uint8).reshape(h, w, -1)
    cv2.imshow('image',imgarr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0