# SoundcloudLikesFetcher
Python script to get a file contains names and links to all of my liked songs on Soundcloud.

## How to use
### Video
https://youtu.be/iTiG6xuIB8U

### Steps
- Go to your Soundcloud likes webpage at this link https://soundcloud.com/you/likes
- If you have a long list of likes, scroll all the way to the bottom untill every song is loaded
- Save the webpage to your computer by choosing File -> Save Page As
- Open the .html file and delete the line starting with <style>.signinForm, it's probably on line 77
- Change the .html file name to soundcloud.txt
- Download the script.py file and put it in the same folder as the web page that you downloaded
- Open the Terminal and run the script with "python3 script.py"
- The script will output a file named output.csv and that's your file

