"""Serve the shop's web page."""
import os

from flask import Flask

from build import ITEMS, page

app = Flask(__name__)
VERSION = os.environ.get("VERSION", "dev")
@app.route("/")
def home():
    return page(ITEMS, VERSION)
@app.route("/health")
def health():
    return {"status": "ok"}