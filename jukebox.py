from mfrc522 import SimpleMFRC522
import lgpio
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

h = lgpio.gpiochip_open(0)
DEVICE_ID="YOUR_DEVICE_ID"
CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"

while True:
  try:
    reader=SimpleMFRC522()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:8080", scope="user-read-playback-state,user-modify-playback-state"))
        
    devices = sp.devices()
    if not any(device['id'] == DEVICE_ID for device in devices['devices']):
      print(f"Can't find device ID: {DEVICE_ID}.")
      continue
        
    while True:
      print("Waiting for record scan...")
      id= reader.read()[0]
      print("Card Value is:",id)
      sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
      # DONT include the quotation marks around the card's ID value, just paste the number
        
      if (id==CARD_ID1):
        sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:track:..')
          sleep(2)
        
      elif (id==CARD_ID2):
        sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:...')
          sleep(2)
            
        #. . . for elif statements for your songs/albums
        #Note: for both spotify tracks and albums, copy the code after "track/" or "album" and before "?si". Paste it in the ... above.

    except Exception as e:
      print(e)
      pass
    
    finally:
      print("Cleaning up...")
      #GPIO.cleanup()
      lgpio.gpiochip_close(h)
