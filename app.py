# Simple EventStream and Handling
#
# @author: Edgar Han
# @date: 18/08/2019
# @email: edgar.h.han@gmail.com

from flask import Flask, session, redirect, url_for, escape, request, render_template, Response, Markup, send_from_directory
import json, time, threading, logging

# ==================================================================
# GLOBAL VARS
# ==================================================================

app = Flask(__name__)
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

@app.route('/')
def main():
    return render_template('index.html')

@app.route("/stream")
def stream():
    def eventStream():
        global message
        while True:
            message = "{}: hello".format(time.time())
            logging.info(message)
            yield "data: {}\n\n".format(message)
            time.sleep(1) # replace this with mutex
    return Response(eventStream(), mimetype="text/event-stream")
