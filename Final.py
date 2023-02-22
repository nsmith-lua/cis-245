#Noah Smith
#2/18/23
#Python Basics


import json, requests

going = ("1")

def main():
  
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  appid = "1b4b625a0cd453d466e65ce85d0bfb3a"
  try:
    city = input("Please select a city: ")
    url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
    print(url)
    print()

    response = requests.get(url)
    unformated_data = response.json()
    def getTemp():
      temp = unformated_data["main"]["temp"]
      print(f"The current temp is {temp}")

    def getTempMax():
      temp_max = unformated_data["main"]["temp_max"]
      print(f"The max temp is {temp_max}")
  

    #print(unformated_data)
    
    getTemp()
    getTempMax()
    print(f"Connection to {city} successful")


  #try:
    #city = input("Please select a city: ")

  except:
    print("Try again, invalid value")


  
def ender(going):
  going = input("Press 1 to try another, 2 to end the program: ")

while going == "1":
  main()
  #city = input("Please select a city: ")
  #getTemp()
  #getTempMax()
  #ender()
  going = input("Press 1 to try another, 2 to end the program: ")
  
  