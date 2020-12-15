import instaloader
import telegram_send
import time

print("Starting")
L = instaloader.Instaloader(download_comments=False, max_connection_attempts=9, post_metadata_txt_pattern=None, save_metadata=False, download_video_thumbnails=False, download_geotags=False, filename_pattern="{shortcode}")
print("Login")
BOT_INSTAGRAM_ACCOUNT = L.login("username","password")
print("Login successful")

PROFILES = ["tackleberry_84", "nervozni_pingvin", "otac_branislav", "gangsteritogroup", "ptica.drkacica", "ludkoleptir", "kojavitez1981", "trkacko_pile", "gospodar_prsljenova", "golman_u_penziji", "riba.cekicara"]

while True:

 try:

   for PROFILE in PROFILES:
    
    print("Profile: "+PROFILE)
    print("Timeout: 34 seconds")
    time.sleep(34)
    profile = instaloader.Profile.from_username(L.context, PROFILE)
    print("Profile loaded")
    Loop = 0
    for post in profile.get_posts():
        Loop = Loop + 1
        print("Timeout: 34 seconds")
        time.sleep(34)
        download = L.download_post(post, PROFILE)
        if download == True:
            video = post.is_video
            if video == True:
                try:
                    with open(post.owner_username+"/"+post.shortcode+".mp4", "rb") as f:
                         telegram_send.send(files=[f], timeout=240)
                         if post.caption is None:
                                telegram_send.send(images=None, messages=[""+post.owner_username+": None"], timeout=240)
                         else:
                                telegram_send.send(images=None, messages=[""+post.owner_username+": "+post.caption+""], timeout=240)
                except:
                    pass
            else:
                try:
                    with open(post.owner_username+"/"+post.shortcode+".jpg", "rb") as f:
                         telegram_send.send(images=[f], timeout=240)
                         if post.caption is None:
                                telegram_send.send(images=None, messages=[""+post.owner_username+": None"], timeout=240)
                         else:
                                telegram_send.send(images=None, messages=[""+post.owner_username+": "+post.caption+""], timeout=240) 
                except:
                    pass
        else:
            break
        if Loop >= 5:
            break  
    print("Next")   
    
 except:
     pass


