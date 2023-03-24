class DatabaseConnection(object):
    articles = []

    def __init__(self):
        self.articles = [
            {
                "id": 1,
                "name": "Docker Compose for absolute beginners",
                "url": "https://mikehuls.medium.com/docker-compose-for-absolute-beginners-how-does-it-work-and-how-to-use-it-examples-733ca24c5e6c",
                "publication_date": "2021-08-23"
            }, {
                "id": 2,
                "name": "Version control your database Part 1: creating migrations and seeding",
                "url": "https://towardsdatascience.com/version-control-your-database-part-1-creating-migrations-and-seeding-992d86c90170",
                "publication_date": "2021-09-01"
            }, {
                "id": 3,
                "name": "Turn Your Code into a Real Program: Packaging, Running and Distributing Scripts using Docker",
                "url": "https://towardsdatascience.com/turn-your-code-into-a-real-program-packaging-running-and-distributing-scripts-using-docker-9ccf444e423f",
                "publication_date": "2021-09-11"
            }, {
                "id": 4,
                "name": "Create a fast auto-documented, maintainable and easy-to-use Python API in 5 lines of code with FastAPI",
                "url": "https://towardsdatascience.com/create-a-fast-auto-documented-maintainable-and-easy-to-use-python-api-in-5-lines-of-code-with-4e574c00f70e",
                "publication_date": "2021-09-21"
            }
        ]

    def get_all_articles(self):
        return self.articles

    def get_one_article(self, articleId: int):
        found_articles = [art for art in self.articles if art['id'] == articleId]
        if (len(found_articles) > 0):
            return found_articles[0]

    def delete_one_article(self, articleId: int):
        self.articles = [art for art in self.articles if art['id'] != articleId]
        return 'ok'

    def post_article(self, articleJson: dict):
        # Get new id
        new_id = max([art['id'] for art in self.articles]) + 1

        # Put new Id in the articleJson
        articleJson['id'] = new_id

        # Insert the article
        self.articles.append(articleJson)

        return "ok"

    def update_article(self, articleId, articleJson):
        articleJson['id'] = articleId
        self.articles = [articleJson for art in self.articles if art['id'] == articleId]
        return "ok"