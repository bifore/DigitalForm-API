from ninja import Router # import router module from ninja
from .query import execute # execute function to create db structure
from .schema import DigitalFormOut, DigitalFormIn, Message, ClientData # schema
from .models import ClientInfo as client # data models
from asgiref.sync import sync_to_async # async support for sync function

from django.core.serializers import serialize # serialize queryset to json
from django.http import HttpResponse
import orjson


# router instance
router = Router()

# get api
@router.get("/home", response={200: Message, 204: None})
async def home(request):
    try:
        if(True):
            return 200, {'message': 'success'}
        else:
            return 204, None
    except Exception as e:
        print(e)


# post api 
@router.post("/client", response={200: Message, 408: Message})
async def save_data(request, clientData: DigitalFormIn):

    try:
        newClient = await client.objects.async_create(
            client_name = clientData.client_name,
            website_link = clientData.website_link,
            address = clientData.address,
            no_of_employees = clientData.no_of_employees,
            no_of_students = clientData.no_of_students,
            admin_email = clientData.admin_email,
            admin_role = clientData.admin_role,
            admin_sign = clientData.admin_sign,
            date_of_sign = clientData.date_of_sign 
        )
        await sync_to_async(newClient.save)()
        return 200, {'message': 'created'}

    except Exception as e:
        print(e)
        return 408, {'message': 'request failed'}


# get api
@router.get("/clientData", response={404: Message})
async def get_data(request):
    
    try:
        data = await client.objects.async_all()
        res = serialize('json', data)
        obj = orjson.loads(res)
        return HttpResponse(orjson.dumps(obj))
        
    except Exception as e:
        print(e)
        return 404, {'message': 'no client data available'}

# query api
@router.post("/createDB", response={200: Message, 408: Message})
async def run(request, client: ClientData):

    try:
        await execute(client)
        return 200, {'message': 'db structure created for new client'}

    except Exception as e:
        print(e)
        return 408, {'message': 'request failed'}