import json
from typing import List

from apistar import App, Route, types, validators
from apistar.http import JSONResponse

# helpers

def _load_cars_data():
    with open('cars.json') as f:
        cars = json.loads(f.read())
        return {car["id"]: car for car in cars}

cars = _load_cars_data()
VALID_MANUFACTURERS = set([car["manufacturer"]
                          for car in cars.values()])
                          
CAR_NOT_FOUND = 'Car not found'

breakpoint()
# load in data

# definition

class Car(types.Type):
    pass

# API methods

def list_cars() -> List[Car]:
    pass

def create_car(car: Car) -> JSONResponse:
    pass

def get_car(car_id: int) -> JSONResponse:
    pass

