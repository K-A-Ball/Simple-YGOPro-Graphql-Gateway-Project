from httpx import AsyncClient

async def get_all_cards_info():
    async with AsyncClient() as client:
        example_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
        response = await client.get(example_url)
        return response.json()["data"]