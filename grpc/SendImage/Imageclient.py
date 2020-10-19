import grpc

# import the generated classes
import ImageTransfer_pb2
import ImageTransfer_pb2_grpc

# data encoding

import numpy as np 
import base64
import zlib
import time
import cv2


options = [('grpc.max_receive_message_length',  5147264)]
channel = grpc.insecure_channel('127.0.0.1:5005',options)

# create a stub (client)
stub = ImageTransfer_pb2_grpc.ImageProcedureStub(channel)

# encoding image/numpy array

t1 = time.time()
img = cv2.imread('cat.jpg')
data = np.asarray( img, dtype="int8" )# img
print(data.shape)
h, w, c = img.shape
data = base64.b64encode(data)

image_req = ImageTransfer_pb2.B64Image(b64image = data, width = w, height = h)
response = stub.ImageMeanWH(image_req)
time.sleep(5)
    
    
image_req = ImageTransfer_pb2.B64Image(b64image = data, width = w, height = h)
response = stub.ImageMeanWH(image_req)
t2 = time.time()

print(t2-t1)