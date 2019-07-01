# grpc imports
import grpc
import electricity_data_pb2 as pb_classes
import electricity_data_pb2_grpc as grpc_classes

# flask imports
from flask import Flask, g, render_template

# other imports
import json

# connect to the grpc server
grpc_channel = grpc.insecure_channel('localhost:50051')

# create a flask app
app = Flask(__name__)

#the default page
@app.route("/")
def serve_data():
    # create a stub to utilise the grpc server
    stub = grpc_classes.ElectrictyDataStub(grpc_channel)

    # get the data from the gRPC server
    data = stub.GetData(pb_classes.RequestInfo())

    # create a dictionary from the information for JSON conversion
    data_dict = {
        "a_name": data.a_name,
        "b_name": data.b_name
    }

    # turn the meter readings into a list for JSON conversion
    meter_readings = []
    for item in data.data_list:
        meter_readings.append((item.a, item.b))
    data_dict["meter_readings"] = meter_readings

    # convert into JSON:
    data_json = json.dumps(data_dict)

    # return is as a JSON object to the HTML page
    return render_template('data_display.html', json_data=data_json)

if __name__ == "__main__":
    app.run(debug=True)
