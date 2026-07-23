from config import WIDTH
from config import HEIGHT

from map_builder import MapBuilder
from renderer import Renderer
from exporter import Exporter
from validator import Validator
from statistics import Statistics
from sample_maps import SAMPLE_NAME

print()

print(

    "ASCII Map Builder"

)

print(

    SAMPLE_NAME

)

builder = MapBuilder()

grid = builder.create(

    WIDTH,

    HEIGHT

)

Renderer().show(

    grid

)

Exporter().save(

    grid

)

valid = Validator().validate(

    grid

)

print(

    "Valid:",

    valid

)

print()

stats = Statistics().collect(

    grid

)

Statistics().print(

    stats

)
