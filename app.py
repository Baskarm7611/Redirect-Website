from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import os
import random
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

DL_WEBSITE_DOMAIN = os.environ.get("DL_WEBSITE_DOMAIN")
FS_WEBSITE_DOMAIN = [x.strip() for x in os.environ.get("FS_WEBSITE_DOMAIN").split()]
PORT = int(os.environ.get("PORT", 80))


@app.get("/store/{path:path}")
async def file_store(path: str):
    url = f"https://telegram.me/THDT_FP3bot?start={path}"
    return RedirectResponse(url)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
