from flask import Flask, redirect, request
import os
import random
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

DL_WEBSITE_DOMAIN = os.environ.get("DL_WEBSITE_DOMAIN")
FS_WEBSITE_DOMAIN = [x.strip() for x in os.environ.get("FS_WEBSITE_DOMAIN").split()]
PORT = int(os.environ.get("PORT", 80))


@app.route("/dl/")
def home(path):
    url = request.url.replace(f"{request.host}/dl", DL_WEBSITE_DOMAIN)
    return redirect(url)


@app.route("/fs/")
def fs_home():
    domain = random.choice(FS_WEBSITE_DOMAIN)
    url = request.url.replace(f"{request.host}/fs", domain)
    return redirect(url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
