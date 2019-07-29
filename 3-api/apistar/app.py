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

# breakpoint()
# load in data

# definition

class Car(types.Type):
    id = validators.Integer(allow_null=True) # assign in POST
    manufacturer = validators.String(enum=list(VALID_MANUFACTURERS))
    model = validators.String(max_length=50)
    year = validators.Integer(minimum=1900, maximum=2050)
    vin = validators.String(max_length=50, default='')

# API methods

def list_cars() -> List[Car]:
    return [Car(car[1]) for car in sorted(cars.items())]
# breakpoint()

def create_car(car: Car) -> JSONResponse:
    car_id = len(cars) + 1
    car.id = car_id
    cars[car_id] = car
    return JSONResponse(Car(car), 201)

def get_car(car_id: int) -> JSONResponse:
    car = cars.get(car_id)
    if not car:
        error = {'error': CAR_NOT_FOUND}
        return JSONResponse(error, 404)

    return JSONResponse(Car(car), 200)

def update_car(car_id: int, car: Car) -> JSONResponse:
    pass

def delete_car(car_id: int) -> JSONResponse:
    pass

routes = [
    Route('/', method='GET', handler=list_cars),
    Route('/', method='POST', handler=create_car),
    Route('/{car_id}/', method='GET', handler=get_car),
    Route('/{car_id}/', method='PUT', handler=update_car),
    Route('/{car_id}/', method='DELETE', handler=delete_car),
]

app = App(routes=routes)

if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)

