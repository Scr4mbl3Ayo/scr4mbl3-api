from fastapi import FastAPI
from fastapi.responses import JSONResponse
from encoder import shift_cipher
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all domains (public usage)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allow requests from any domain
    allow_credentials=True,
    allow_methods=["*"],      # Allow GET, POST, etc.
    allow_headers=["*"],      # Allow custom headers
)

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

