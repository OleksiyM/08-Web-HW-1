import json

from mongoengine.errors import NotUniqueError

from models import Author, Quote


def main():
    with open('authors.json', encoding='utf-8', mode='r') as f:
        authors = json.load(f)
        for author in authors:
            try:
                author = Author(fullname=author['fullname'], born_date=author['born_date'],
                                born_location=author['born_location'], description=author['description'])
                author.save()
            except NotUniqueError as e:
                print(f'Author already exists: {author.fullname}, error {e}')

    with open('quotes.json', encoding='utf-8', mode='r') as fq:
        quotes = json.load(fq)
        for quote in quotes:
            try:
                author = Author.objects(fullname=quote['author'])
                quote = Quote(author=author[0], quote=quote['quote'], tags=quote['tags'])
                quote.save()
            except Exception as e:
                print(f'Unable to add: {quote.quote}, error {e}')


if __name__ == "__main__":
    main()
