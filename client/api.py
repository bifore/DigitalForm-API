from ninja import Router # import router module from ninja
# import asyncpg # asynchronous driver for postgres
# from .query import execute 
from decouple import config # store env variables in .env or ini
from .schema import DigitalFormOut, DigitalFormIn, Message # schema
from .models import ClientInfo as client # data models
from asgiref.sync import sync_to_async # async support for sync function
from django.core.serializers import serialize # serialize queryset to json

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
@router.get("/clientData")
async def get_data(request):
    
    try:
        data = await client.objects.async_all()
        res = serialize('json', data)
        return res
    except Exception as e:
        print(e)


# query api
@router.get("/pg")
async def run(request):

    try:
        conn = await asyncpg.connect(user=config('USER'), password=config('PASSWORD'),
                                     database=config('DATABASE'), host=config('HOST'))
        
        await execute(conn)
        await conn.close()
        print("done")

    except Exception as e:
        print(e)