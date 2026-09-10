from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email:EmailStr
    linkdn_url: AnyUrl
    age: int
    weight: float
    married: bool=False
    #allergies: [List[str]]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['hdfc.com', 'icici.com']
        #abc#gamil.com
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError("Age SHould be between 0 to 100")



patient_info = {
    'name': 'Golu',
    'linkdn_url':'https://github.com/NitinPatil-SDET',
    'age': '27',
    'email':'golu@hdfc.com',
    'weight':55.5,
    #'married':True,
    #'allergies':["Peanuts", "Dust", "Pollen"],
    'contact_details':{'email':'abc@hdfc.com','phone':'9879879876'}

}

patient1 = Patient(**patient_info)

def insert_patient_data(patient1):
    print(patient1.name)
    print(patient1.email)
    print(patient1.linkdn_url)
    print(patient1.age)
    print(patient1.weight)
    print(patient1.married)
    #print(patient1.allergies)
    print(patient1.contact_details)
    print('Inserted into Database')

insert_patient_data(patient1)
