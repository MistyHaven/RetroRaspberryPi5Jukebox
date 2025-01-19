# Raspberry-Pi-5-Retro-Game-Jukebox
A Raspberry Pi 5 jukebox that plays retro video game music by scanning a RFID card. :)

Credits: 
- Heavily inspired by talaexe's video "Modern Day Record Player Tutorial (RFID, Spotify API, Python, and Raspberry Pi)" over on Youtube.
- 

List of "Ingredients":
  - Female to Female wires
  - RFID scanner
  - Header pins
  - Raspberry pi 5
  - RFID cards

Requirements:
  - Make sure you have a Spotify Premium account!
  - The package that we will download for the project only works if you have a premium account.

Steps:

1) Prepare the pie!
   - First, make sure to update your Pi by pasting the following code in terminal:

  Code:   
```
sudo apt-get update
sudo apt-get upgrade
```  
   - Then, we'll need to edit configurations. You can do so by pasting the following code:

 Code:
```   
sudo raspi-config
```     
   - This will take you to the Raspberry Pi's Configuration Tool. There, press "Interface Options" and select "SPI". Press "Yes". Now, press "finish" in order to exit the Configuration Tool.           However, in order for the selection to be updated, you'll need to reboot your Raspberry Pi.

  Code:   
```
sudo reboot
```
   - After successfully rebooting your Pi, we will make sure to update our python 3. Don't worry if the terminal will print you a warning.

  Code:   
```
sudo apt-get install python3-dev python3-pip
```    
   - Download mfrc522, spidev and lgpio libraries
     - Since the raspberry pi 5 doesn't allow to directly use commands like "sudo pip3 install spidev" for ex, we'll need to create a virtual environment.   

  Code:   
```
python3 -m venv rfid_env
source rfid_env/bin/activate
pip install spidev
```  
1) Prepare the hardware!
   - Connect the Pi to RFID scanner
   - Picture of Raspberry pi GPIOs
   - List of wires to connect to pins:
     - SDA = GPIO8
     - SCK = GPIO11
     - MOSI = GPIO10
     - MISO = GPIO9
     - IRQ = nothing
     - GND = GND
     - RST = GPIO23
     - 3.3v = 3v3 Power
    ![image](https://github.com/user-attachments/assets/6fa06086-f022-42df-89c3-68cffb245242)

4) Create our first python file "reader.py":
   - Very simple code => we'll need this in order to determine the ids of our RFID cards
   - Firstly, we'll create a folder in documents called "retrojukebox"
   - Then create a file in the previous folder. Name it however you wish. I simply went with "reader.py" for simplicity.
   - Open Thonny and write code in "reader.py" (in repo).
   - Given that the Raspberry Pi 5 doesn't support the GPIO module, we'll use thee lgpio instead. It gives the same result.
   - In Thonny, go to "tools" then "options". In "options", press "interpretor". You'll see a button called "Python executable" => press the three dots button and select the path leading to the       python3 folder in your rfid_env that you          created preivously. 
   - Run the code. Once the expected message appears in the console, tap your card => this will give the id for that specific card. Make sure to note it down for later use.

5) Connecting to the Spotify API:
   - Before connecting to the Spotify API, make sure to install the "Spotipy library" - this will allow you to use the API with python.
   - Here, we will use "raspotify" by dtcooper: https://github.com/dtcooper/raspotify
   - Paste the following line of code (from dtcooper's github) into the terminal:
   
   Code:     
```
sudo apt-get -y install curl && curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
```
   - After the download is finished, open your spotify on any device and check your device connections. You should see your raspberry pi there!

6) Creating a project in the Spotify Developer API:
   - Now, you'll need to make create a project in "Spotify for Developers". Make sure that you have an account.
   - Once signed in, go to Dashboard and press "Create app".
   - Then, you'll need to fill in the name, descriptions etc.
     - For simplicity, I called my app "Retro Jukebox", and gave it a brief bio, but you can call it whatever you like.
     - For the Redirect URIs, you'll need to add two:
       1)  http://localhost:8888/callback
       2)  http://localhost:8080
    => 1) will handle redirected responses, will tell the server where to send user after authentication, while 2) serves as the starting point for the app.
   - After creating your app, you'll need to note down its "Client ID" and "Client Secret". These are REALLY important and will help you in the authentication process.
   - By the way, don't forget to connect your Raspberry Pi 5 to your Spotify!!


7) Spotify API Token Setup:
   a) Authentication code:
   - For me, this was the hardest step.
   - First, you will first need to obtain an Authentication code. Without it, you won't be able to receive a token!
   - Make sure that Flask is installed - usually it is by default, but if not, try writing "sudo apt install python3-flask" in the terminal.
   - Write and run the code in "app.py" (in repo) in Thonny.
   - With this code, we have created a server.
   - Now, print the following URL in your browser:
     -  https://accounts.spotify.com/authorize?client_id=CLIENT_ID&response_type=code&redirect_uri=http://localhost:8888/callback&scope=user-read-playback-state
     -  Replace "CLIENT_ID" with your client id. 
   - If successful, you would see the Authentication code. Write it down.
  b) Access Token:
   - Now, to obtain an access token, write and run the code in "requests.py" (in repo).
   - If done correctly, you should see the access token (as well as the refresh token) printed in your console.
   - Write it done please.
   - You'll need to hurry since the token will expire in an hour after its creaion!!

  c) Device id:
   - Now that you have your access token, you'll need to obtain your device id.This will Spotify to play your song after tapping your RFID card to the scanner
   - Write and run the following cude in the terminal:
  
  Code:   
```
curl --request GET \
    --url https://api.spotify.com/v1/me/player/devices \
    --header 'Authorization: Bearer ACCESS_TOKEN'
```
   - You should see your device id listed after running the previous code. Write it down.

8) Last step: Making the jukebox
  - We're almost done.
  - Now, you have everything ready to write the actualy code for your retro video game jukebox!
  - Write the code in "jukebox.py" in Thonny:
  - Run the code and tap your card to the RFID scanner. It should now work!!
  - The options are limitless -- if you happen to have 1000 RFID cards, you then can play 100 different songs and albums (although that would be a lot of work...)
  - Thank you for making it this far! Great job!!
  - Again, I would like to thank talaexe on Youtube for inspiring this project.
  
9) BONUS:
  - For those feeling a tad bit creative, I suggest you decorate your jukebox!
  - For example, you can print the covers of various classic video game titles/albums and stick it to your RFID cards. Don't worry, they still work ;)

![20250115_172740](https://github.com/user-attachments/assets/44a30b16-654f-49d5-80bc-db3531058d84)


  - You can also make the jukebox using a wooden, plastic or even cardboard box.
  - Here's a picture of my little jukebox! She's not the fanciest, but it's the idea that counts :b
    
![20250115_170410](https://github.com/user-attachments/assets/48893b5f-c483-4dfb-a775-7ea1067cec8d)

  - If you'd like to see the the jukebox in action, please watch the video on my channel: https://youtu.be/cQe-NdvQzg8 
    
      
    
  - Of course, this step is not necessary, but if you want to have a little more fun, go for it!


    




   
  
   
