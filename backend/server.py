from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return "Hey there. Thanks for checking out the link. Truth is it's not quite ready, got a bit busy with sick kids and planleggingsdag so I've had less time this week, but I wanted to send in the application with the link before the deadline. Check back in a few days :)"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
