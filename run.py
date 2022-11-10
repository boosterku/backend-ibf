from flask import Flask
#from flask_ngrok import run_with_ngrok #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku
from flask import request
from flask import Response
import json
import copy
from flask_cors import CORS

geo=[]

main = Flask(__name__)
CORS(main)
#run_with_ngrok(main)

fileAbout='./about.json'
fileKI='./ki.geojson'
fileRH='./rh.geojson'
fileMSLP='./mslp.geojson'
fileTP='./tp.geojson'

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

@main.route('/query')
def display_query():
    parameter = request.args.get('parameter')
    value = request.args.get('value')
    operator = request.args.get('operator')
    
    fileOpen=f"./{parameter}.geojson"
    variabel=openJSON(fileOpen)
    features=variabel["features"]
  
    if operator=='lebihdari':
      dataquery = [p for p in features if p["properties"]["value"] > int(value)]
    elif operator=='kurangdari':
      dataquery = [p for p in features if p["properties"]["value"] < int(value)]
    elif operator=='samadengan':
      dataquery = [p for p in features if p["properties"]["value"] == int(value)]
    
    return Response(response=json.dumps(dataquery),
                    status=200,
                    mimetype="application/json")

@main.route('/add', methods=["POST"])
def add_status():
    try:
      req = json.loads(request.data)
      geo.append(copy.copy(req))
      return Response(response=json.dumps(geo),
                      status=200,
                      mimetype="application/json")
    except:
      res = {
          "error": True,
          "message": "Unable to find data"
      }
      return Response(response=json.dumps(res),
                    status=404,
                    mimetype="application/json")

@main.route('/get', methods=["GET"])
def send_status():
    try:
      return Response(response=json.dumps(geo),
                      status=200,
                      mimetype="application/json")
    except:
      res = {
          "error": True,
          "message": "Unable to find data"
      }
      return Response(response=json.dumps(res),
                    status=404,
                    mimetype="application/json")

@main.route('/query')
def sent_status():                    
      tipe = request.args.get('tipe')
      category = request.args.get('category')

      dataquery = [p for p in geo if p["properties"]["category"] == int(category)] #perhatikan jenis variable

      return Response(response=json.dumps(dataquery),
                      status=200,
                      mimetype="application/json")
       


if __name__ == '__main__':
    main.run()