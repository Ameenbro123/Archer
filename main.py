import pydexcom
import os
import sys
import json
import time
import datetime


# Loading the password and user
with open("userandpass.json","r") as f:
  user_data = json.load(f)

class main:
  # Getting the password and user from json
  password = json.dumps(user_data["password"]).replace("\"","")
  user = json.dumps(user_data["user"]).replace("\"","")
  # Getting the command and parsing
  def get_bloodsugar(user,password):
    usr = pydexcom.Dexcom(user,password)
    bg = usr.get_current_glucose_reading()
    return str(bg.value)+str(bg.trend_arrow)
  def get_cmd(): 
    inp = input("Archer > ")
    return inp
  def parse(cmd):
    if cmd == "exit":
      print("bye!")
      exit("[X] User requested exit")
    elif cmd == "bloodsugar":
      print(main.get_bloodsugar(main.user,main.password))
    if cmd == "time":
      print(datetime.datetime.now().strftime("%I:%M"))
    else:
      print("[X] Invalid command")
  
  # Mainloop
while True:
  cmd = main.get_cmd()
  main.parse(cmd)
