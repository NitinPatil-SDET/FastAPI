#03_ModelValidator.py

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email:EmailStr
    linkdn_url: AnyUrl
    age: int
    weight: float
    height: float
    married: bool=False
    #allergies: [List[str]]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/((self.height/100)**2),2)
        return bmi

patient_info = {
    'name': 'Golu',
    'linkdn_url':'https://github.com/NitinPatil-SDET',
    'age': '65',
    'email':'golu@hdfc.com',
    'weight':55.5,
    'height':165,
    #'married':True,
    #'allergies':["Peanuts", "Dust", "Pollen"],
    'contact_details':{'email':'abc@hdfc.com','phone':'9879879876', 'emergency':'1231231231'}

}

patient1 = Patient(**patient_info)

def insert_patient_data(patient1):
    print(patient1.name)
    print(patient1.email)
    print(patient1.linkdn_url)
    print(patient1.age)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.bmi)
    #print(patient1.allergies)
    print(patient1.contact_details)
    print('Inserted into Database')

insert_patient_data(patient1)
