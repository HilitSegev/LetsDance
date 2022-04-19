from pymongo import MongoClient


class DB:

    def __init__(self):
        self.db = None
        self.connect()

    def connect(self):
        try:
            #conn = MongoClient('localhost', 27017)
            client = MongoClient()
        except:
            print("could not connect to MongoDB")
            return
        self.db = client['LetsDance']
        #self.db = conn.LetsDance

    # def upload_video_frames(self, picture_path, picture_name, frames_num):
    #     #print(self.db.get_collection('Pictures'))
    #     collection = self.db.Pictures
    #     record = {"name": picture_name}
    #     path = picture_path + "\\frame.jpg"
    #     for i in range(frames_num):
    #         record["frame" + str(i) + "_location"] = path + str(i)
    #     rec_id = collection.insert_one(record)
    #     print(record)
    #     print(rec_id)

    def upload_video_frames(self, picture_path, video_name, frames_num):
        #print(self.db.get_collection('Pictures'))
        collection = self.db.Pictures
        last_frame_path = picture_path + "\\frame" + str(frames_num-1) + ".jpg"
        record = {"name": video_name, "frames_dir": picture_path,
                  "last_frame_path": last_frame_path, "num_of_frames": frames_num}
        rec_id = collection.insert_one(record)
        print(record)
        print(rec_id)



