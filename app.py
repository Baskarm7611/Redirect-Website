from quart import Quart, redirect, request
import os
import random
from dotenv import load_dotenv

load_dotenv()

app = Quart(name)

DL_WEBSITE_DOMAIN = os.environ.get("DL_WEBSITE_DOMAIN")
FS_WEBSITE_DOMAIN = [x.strip() for x in os.environ.get("FS_WEBSITE_DOMAIN").split()]
PORT = int(os.environ.get("PORT", 80))


@app.route("/dl/<path:path>")
async def home(path):
    url = request.url.replace(f"{request.host}/dl/{path}", DL_WEBSITE_DOMAIN)
    return redirect(url)


@app.route("/fs/")
async def fs_home():
    domain = random.choice(FS_WEBSITE_DOMAIN)
    url = request.url.replace(f"{request.host}/fs", domain)
    return redirect(url)
    
@app.route("/store/<path:path>")
async def file_store(path):
    url = f"https://telegram.me/THDT_FP3bot?start={path}"
    return redirect(url)


if name == "main":
    app.run(host="0.0.0.0", port=PORT)
