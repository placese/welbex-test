from enum import Enum
from database_module import schemas
from loguru import logger

class FieldSortParams(Enum):
    quantity: str = 'quantity'
    distance: str = 'distance'
    title: str = 'title'


class FieldFilterParams(Enum):
    date: str = 'date'
    quantity: str = 'quantity'
    distance: str = 'distance'
    title: str = 'title'


def is_float(verifiable_number):
    """Returns True if string is float"""
    try:
        float(verifiable_number)
        return True
    except ValueError:
        return False


def filter_entities(entities: list[schemas.Entity],
                    filter_field: str | None = None,
                    filter_type: str | None = None,
                    filter_value: str | None = None):
    """Returns filtered entities"""

    if filter_field and filter_type and filter_value:
        
        # filter_field is data
        if filter_field == FieldFilterParams.date.value:
            if filter_type == "equals":
                return list(filter(lambda entity: filter_value == entity[filter_field], entities))
            elif filter_type == "contains":
                return list(filter(lambda entity: filter_value in str(entity[filter_field]), entities))
            elif filter_type == "above":
                return list(filter(lambda entity: entity[filter_field] > filter_value, entities))
            elif filter_type == "under":
                return list(filter(lambda entity: entity[filter_field] < filter_value, entities))
        
        # filter_field is is title
        elif filter_field == FieldFilterParams.title.value:
            if filter_type == "equals":
                return list(filter(lambda entity: filter_value == entity[filter_field], entities))
            elif filter_type == "contains":
                return list(filter(lambda entity: filter_value in entity[filter_field], entities))
        
        # filter_field is quantity
        elif filter_field == FieldFilterParams.quantity.value:
            if filter_type == "equals":
                return list(filter(lambda entity: str(filter_value) == str(entity[filter_field]), entities))
            elif filter_type == "above" and filter_value.isnumeric():
                return list(filter(lambda entity: entity[filter_field] > int(filter_value), entities))
            elif filter_type == "under" and filter_value.isnumeric():
                return list(filter(lambda entity: entity[filter_field] < int(filter_value), entities))
        
        # filter_field is distance
        elif filter_field == FieldFilterParams.distance.value:
            if filter_type == "equals" and is_float(filter_value):
                return list(filter(lambda entity: float(filter_value) == entity[filter_field], entities))
            elif filter_type == "above" and is_float(filter_value):
                return list(filter(lambda entity: entity[filter_field] > float(filter_value), entities))
            elif filter_type == "under" and is_float(filter_value):
                return list(filter(lambda entity: entity[filter_field] < float(filter_value), entities))

    return entities
