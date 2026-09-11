#05_nested_model.py

from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict={'city':'mumbai', 'state':'MH', 'pin':'400097'}
address1=Address(**address_dict)

patient_dict={'name':'Zopesh', 'gender':'Male', 'age':22, 'address':address1}
patient1=Patient(**patient_dict)


temp=patient1.model_dump()
temp2=patient1.model_dump_json()
temp3=patient1.model_dump(include=[])
temp4=patient1.model_dump(exclude=[])
temp5=patient1.model_dump(exclude_unset=True)

print(temp2)
print(type(temp2))

