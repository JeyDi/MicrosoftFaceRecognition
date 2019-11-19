from functions.camera import cameraCapture
from functions.config import define_path, read_yaml_config
from functions.faceapi import auth_client

def main():
    #Define path and read the config file
    path = define_path()
    sub_key, endpoint = read_yaml_config(path)

    #Authenticate and create the client
    client = auth_client(sub_key,endpoint)

    #Capture frame with pc camera
    cameraCapture(client)

    pass


if __name__ == "__main__":
    print("Starting...")
    main()