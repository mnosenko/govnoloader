from flask import Flask
import os
from datetime import datetime
from base64 import b64encode


app = Flask(__name__)
data_size = int(os.environ.get('APP_RETURN_DATA_SIZE', 100)) #return data size in MB
wait_time = int(os.environ.get('APP_WAIT_TIME_TO_RESPONSE', 10)) 


def generate_data(starttime, data_size: int, wait_time: int):
    answer = b64encode(os.urandom(data_size*1024*1024)).decode('utf-8')
    delta = datetime.utcnow() - starttime
    if delta.seconds < wait_time:
        return generate_data(starttime, data_size, wait_time)
    return answer


@app.route('/')
def main():
    starttime = datetime.utcnow()
    return generate_data(starttime, data_size, wait_time)


