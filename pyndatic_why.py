from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email:EmailStr
    linkdn_url: AnyUrl
    age: int
    weight: float
    married: bool=False
    allergies: Optional[List[str]]=None
    contact_details: Dict[str, str]

patient_info = {
    'name': 'Golu',
    'linkdn_url':'https://github.com/NitinPatil-SDET',
    'age': '27',
    'email':'golu@test.com',
    'weight':45.5,
    #'married':True,
    #'allergies':["Peanuts", "Dust", "Pollen"],
    'contact_details':{'email':'abc@test.com','phone':'9879879876'}

}

patient1 = Patient(**patient_info)

def insert_patient_data(patient1):
    print(patient1.name)
    print(patient1.email)
    print(patient1.linkdn_url)
    print(patient1.age)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.allergies)
    print(patient1.contact_details)
    print('Inserted into Database')

insert_patient_data(patient1)
