from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.user import user_router
from domain.message import message_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for r in [user_router.router, message_router.router]:
    app.include_router(r)


@app.get("/")
def main():
    return {"main" :"hello"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost" , port=8000, reload=True)