# grpc imports
import grpc
import electricity_data_pb2 as pb_classes
import electricity_data_pb2_grpc as grpc_classes

# flask imports
from flask import Flask, g, render_template

import json

# connect to the grpc server
grpc_channel = grpc.insecure_channel('localhost:50051')

# # create a flask app
# app = Flask(__name__)
#
# #the default page
# @app.route("/")
# def serve_data():
# create a stub to utilise the grpc server
stub = grpc_classes.ElectrictyDataStub(grpc_channel)

# get the data from the gRPC server
data = stub.GetData(pb_classes.RequestInfo())

# turn the meter readings into a list for JSON conversion
pair_list = []
for item in data.data_list:
    pair_list.append((item.a, item.b))

# create a dictionary from the information for JSON conversion
data_dict = {
    "a_name": data.a_name,
    "b_name": data.b_name,
    "data_list": pair_list
}

# convert into JSON:
data_json = json.dumps(data_dict)

# the result is a JSON string:
print(data_json)

    #     # return is as a JSON object
    # return render_template("templates/display_data.html",
    #                        a_name=data.a_name,
    #                        b_name=data.b_name,
    #                        data=data.data_list)
