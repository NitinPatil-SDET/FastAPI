from pydantic import BaseModel
from typing import List

class Patient(BaseModel):
    name: str
    age: int
    weight: float

patient_info = {
    'name': 'Nitin',
    'age': '27',
    'weight':45.5,
    married:bool,
    allergies:List[str],
    
}

patient1 = Patient(**patient_info)

def insert_patient_data(patient1):
    print(patient1.name)
    print(patient1.age)
    print(patient1.weight)
    print('Inserted into Database')

insert_patient_data(patient1)