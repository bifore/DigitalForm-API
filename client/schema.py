from ninja import Schema # schema library for data validation
from datetime import date # datetime library for parsing and validating date and timestam

# pydantic schema

class Message(Schema):
    message: str

class DigitalFormIn(Schema):
    client_name: str 
    website_link: str 
    address: str 
    no_of_employees: int 
    no_of_students: int 
    admin_email: str 
    admin_role: str 
    admin_sign: str 
    date_of_sign: date

class DigitalFormOut(Schema):
    client_name: str 
    website_link: str
    message: str = 'success'