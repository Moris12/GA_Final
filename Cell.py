

class Cell:
    """
    This represent the photovoltaic cell attributes and behaviour
    """
    def __init__(self, length, width, angle, distance_next, id, aoi):
        """
        Initializing a cell for the sequencing
        :param length: cell thickness
        :param width: cell width
        :param angle: cell position angle
        :param distance_next: cable distance to next cell
        :param id: cell id
        :param aoi: irradiation angle of incidence with the cell
        """
        self.length = length
        self.width = width
        self.angle = angle
        self.distance_to_next = distance_next
        self.distance_to_prev = 0
        self.id = id
        self.shade = 0
        self.aoi = aoi




