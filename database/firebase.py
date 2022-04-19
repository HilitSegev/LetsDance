import os
from firebase_admin import credentials, initialize_app, storage
from google.cloud import storage
#from firebase import firebase
from oauth2client.service_account import ServiceAccountCredentials
import pyrebase
import certifi

x = certifi.where()

def upload_photo():
    config = {
        apiKey: "AIzaSyCA1sPXraANkU16aa5HfPlA8fHua-Q55AI",
        autoDomain: "let-s-dance-a0be2.firebaseapp.com",
        databaseURL: ""
    }

#def upload_to_bucket("""blob_name, path_to_file, bucket_name"""):
def upload_to_bucket():

    """ Upload data to a bucket"""
    my_path = os.getcwd()
    os.chdir(my_path + '\\database')

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        'lets-dance-341700-cd06afdb4558.json')

    #print(buckets = list(storage_client.list_buckets())

    bucket = storage_client.get_bucket('my-bucket')
    blob = bucket.blob('frame.jpg')
    blob.upload_from_filename('frame.jpg')

    #returns a public url
    os.chdir(my_path)
    return blob.public_url


def upload_photo2(photo_name):

    firebase = firebase.F
    my_path = os.getcwd()
    os.chdir(my_path+'\\database')
    # Init firebase with your credentials
    cred = credentials.Certificate("lets-dance-341700-cd06afdb4558.json")
    initialize_app(cred, {'storageBucket': 'let-s-dance-a0be2.appspot.com'})

    # Put your local file path
    fileName = photo_name
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("your file url", blob.public_url)
    os.chdir(my_path)

def upload_photo(photo_name):
    my_path = os.getcwd()
    os.chdir(my_path+'\\database')
    # Init firebase with your credentials
    cred = credentials.Certificate("lets-dance-341700-cd06afdb4558.json")
    initialize_app(cred, {'storageBucket': 'let-s-dance-a0be2.appspot.com'})

    # Put your local file path
    fileName = photo_name
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("your file url", blob.public_url)
    os.chdir(my_path)