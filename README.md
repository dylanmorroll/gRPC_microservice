# gRPC_microservice
## Spectral Technical Task

First I created a gRPC server client structure in Python. To do this I wrote the electricity_data.proto file to describe the interaction the client would have with the server - send an empty request to the server and have the data returned in the appropriate format (a Data message containing two strings and a list of DataPair messages). From this proto file I used gRPC to generate the electricity_data_pb2.py and electricity_data_pb2_grpc.py files. Once these files had been created I implemented the ElectricityDataServicer interface in electricity_data_server.py. This fetches the data from the file, creates the appropriate objects for it using the generated classes, then sends it to the connecting client.

To complement this I created the electricty_data_client.py file to generate a stub from the server and retrieve the data information. Once I had this gRPC server and client set up, I modified the electricty_data_client.py to also start a Flask server. Now, when ran, it starts a server of it's own which can be accessed from a web browser. When the page is accessed it pulls the data from the gRPC server (this way it allows the latest information to be pulled from the gRPC server in case the data has been modified since the Flask server started), converts it into a JSON string, and passes it to the web page.

Finally I then created a web page that takes the JSON data that is passed from the server and parses it using javascript. Once it is parsed it uses the information to generate a table so it is in a digestable format.
