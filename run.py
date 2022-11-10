from flask import Flask
#from flask_ngrok import run_with_ngrok #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku
from flask import request
from flask import Response
import json
import copy
from flask_cors import CORS

geo=[]

pelatihan_ibf_app = Flask(__name__)
CORS(pelatihan_ibf_app)
#run_with_ngrok(pelatihan_ibf_app) #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku  

@pelatihan_ibf_app.route('/add', methods=["POST"])
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

@pelatihan_ibf_app.route('/get', methods=["GET"])
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

@pelatihan_ibf_app.route('/query')
def sent_status():                    
      tipe = request.args.get('tipe')
      category = request.args.get('category')

      dataquery = [p for p in geo if p["properties"]["category"] == int(category)] #perhatikan jenis variable

      return Response(response=json.dumps(dataquery),
                      status=200,
                      mimetype="application/json")
       


if __name__ == '__main__':
    pelatihan_ibf_app.run()