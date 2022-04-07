from fastapi import FastAPI
import routertest

app = FastAPI(
    title='build test page'
)

app.include_router(routertest.router)