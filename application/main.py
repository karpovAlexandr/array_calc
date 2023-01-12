from app_factory import create_app
from db import Base, engine

app = create_app()


@app.on_event("startup")
async def startup() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app")