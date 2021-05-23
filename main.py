from service import get_all_cards_info
import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from graphql.execution.executors.asyncio import AsyncioExecutor as executor


class CardImage(graphene.ObjectType):
    id = graphene.Int()
    image_url = graphene.String()
    image_url_small = graphene.String()


class CardSet(graphene.ObjectType):
    set_name = graphene.String()
    set_code = graphene.String()
    set_rarity = graphene.String()
    set_rarity_code = graphene.String()
    set_price = graphene.String()


class CardPriceData(graphene.ObjectType):
    cardmarket_price = graphene.String()
    tcgplayer_price = graphene.String()
    ebay_price = graphene.String()
    amazon_price = graphene.String()
    coolstuffinc_price = graphene.String()


class YGOCard(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    type = graphene.String()
    desc = graphene.String()
    atk = graphene.Int()
    race = graphene.String()
    attribute = graphene.String()
    archetype = graphene.String()
    linkval = graphene.Int()
    linkmarkers = graphene.List(graphene.String)
    card_sets = graphene.List(CardSet)
    card_images = graphene.List(CardImage)
    card_prices = graphene.List(CardPriceData)


class Query(graphene.ObjectType):
    allCardsInfo = graphene.List(YGOCard, names=graphene.List(graphene.String))

    @staticmethod
    async def resolve_allCardsInfo(self, info, names):
        
        response = await get_all_cards_info()
        filtered_by_names_provided = [card for card in response if card["name"] in names]
        return filtered_by_names_provided


app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query),
    executor_class=executor))