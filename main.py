import json

import aiohttp
import asyncio

from category import Category

BASE_URL = 'https://www.wildberries.ru/'
CATALOG_URL = 'https://static-basket-01.wbbasket.ru/vol0/data/main-menu-ru-ru-v2.json'

MAX_LEVEL_NESTING = 99


async def parse_category(
        data: dict,
        level: int,
        max_level_nesting: int = MAX_LEVEL_NESTING
) -> Category | None:
    if not data or not data.get('isDenyLink') or level > max_level_nesting:
        return None

    data_childs = data.get('childs')
    print(data_childs)
    if data_childs:
        childs = [c for c in [await parse_category(d, level + 1) for d in data_childs] if c is not None]
        data['childs'] = childs

    try:
        parse_object = Category(**data)
    except Exception as e:
        print(f'Error: {e}')
        return None

    return parse_object


async def parse_goods(data: dict) -> list:
    pass


async def main():
    categories_data = None
    async with aiohttp.ClientSession() as session:

        async with session.get(CATALOG_URL) as response:
            try:
                categories_data = json.loads(await response.text())
            except json.decoder.JSONDecodeError as e:
                print(f'Error: {e}')

    categories = [c for c in [await parse_category(d, 0) for d in categories_data] if c is not None]




if __name__ == '__main__':
    asyncio.run(main())
