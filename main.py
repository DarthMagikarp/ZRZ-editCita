# chat conversation
import json
import pymysql
import requests
import http.client
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from itertools import cycle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def function(self):
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_DDBB = os.getenv("DB_DDBB")
    #try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DDBB)
    cursor = connection.cursor()

    print("conexión exitosa")

    sql = '''
        update ZRZ2.citas set
            profesional_id = '''+request.json['profesional_id']+''',
            alumno_id = '''+request.json['alumno_id']+''',
            fecha = "'''+request.json['fecha']+'''",
            hora = "'''+request.json['hora']+'''",
            estado = "'''+request.json['estado']+'''",
            modalidad = "'''+request.json['modalidad']+'''",
            campus = "'''+request.json['campus']+'''",
            notas = "'''+request.json['notas']+'''",
            motivo = "'''+request.json['motivo']+'''",
            como = "'''+request.json['como']+'''",
            derivado_desde = "'''+request.json['derivado_desde']+'''",
            tratamiento = "'''+request.json['tratamiento']+'''"
        WHERE (profesional_id = %s and alumno_id = %s);
    '''
    print(sql)
    cursor.execute(sql, (request.json['profesional_id'], request.json['alumno_id']))
    connection.commit()
    retorno = {           
            "detalle":"success!!!"
        }
    return retorno

    #except Exception as e:
    #    print('Error: '+ str(e))
    #    retorno = {           
    #        "detalle":"algo falló", 
    #        "validacion":False
    #    }
    #    return retorno

if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')