from flask import Flask
from flask import Response
from flask import request
#from flask_ngrok import run_with_ngrok
import json

main = Flask(_name_)
#run_with_ngrok(main)

fileAbout='./about.json'
fileKI='./ki_clip.geojson'
fileRH='./rh_clip_more70.geojson'
fileMSLP='./mslp_clip.geojson'
fileTP='./tp_clip_more0.geojson'

def openJSON(file):
  with open(file) as f:
    content=json.load(f)
  return content

@main.route("/")
def helloWorld():
  about=openJSON(fileAbout)
  return Response(response=json.dumps(about),
                    status=200,
                    mimetype="application/json")

@main.route("/ki")
def displayKI():
  ki=openJSON(fileKI)
  return Response(response=json.dumps(ki),
                    status=200,
                    mimetype="application/json")

@main.route("/rh")
def displayRH():
  rh=openJSON(fileRH)
  return Response(response=json.dumps(rh),
                    status=200,
                    mimetype="application/json")

@main.route("/mslp")
def displayMSLP():
  mslp=openJSON(fileMSLP)
  return Response(response=json.dumps(mslp),
                    status=200,
                    mimetype="application/json")

@main.route("/tp")
def displayTP():
  tp=openJSON(fileTP)
  return Response(response=json.dumps(tp),
                    status=200,
                    mimetype="application/json")

if _name_ == '_main_':
  main.run()