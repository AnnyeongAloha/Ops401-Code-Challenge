# Ops401 Code Challenge Day 37 
# Justin 'Sage'
# Utilized Demo Code and ChatGPT


#!/usr/bin/env python3

import requests

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp"  # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster():
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

def save_response_as_html(response):
    with open("response.html", "w") as file:
        file.write(response.text)

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and receive an HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)

# Generate a .html file to capture the contents of the HTTP response
save_response_as_html(response_with_cookie)

# Open the HTML file with Firefox
import webbrowser
webbrowser.get("firefox").open("response.html")
