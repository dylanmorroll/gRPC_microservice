import grpc
import electricity_data_pb2 as pb_classes
import electricity_data_pb2_grpc as grpc_classes

# connect to server
channel = grpc.insecure_channel('localhost:50051')
stub = grpc_classes.ElectrictyDataStub(channel)

#
info = pb_classes.RequestInfo()
data = stub.GetData(info)
print(data.a_name, data.b_name)
for item in data.data_list:
    print(item.a, item.b)
