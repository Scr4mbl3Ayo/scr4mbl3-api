from fastapi import FastAPI
from fastapi.responses import JSONResponse
from encoder import shift_cipher

app = FastAPI()

@app.post("/encode")
async def encode(payload: dict):
    try:
        text = payload["text"]
        shifts = payload["shifts"]
        direction = payload.get("direction", 1)

        if isinstance(shifts, str):
            shifts = [int(x.strip()) for x in shifts.split(",") if x.strip()]

        result = shift_cipher(text, shifts, int(direction))
        return {"result": result}

    except Exception as e:
        return JSONResponse(
            status_code=200,
            content={"error": str(e)}
        )
