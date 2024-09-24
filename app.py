from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import os
import random
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

PORT = int(os.environ.get("PORT", 80))


@app.get("/store/{path:path}")
async def file_store(path: str):
    url = f"https://telegram.me/THDT_FP3bot?start={path}"
    return RedirectResponse(url)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
