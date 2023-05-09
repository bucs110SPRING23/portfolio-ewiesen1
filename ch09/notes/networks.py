# network programming
# build a program that asks trivia questions

#server: any computerlsitening for incoming network connections
#request: an incoming connection that asks for some resource from the server
    #resources could be images, video, music, text, JSON, HTML

#types of requests
    #GET - a read operation
        #visiting a website, downloading a file, etc
    #PUT - a write operation (requires security)
        #logging in, deleting a file

#Headers
    #sent with request and the response
        #status codes - 200 (means everything went fine), 400 (resource requested could not be delivered), 500 (bad server code)
        #ip address
        #system information (geolocation)

#urllib

#Request library (HTTP for humans)

#API - application programmer's interface
#APIs can return data in any format, usually they return in JSON
    #want ones with no authorization
#URL parameters
    #? and &
    #binghamton.edu/cs?var1=100&var2="Hello"
        #where everything after the ? are variables

    

import requests

def main():
    response = requests.get("http://opentdb.com/api.php?amount=1&category=18")
    print (response.status_code)
    #print(response.headers)
    data = (response.json())
    print (data)

main()