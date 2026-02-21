# import pymongo 
from pymongo import MongoClient # because of this no need to write pymongo. again and again
from bson import ObjectId  # imported because pymongo is handling id as a string by importing this now it a  refered as ObjectedId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.cqqcut1.mongodb.net/") # after / we can put database name 
        #  Not a good idea to include id and password in code files

db = client["ytmanager"]   
video_collection = db["videos"]     


# print(video_collection)

def list_videos():
     for video in video_collection.find({}):
         print(f"ID: {ObjectId(video['_id'])}, Name : {video['name']}, and Time : {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name": name , "time": time})

def update_video(video_id,name,time):
    video_collection.update_one({'_id':ObjectId(video_id)},{'$set': {"new_name":name ,"new_time": time}})
     

def delete_video(video_id):
    video_collection.delete_one({'_id':ObjectId(video_id)})

def main ():

    while True:
        print("\nYoutube manager")
        print("1. List all video  ")
        print("2. Add a new video  ")
        print("3. Update a video ")
        print("4. Delete a video ")
        print("5 .Exit the app")

        choice = (input("Enter your choice : "))

        if choice == '1':
            list_videos()

        elif choice =='2':
            name = (input("Enter video name :"))    
            time = (input("Enter video time :")) 
            add_video(name,time) 

        elif choice == '3':
            video_id = (input("Enter the video_id : "))
            name = (input("Enter new video name :"))    
            time = (input("Enter new video time :")) 
            update_video(video_id,name,time) 

        elif choice == '4':
            video_id = (input("Enter the video_id to delete : "))  
            delete_video(video_id)  

        elif choice == '5':
            break  

        else :
            print("Invalid choice")  
 
if __name__ =="__main__":
    main()