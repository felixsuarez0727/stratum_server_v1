# Author: Felix Suarez Bonilla

import psycopg2
from flask import Flask
from flask_jsonrpc import JSONRPC

# Global Vars
id_auth=0

# Flask Application
app = Flask(__name__)

# Flask-JSONRPC
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

# Connect with Table.
conn = psycopg2.connect(host="localhost", database="luxor", user="luxor", password="luxor", port="5432")
cursor = conn.cursor()

@jsonrpc.method('mining.authorize')
def index(user: str, password: str) -> str:
    ++id_auth

    # Modify DB.
    params = user + ',' + password
    sqlInsertRow = "INSERT INTO dev_1 values(" + str(id_auth)  + ", 'mining.authorize', '"+ params +"', 'True')";
    cursor.execute(sqlInsertRow)
    conn.commit()

    return 'True'

@jsonrpc.method('mining.subscribe')
def index(agent_version1: str) -> str:
    return '[[["mining.set_difficulty", "subscription id 1"], ["mining.notify", "subscription id 2"]], "extranonce1", extranonce2_size]'

@jsonrpc.method('mining.notify')
def index() -> str:
    return '["bf", "4d16b6f85af6e2198f44ae2a6de67f78487ae5611b77c6c0440b921e00000000", "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff20020862062f503253482f04b8864e5008", "072f736c7573682f000000000100f2052a010000001976a914d23fcdf86f7e756a64a7a9688ef9903327048ed988ac00000000", [], "00000002", "1c2ac4af", "504e86b9", false]'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
