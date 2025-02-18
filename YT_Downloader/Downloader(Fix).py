#Import Section
import time



with open('creator_id.txt', 'r') as file:
    creator_id = file.read().strip()
    
    

print(f"Creator ID: {creator_id}")

time.sleep(3)

time.sleep(1)
for i in range (99):
        print ("")
print ("⏳ - CHECKING PYTUBE LIBRARY")
time.sleep(0.5)
print ("⏳ - CHECKING YT-DLP LIBRARY")
time.sleep(0.2)
print ("⏳ - SUBPROCESS LIBRARY")
time.sleep(0.2)
print ("⏳ - SYS LIBRARY")
time.sleep(0.2)
print ("⏳ - RE LIBRARY")
time.sleep(0.2)
print ("⏳ - TIME LIBRARY")
time.sleep(0.2)

time.sleep(1)
while True:
    while True:
        try:
            import time

            import subprocess
            import sys
            from pytube import YouTube  
            from pytube.exceptions import RegexMatchError
            from pytube.exceptions import VideoUnavailable
            from pytube import YouTube  
            import re
            import yt_dlp
            break  
        except ImportError as e:
            print("⏳ - SOME LIBRARY IS MISSING")
            
            time.sleep(1)
            print("⚠️ INSTALLING MISSING LIBRARY (Y/n)")
            time.sleep(1)
            

            user_input = input("[INPUT] : ").strip().lower()

            if user_input == "n":
                print("⚠️ -TO RUN THIS PROGRAM YOU NEED TO INSTALL SOME LIBRARY")
                time.sleep(1)
                print("⚠️ -PROGRAM CANCELLED")
                time.sleep(1)
                print("🛑 -EXITING...")
                raise SystemExit
            elif user_input == "y" or user_input == "":
                try:
                    subprocess.Popen(["cmd", "/K",sys.executable, "-m", "pip", "install", "pytube"])
                    subprocess.Popen(["cmd", "/K",sys.executable, "-m", "pip", "install", "yt-dlp"])
                    subprocess.Popen(["cmd", "/K",sys.executable, "-m", "pip", "install", "-U", "--pre", "yt-dlp[default]"])
                    subprocess.Popen(["cmd", "/K",sys.executable,"winget", "install", "Gyan.FFmpeg"])
                    subprocess.Popen(["cmd", "/K",sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
                    print("✅ - ALL LIBRARY INSTALLED SUCCESSFULLY")
                    time.sleep(1)
                except Exception as e:
                    print("📢 - PLEASE CHECK EROR CODE BELOW")
                    time.sleep(1)
                    print(f"⚠️ - FAILED TO INSTALL PYTUBE: {e}")
                    time.sleep(1)
                    raise SystemExit
            else:
                print("WRONG INPUT. ENTER TO RE-START.")
                time.sleep(1)
                continue
        except ValueError:
            print("WRONG INPUT. PLEASE TRY AGAIN.")
            time.sleep(1)
            continue
            
        
        
        
        

        print("✅ - PYTUBE LIBRARY INSTALLED SUCCESSFULLY")
        time.sleep(1)
        
    print ("✅ - NO MISSING LIBRARY")
    for i in range (99):
            print ("")
            
    print ("-------------------------------------")        
    print ("📢 - WELCOME TO YOUTUBE DOWNLOADER")
    print ("📢 - MAKE SURE COPY CLEAN LINK/URL ")
    print ("-------------------------------------")
    time.sleep(1)
    link = input("ENTER THE LINK OF THE VIDEO : ") 

    
    yt = YouTube(link)
            

            
    time.sleep(1)
    def get_video_info(link):
                try:
                    ydl_opts = {}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(link, download=False)
                        for i in range (40):
                            print ("")
                        print ("-------------------------------------------------------------")
                        print(f"\n🎬 Title: {info['title'][:30]}{'...' if len(info['title']) > 300 else ''}")
                        print(f"⏱️ Duration: {info['duration'] // 60} M {info['duration'] % 60} S")
                        print(f"👀 Views: {info['view_count']:,}")
                        print(f"📆 Release Date: {info['upload_date'][:4]}-{info['upload_date'][4:6]}-{info['upload_date'][6:]}")
                        print ("-------------------------------------------------------------")
                        time.sleep(3)
                        return
                except Exception as e:
                    print(f"❌EROR DETECTED: {e}")
                    
                    
                    
    retry = get_video_info(link)
    print("CHOOSE FILE TYPE TO INSTALL")
    print("1. MP4")
    print("2. MP3")
    user_choice = input(f"📢 [INPUT] : ")
    if user_choice == "1" :
            
            print("📢 - INSTALLING VIDEO")
            time.sleep(1)
            print("📢 - PLEASE WAIT")
            time.sleep(1)
            print("📢 - INSTALLING...")
            yt_dlp.YoutubeDL().download([link])
            time.sleep(1)
            print("📢 - INSTALLATION SUCCESSFUL")
            time.sleep(1)
            print("📢 - VIDEO INSTALLED")
            time.sleep(1)
            
    elif user_choice == "2":
            print("📢 - INSTALLING AUDIO")
            time.sleep(1)
            print("📢 - PLEASE WAIT")
            time.sleep(1)
            print("📢 - INSTALLING...")
            
            #LIMIT EDITTING AUDIO FORMAT ------------------------------------------------

            #YOU CAN EDIT THE QUALITY OF THE AUDIO BY CHANGING THE PREFERREDQUALITY VALUE
            #YOU CAN CHANGE THE FORMAT OF THE AUDIO BY CHANGING THE PREFERRED CODEC VALUE
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'MP3',  
                    'preferredquality': '192',
                }],
                'outtmpl': '%(title)s.%(ext)s',
            }
            #LIMIT EDITTING AUDIO FORMAT ------------------------------------------------
            
            
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            time.sleep(1)
            print("📢 - INSTALLATION SUCCESSFUL")
            time.sleep(1)
            print("📢 - AUDIO INSTALLED")
            time.sleep(1)

            
            
    elif user_choice == "":    
            print("📢 - INSTALLATION CANCELLED")
            time.sleep(1)
            print("📢 - EXITING...")
            
            raise SystemExit
        
    print ("DO YOU WANT TO INSTALL ANOTHER VIDEO Y/n")   
    restart = input("📢 [INPUT] : ")
    if restart == "Y" or restart == "y" or restart == "":
            link = input("Enter the link of the video: ") 
            get_video_info(link)
    elif restart == "n" or restart == "N":
            for i in range (99):
                print ("")
            print("📢 - INSTALLATION CANCELLED")
            time.sleep(0.3)
            print("📢 - EXITING...")
            time.sleep(0.3)
            
            raise SystemExit
    
            
    else :
            print("📢 - INSTALLATION CANCELLED")
            time.sleep(0.3)
            print("📢 - EXITING...")
            time.sleep(0.3)
            print("📢 - EXITED")
            time.sleep(0.3)
            print("📢 - THANK YOU")
            raise SystemExit
