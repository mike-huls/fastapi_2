from fastapi import APIRouter
from services.databaseConnection import DatabaseConnection
dbConnection = DatabaseConnection()


router_articles = APIRouter()


@router_articles.get("/all_articles")
def get_all_articles():
    return dbConnection.get_all_articles()

@router_articles.get("/article")
@router_articles.get("/article/{articleId}")
def get_one_article(articleId:int):
    return dbConnection.get_one_article(articleId=articleId)

@router_articles.delete("/article")
def delete_one_article(articleId:int):
    return dbConnection.delete_one_article(articleId=articleId)

@router_articles.post("/article")
def post_article(body:dict):
    return dbConnection.post_article(articleJson=body)

@router_articles.put("/article")
@router_articles.put("/article/{articleId}")
def update_article(articleId:int, body:dict):
    return dbConnection.update_article(articleId=articleId, articleJson=body)
