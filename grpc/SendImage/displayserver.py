import numpy as np
import cv2
import grpc
from concurrent import futures
import time
import image_procedure
# import the generated classes
import ImageTransfer_pb2
import ImageTransfer_pb2_grpc


# based on .proto service
class ImageProcedureServicer(ImageTransfer_pb2_grpc.ImageProcedureServicer):

    def ImageMeanWH(self, request, context):
        response = ImageTransfer_pb2.Prediction()
        response.channel, response.mean  = image_procedure.predict(request.b64image, request.width, request.height)
        return response


# create a gRPC server
channel_opt = [('grpc.max_receive_message_length', 4000 * 4000 * 3)]
server = grpc.server(futures.ThreadPoolExecutor(max_workers=12), options=channel_opt)

# add the defined class to the server
ImageTransfer_pb2_grpc.add_ImageProcedureServicer_to_server(
        ImageProcedureServicer(), server)

# listen on port 5005
print('Starting server. Listening on port 5005.')
server.add_insecure_port('[::]:5005')
server.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    server.stop(0)
# Load an color image in grayscale
# img = cv2.imread('1.png',0)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()