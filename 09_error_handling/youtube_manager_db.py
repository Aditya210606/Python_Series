import sqlite3

conn = sqlite3.connect('youtube_video.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS videos(
                             id INTEGER PRIMARY KEY,
                             name TEXT NOT NULL,
                             time TEXT NOT NULL
     )
''')

def list_video():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    conn.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?",(video_id,new_name,new_time))
    conn.commit()

def delete_video(video_id):
    conn.execute("DELETE FROM videos WHERE id = ? ",(video_id,)) # imp put, then only it is consider as tuple 

def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List  videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video ")
        print("5. Exit the app")
        choice = input("Enter the choice: ")

        if choice == '1':
            list_video()

        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)

        elif choice == '3':
            video_id = input("Enter the video_id: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id,name,time)

        elif choice =='4':
            video_id = input("Enter the video_id to delete: ")
            delete_video(video_id)
            
        elif choice == '5':
            break

        else:
            print("Invalid choice")               

    conn.close()
    

if __name__=="__main__":
    main()

