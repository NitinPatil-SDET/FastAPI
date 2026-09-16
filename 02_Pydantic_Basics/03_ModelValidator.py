#03_ModelValidator.py

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
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

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and "emergency" not in self.contact_details:
            raise ValueError(
                "Patient older than 60 must have an emergency contact"
            )
        return self


    



patient_info = {
    'name': 'Golu',
    'linkdn_url':'https://github.com/NitinPatil-SDET',
    'age': '65',
    'email':'golu@hdfc.com',
    'weight':55.5,
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
    #print(patient1.allergies)
    print(patient1.contact_details)
    print('Inserted into Database')

insert_patient_data(patient1)
