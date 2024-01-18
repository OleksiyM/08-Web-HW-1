from pymongo.mongo_client import MongoClient
import os

from dotenv import load_dotenv

from app import search_by_name, search_by_tag

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')


URI = f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/?retryWrites=true&w=majority'

# uri = "mongodb+srv://<username>:<password>@cluster0.vhirvg8.mongodb.net/?retryWrites=true&w=majority"


if __name__ == '__main__':
    client = MongoClient(URI)

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    print(search_by_name('asd'))
    print()
    print(search_by_name('Albert Einstein'))
    print()
    print(search_by_tag('live'))
    print()
    print(search_by_tag('life'))
    print(search_by_tag('life123'))
    print()
    print('Done!')
    input('Press Enter to exit...')
    exit(0)
