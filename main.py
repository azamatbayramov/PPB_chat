from fastapi import FastAPI, HTTPException

app = FastAPI()

memes_count = 0
memes = {}


@app.get("/memes/{id}")
async def get_meme(id: int):
    if memes.get(id) is None:
        raise HTTPException(status_code=404)

    return {
        "id": id,
        "text": memes[id]
    }


@app.post("/memes")
async def create_meme(text: str):
    global memes_count
    memes_count += 1
    memes[memes_count] = text
    return {
        "id": memes_count,
        "text": text
    }


@app.delete("/memes/{id}")
async def delete_meme(id: int):
    if memes.get(id) is None:
        raise HTTPException(status_code=404)

    del memes[id]
    return {"message": "OK"}


@app.put("/memes/{id}")
async def update_meme(id: int, text: str):
    if memes.get(id) is None:
        raise HTTPException(status_code=404)

    old_text = memes[id]
    memes[id] = text
    return {
        "old": {
            "id": id,
            "text": old_text
        },
        "new": {
            "id": id,
            "text": text
        }
    }


@app.get("/memes")
async def get_all_memes():
    return [{"id": key, "text": memes[key]} for key in memes.keys()]
