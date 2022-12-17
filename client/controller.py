import orjson # fast, accurate JSON library for Python
from ninja import NinjaAPI # import ninja-api library
from ninja.parser import Parser
from ninja.renderers import BaseRenderer
from .api import router as main_router # import router instance from api

# parser configuration for orjson
class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)

# render configuration for orjson
class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)  
        
# ninja instance
api = NinjaAPI(parser=ORJSONParser(), renderer=ORJSONRenderer())

# add router
api.add_router("/", main_router)
