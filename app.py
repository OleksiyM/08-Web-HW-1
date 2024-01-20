from typing import Tuple

from models import Author, Quote

import redis

from redis_lru import RedisLRU

client = redis.Redis(host='localhost', port=6379, password=None, db=0)

cache = RedisLRU(client)


def print_help():
    print('valid commands:')
    print('  name:value       - search by Author name')
    print('  tag:value        - search by tag in the quote')
    print('  tags:value,value - search by tags in the quote')
    print('examples:')
    print('  name: Steve Martin')
    print('  tag: love')
    print('  tags: love,life')
    print('  name:st          - you can use part of the name')
    print('  tag:li           - you can use part of the tag')


def parser(input_command: str) -> tuple[str, str] | tuple[None, None]:
    try:
        search_type, val = input_command.split(':', 1)
    except ValueError:
        return None, None
    if search_type not in ['name', 'tag', 'tags']:
        print('Invalid command')
        print_help()
        return None, None

    return search_type, val


@cache
def search_by_name(author_name: str) -> str:
    print(f'Searching in DB quotes by name: {value}')
    authors = Author.objects(fullname__iregex=author_name)
    quotes = ''
    if authors:
        for author in authors:
            quotes = Quote.objects(author=author)
        if quotes:
            return "\n".join(f"{q.quote}" for q in quotes)
        else:
            return ''
    else:
        return f'Author {author_name} not found'


@cache
def search_by_tag(tag: str) -> str:
    print(f'Searching in DB quotes by tag: {tag}')
    quotes = Quote.objects(tags__iregex=tag)
    if len(quotes) > 0:
        return "\n".join(f"{q.quote}" for q in quotes)
    else:
        return f'Quote not found with tag {tag}'


def select_search_type(search_type, value):
    if search_type == 'name':
        print(search_by_name(value))
    elif search_type == 'tag':
        print(search_by_tag(value))
    elif search_type == 'tags':
        tag_list = value.split(',')
        for t in tag_list:
            print(search_by_tag(t))
    return f'Search done'


if __name__ == "__main__":
    while True:
        print('\nEnter command: value for search in DataBase or enter "help" for list of commands or "exit" to exit')
        user_input = input('>>>')
        if user_input == 'exit':
            break
        elif user_input == 'help':
            print_help()
            continue
        # print(parser(user_input))
        db, value = parser(user_input)
        if db and value:
            print(select_search_type(db.strip(), value.strip()))
        else:
            print('Invalid command')
