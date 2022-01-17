import GAutils
import numpy
import Cell

CONST_ANGLE_PENALTY = 0.25
CONST_DISTANCE_PENALTY = 0.6
CONST_SHADE_PENALTY = 0.15
CONST_POSITION_PENALTY = 0.0


class Genome:
    """
    A class that describes the solution
    """
    angle_hour = 170

    def __init__(self, zenith_angle=0, azimuth_angle=0, best_angle=0, length=0, width=0, Seq=0):
        """
        solution initialization
        :type seq: Cell[]
        :param seq: the sequence that is already built
        :param zenith_angle: zenith angle from our latitude, needed to calc aoi
        :param azimuth_angle: azimuth angle to the sun, needed to calc aoi
        :param best_angle: best angle for the cell angle to be
        :param length: cell length
        :param width: cell width
        """
        # numpy.random.permutation(GAutils.CONST_SEQUENCE_LENGTH)
        if zenith_angle != 0:
            self.zenith_angle = zenith_angle
        if azimuth_angle != 0:
            self.azimuth = azimuth_angle
        if best_angle != 0:
            self.best_angle = best_angle
        if Seq == 0:
            temp = []
            for i in range(GAutils.CONST_CELLS_IN_SEQUENCE):
                distance = numpy.round(numpy.random.uniform(GAutils.CONST_MIN_DISTANCE, GAutils.CONST_MAX_DISTANCE), 2)
                angle = numpy.round(numpy.random.uniform(GAutils.CONST_MIN_CELL_ANGLE, GAutils.CONST_MAX_CELL_ANGLE), 2)
                aoi = numpy.round(self.calculate_aoi(angle), 2)
                a = Cell.Cell(length, width, angle, distance, i, aoi)
                temp.append(a)
            self.sequence = temp
        else:
            self.sequence = Seq
        self.fitness = 0
        self.range = [0, 0]
        self.penalty = 0

    def getIndexSequence(self, i):
        return self.sequence[i]

    def getSequence(self):
        """
        This method extract the sequence of a slution
        :return: The solutions' sequence
        """
        return self.sequence

    def setRange(self, minRange, maxRange):
        """
        This method build the range of the pie slice for the roulette selection based on the solutions' fitness
        :param minRange: the minimum range [0,<1]
        :param maxRange: the maximum range [0,1]
        :return: True for success, False otherwise
        """
        if minRange < maxRange:
            self.range = [minRange, maxRange]
            return True
        else:
            return False

    def getRange(self):
        """
        This method extract the solution range
        :return: the solution range
        """
        return self.range

    def getFit(self):
        """
        This method extract the solution fitness
        :return: the solution fitness
        """
        return self.fitness

    def evaluate(self):
        """
        This method evaluate the whole sequence fitness based on each cell attributes
        :return: NONE
        """
        angle_penalty = 0
        dist_penalty = 0
        shade_penalty = 0
        self.calculate_shade_in_solution(self.azimuth)
        for i in range(GAutils.CONST_SEQUENCE_LENGTH):
            temp_angle = numpy.fabs(self.sequence[i].angle - self.best_angle)
            temp_angle_penalty = temp_angle / GAutils.CONST_ANGLE_DIF
            angle_penalty += temp_angle_penalty
            temp_shade = self.sequence[i].shade
            shade_penalty += temp_shade
        for i in range(GAutils.CONST_SEQUENCE_LENGTH - 1):
            temp_dist = self.sequence[i].distance_to_next / GAutils.CONST_DISTANCE_DIF
            dist_penalty += temp_dist
        total_dist_penalty = (dist_penalty / (GAutils.CONST_SEQUENCE_LENGTH - 1)) * CONST_DISTANCE_PENALTY
        total_angle_penalty = (angle_penalty / GAutils.CONST_SEQUENCE_LENGTH) * CONST_ANGLE_PENALTY
        total_shade_penalty = (shade_penalty / GAutils.CONST_SEQUENCE_LENGTH) * CONST_SHADE_PENALTY
        self.fitness = 1 - (total_angle_penalty + total_dist_penalty + total_shade_penalty)
        self.penalty = total_dist_penalty + total_shade_penalty + total_angle_penalty

    def get_penalty(self):
        """
        This method extract the penalty of a sequence
        :return: the penalty
        """
        return self.penalty

    def calculate_shade_in_solution(self, azimuth):
        """
        This method calc's the shade on each cell according to azimuth to sun
        :param azimuth: azimuth to sun, needed to calc shade direction
        :return: NONE
        """
        seq = self.getSequence()
        if azimuth <= GAutils.CONST_AZIMUTH_MAX_1 or azimuth > GAutils.CONST_AZIMUTH_MIN_1:
            for i in range(GAutils.CONST_SEQUENCE_LENGTH):
                cell = seq[i]
                if (i % 3) == 0:
                    shade = self.calculate_shade(cell, seq[i + 2].distance_to_next)
                    if shade > 0 and (i + 5) < GAutils.CONST_SEQUENCE_LENGTH:
                        self.sequence[i + 5].shade += shade / cell.length
                if (i % 3) == 1:
                    shade = self.calculate_shade(cell, seq[i + 1].distance_to_next)
                    if shade > 0 and (i + 3) < GAutils.CONST_SEQUENCE_LENGTH:
                        self.sequence[i + 3].shade += shade / cell.length
                if (i % 3) == 2:
                    shade = self.calculate_shade(cell, cell.distance_to_next)
                    if shade > 0 and (i + 1) < GAutils.CONST_SEQUENCE_LENGTH:
                        self.sequence[i + 1].shade += shade / cell.length

        elif (azimuth <= GAutils.CONST_AZIMUTH_MAX_2) and (azimuth > GAutils.CONST_AZIMUTH_MIN_2):
            for i in range(GAutils.CONST_SEQUENCE_LENGTH):
                cell = seq[i]
                if i == 3:
                    shade = self.calculate_shade(cell, cell.distance_to_next)
                    if shade > 0:
                        self.sequence[i + 1].shade += shade / cell.length
                    shade = self.calculate_shade(cell, seq[i + 2].distance_to_next)
                    if shade > 0:
                        self.sequence[i + 5].shade += shade / cell.length
                        self.sequence[i + 4].shade += shade / (3 * cell.length)
                if (i % 3) == 1:
                    if i == 1:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (2 * cell.length)
                        shade = self.calculate_shade(cell, seq[i + 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i + 3].shade += shade / cell.length
                            self.sequence[i + 4].shade += shade / (3 * cell.length)
                    if i == 4:
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / (2 * cell.length)
                        shade = self.calculate_shade(cell, seq[i + 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i + 3].shade += shade / cell.length
                            self.sequence[i + 2].shade += shade / (3 * cell.length)
                if (i % 3) == 2:
                    if i == 2:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (2 * cell.length)
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                            self.sequence[i + 2].shade += shade / (3 * cell.length)
                    if i == 5:
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                    if i == 8:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (2 * cell.length)

        elif (azimuth <= GAutils.CONST_AZIMUTH_MAX_3) and (azimuth > GAutils.CONST_AZIMUTH_MIN_3):
            for i in range(GAutils.CONST_SEQUENCE_LENGTH):
                cell = seq[i]
                if (i % 3) == 0:
                    if i == 3:
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                if (i % 3) == 1:
                    if i == 1 or i == 7:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length
                    else:
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                if (i % 3) == 2:
                    if i == 2 or i == 8:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length

        elif (azimuth <= GAutils.CONST_AZIMUTH_MAX_4) and (azimuth > GAutils.CONST_AZIMUTH_MIN_4):
            for i in range(GAutils.CONST_SEQUENCE_LENGTH):
                cell = seq[i]
                if (i % 3) == 0:
                    if i == 3:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length
                            self.sequence[i - 2].shade += shade / (2 * cell.length)
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / (3 * cell.length)
                    if i == 6:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (2 * cell.length)
                if (i % 3) == 1:
                    if i == 1:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (3 * cell.length)
                    elif i == 4:
                        shade = self.calculate_shade(cell, seq[i - 2].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 3].shade += shade / cell.length
                            self.sequence[i - 4].shade += shade / (2 * cell.length)
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / (3 * cell.length)
                    elif i == 7:
                        shade = self.calculate_shade(cell, seq[i - 2].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 3].shade += shade / cell.length
                            self.sequence[i - 2].shade += shade / (2 * cell.length)
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (3 * cell.length)

                if (i % 3) == 2:
                    if i == 2:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (3 * cell.length)
                    elif i == 5:
                        shade = self.calculate_shade(cell, seq[i - 3].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 5].shade += shade / (2 * cell.length)
                    elif i == 8:
                        shade = self.calculate_shade(cell, seq[i - 3].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 5].shade += shade / cell.length
                            self.sequence[i - 4].shade += shade / (3 * cell.length)
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (2 * cell.length)

        elif (azimuth <= GAutils.CONST_AZIMUTH_MAX_5) and (azimuth > GAutils.CONST_AZIMUTH_MIN_5):
            for i in range(GAutils.CONST_SEQUENCE_LENGTH):
                cell = seq[i]
                if (i % 3) == 0:
                    if i != 0:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length
                if (i % 3) == 1:
                    if i != 1:
                        shade = self.calculate_shade(cell, seq[i - 2].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 3].shade += shade / cell.length
                if (i % 3) == 2:
                    if i != 2:
                        shade = self.calculate_shade(cell, seq[i - 3].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 5].shade += shade / cell.length

        elif (azimuth <= GAutils.CONST_AZIMUTH_MAX_6) and (azimuth > GAutils.CONST_AZIMUTH_MIN_6):
            for i in range(GAutils.CONST_SEQUENCE_LENGTH):
                cell = seq[i]
                if (i % 3) == 0:
                    if i == 3:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (2 * cell.length)
                    if i == 6:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / (3 * cell.length)
                            self.sequence[i - 2].shade += shade / (2 * cell.length)
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                if (i % 3) == 1:
                    if i == 4:
                        shade = self.calculate_shade(cell, seq[i - 2].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 2].shade += shade / (2 * cell.length)
                            self.sequence[i - 3].shade += shade / (3 * cell.length)
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length
                    if i == 7:
                        shade = self.calculate_shade(cell, seq[i - 2].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 3].shade += shade / (3 * cell.length)
                            self.sequence[i - 4].shade += shade / (2 * cell.length)
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                if (i % 3) == 2:
                    if i == 5:
                        shade = self.calculate_shade(cell, seq[i - 3].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 4].shade += shade / (3 * cell.length)
                            self.sequence[i - 5].shade += shade / (2 * cell.length)
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length
                    if i == 8:
                        shade = self.calculate_shade(cell, seq[i - 3].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 5].shade += shade / (3 * cell.length)

        elif (azimuth <= GAutils.CONST_AZIMUTH_MAX_7) and (azimuth > GAutils.CONST_AZIMUTH_MIN_7):
            for i in range(GAutils.CONST_SEQUENCE_LENGTH):
                cell = seq[i]
                if (i % 3) == 0:
                    if i != 3:
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                if (i % 3) == 1:
                    if i == 1 or i == 7:
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                    else:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length
                if (i % 3) == 2:
                    if i == 5:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length

        elif (azimuth <= GAutils.CONST_AZIMUTH_MAX_8) and (azimuth > GAutils.CONST_AZIMUTH_MIN_8):
            for i in range(GAutils.CONST_SEQUENCE_LENGTH):
                cell = seq[i]
                if (i % 3) == 0:
                    if i == 0:
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                        shade = self.calculate_shade(cell, seq[i + 2].distance_to_next)
                        if shade > 0:
                            self.sequence[i + 5].shade += shade / (2 * cell.length)
                            self.sequence[i + 4].shade += shade / (3 * cell.length)
                    if i == 3:
                        shade = self.calculate_shade(cell, seq[i + 2].distance_to_next)
                        if shade > 0:
                            self.sequence[i + 5].shade += shade / (2 * cell.length)
                if (i % 3) == 1:
                    if i == 1:
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / cell.length
                        shade = self.calculate_shade(cell, seq[i + 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i + 2].shade += shade / (3 * cell.length)
                            self.sequence[i + 3].shade += shade / (2 * cell.length)
                    if i == 4:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length
                        shade = self.calculate_shade(cell, seq[i + 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i + 3].shade += shade / (2 * cell.length)
                            self.sequence[i + 4].shade += shade / (3 * cell.length)
                if (i % 3) == 2:
                    if i == 5:
                        shade = self.calculate_shade(cell, seq[i - 1].distance_to_next)
                        if shade > 0:
                            self.sequence[i - 1].shade += shade / cell.length
                        shade = self.calculate_shade(cell, cell.distance_to_next)
                        if shade > 0:
                            self.sequence[i + 1].shade += shade / (2 * cell.length)
                            self.sequence[i + 2].shade += shade / (3 * cell.length)

    def calculate_aoi(self, angle):
        """
        This method is used to calc every cell aoi
        :param angle: needed to calc sun irradiation angle of incidence(aoi) on cell
        :return: NONE
        """
        cos_aoi = numpy.cos(numpy.deg2rad(self.zenith_angle)) * numpy.cos(numpy.deg2rad(angle)) + numpy.sin(numpy.deg2rad(self.zenith_angle)) * numpy.sin(numpy.deg2rad(angle)) * numpy.cos(numpy.deg2rad(self.azimuth - self.angle_hour))
        aoi = numpy.arccos(cos_aoi)
        aoi = numpy.rad2deg(aoi)
        return aoi

    def calculate_shade(self, cell, cell_distance):
        """
        This method calc's the shade of a given cell
        :param cell: the cell we check the shade he make
        :param cell_distance: distance to next cell
        :return: shade in decimal point refers to the % of shade from cell
        """
        shade = numpy.cos(numpy.deg2rad(cell.angle)) * (numpy.sin(numpy.deg2rad(cell.angle)) * cell.length * numpy.tan(numpy.deg2rad(90 - cell.aoi)) - cell_distance - (cell.length - cell.length * numpy.cos(numpy.deg2rad(cell.angle))))
        return shade


