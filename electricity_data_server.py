# external imports
import grpc
import time
from concurrent import futures

#internal imports
import electricity_data_pb2 as pb_classes
import electricity_data_pb2_grpc as grpc_classes

# retrieve meter usage data from file
def getMeterUsage():
    # turn file into a Data object
    data = pb_classes.Data()

    # retrieve the information from the csv file
    with open("meterusage.csv") as data_file:
        # get the titles of the fields
        one, two = data_file.readline().strip().split(',')
        data.a_name = one
        data.b_name = two

        # get the values of the file
        for line in data_file:
            one, two = line.strip().split(',')
            # append it to data
            data.data_list.append(pb_classes.DataPair(a=one, b=two))

    # return information
    return data

# implement ElectricityData interface
class ElectrictyDataServicer(grpc_classes.ElectrictyDataServicer):
    # method to return the meter usage data (called by the client)
    def GetData(self, request, context):
        data = getMeterUsage()
        return data

# start the server
def serve():
    # create and start a grpc server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_classes.add_ElectrictyDataServicer_to_server(
        ElectrictyDataServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    # sleep-loop to wait for connections
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
