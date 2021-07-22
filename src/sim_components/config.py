import collections

#Position = collections.namedtuple('Position', ['x', 'y'])

seed = 420 # dank

field_size = 100

actorPlottingConfig = {
    'color' : '#3BEBA8',
    'marker' : 'o',
    'label' : 'actors'
}

foodPlottingConfig = {
    'color' : 'red',
    'marker' : 'x',
    'label' : 'food'
}

food_values = {
    'default_nutritive_value' : 1
}



if __name__ == "__main__":
    print(Position(1, 2))
