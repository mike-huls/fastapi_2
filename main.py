from fastapi import FastAPI
from routes.article_routes import router_articles

app = FastAPI()

app.include_router(router=router_articles, prefix='/articles')
