import os
import cs50
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/")
def pagprinc():
    return render_template("index.html")

@app.route("/emmaus")
def emmaus():
    return render_template("emmaus.html")

@app.route("/rn")
def rn():
    return render_template("rn.html")

@app.route("/c14")
def c14():
    return render_template("c14.html")

@app.route("/pret")
def pret():
    return render_template("pre-t.html")

@app.route("/info")
def info():
    return render_template("info.html")