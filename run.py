from flask import Flask
from flask import Response
#from flask_ngrok import run_with_ngrok #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku
import json

f = open('./anscombe.json')

geodata = json.load(f)

pelatihan_ibf_app = Flask(__name__)
#run_with_ngrok(pelatihan_ibf_app) #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku  

@pelatihan_ibf_app.route('/')
def send_json_data():
    return Response(response=json.dumps(geodata),
                    status=200,
                    mimetype="application/json")
    
@pelatihan_ibf_app.route('/other-route')
def send_json_data_other():
    geodataspec = geodata[2]
    return Response(response=json.dumps(geodataspec),
                    status=200,
                    mimetype="application/json")
    
@pelatihan_ibf_app.route('/other-route-two')
def send_json_data_other_two():
    geodataspec = geodata[1]["Series"]
    return Response(response=json.dumps(geodataspec),
                    status=200,
                    mimetype="application/json")


if __name__ == '__main__':
    pelatihan_ibf_app.run()