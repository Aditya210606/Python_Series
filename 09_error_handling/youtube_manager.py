import json


def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file) 
                 
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)    

def List_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos,start=1) :
        print(f"{index}. {video['name']}, 'Duration':{video['time']}") 
    print("*" * 50)

def add_video(videos):
    name = input("Enter video name:")
    time = input("Enter video time:")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    List_all_videos(videos)
    index =  int(input("Enter the video number to update:"))
    if 1<= index <= len(videos):
        name = input("Enter the new video name : ")
        time = input("Enter the new video time : ")
        videos[index-1] = {'name':name , 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected !!")    

    
def delete_video(videos):
    List_all_videos(videos)
    index = int(input("Enter the video number to delete:"))
   
    if 1 <= index <= len(videos):
       del videos[index-1]      # used index-1 because python counts from [0]
       save_data_helper(videos)
       print(f"{index}. video deleted !!") # del is used to delete reference of an object
    else :
       print("Invalid number selected !!")


def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager  |  Choose a option")
        print("1. List a favourite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video ")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        #print(videos)

        match choice:
            case '1':
                List_all_videos(videos) 
            case '2':
                add_video(videos) 
            case '3':
                update_video(videos) 
            case '4':
                delete_video(videos) 
            case '5':
                break   
            case _:        # any other input 
                print("Invalid choice")        

if __name__ == "__main__" :
    main()       # if only main than function reference is printed
                 # if main() then function is called 

