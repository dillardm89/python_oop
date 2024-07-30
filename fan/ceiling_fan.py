from user.user_new_fan_input import (change_num_blades, change_num_bulbs)
from fan.fan_print_status import get_fan_status_statement


class CeilingFan:
    """ A class to represent a Ceiling Fan

        ...
        Methods
        ----------
            get_fan_details():
                Get all fan attributes
            set_blades():
                Sets value for number of fan blades (3-6)
            set_bulbs():
                Sets value for number of light bulbs (1-5)
            change_fan_status(fan_status):
                Updates fan status (on/off)
            change_light_status(light_status):
                Updates light status (on/off)
            change_speed(speed):
                Updates fan speed setting (1-3)
            change_light_setting(light_setting):
                Updates light level setting (1-5)
            change_direction(direction):
                Updates fan spin direction setting
                (clockwise or counter-clockwise)
    """

    def __init__(self, name, id=None, fan_status="off",
                 light_status="off", blades=None, bulbs=None,
                 speed=0, light_setting=0, direction="counter-clockwise"):
        """ Constructs all the attributes of the object

            Parameters
            ----------
                name : str
                    User defined name of the fan
                id : int
                    Id of the fan
                fan_status : str
                    Status of the fan on or off (default is 'off')
                light_status : str
                    Status of the light on or off (default is 'off')
                blades : int
                    The number of fan blades (default is None)
                bulbs : int
                    The number of light bulbs (default is None)
                speed : int
                    The fan speed setting between 1-3 (default is 0)
                light_setting : int
                    The light level setting between 1-5 (default is 0)
                direction : str
                    The fan rotation direction (default is counter-clockwise)
        """

        self.name = name
        self.id = id
        self.fan_status = fan_status.lower()
        self.light_status = light_status.lower()
        self.blades = blades
        self.bulbs = bulbs
        self.speed = speed
        self.light_setting = light_setting
        self.direction = direction.lower()
        self.set_blades()
        self.set_bulbs()

    def __str__(self):
        """ Prints fan details when print(object) called """
        statement = get_fan_status_statement(self)
        print(statement)
        return ""

    def get_fan_details(self):
        """ Get all fan attributes

            Returns:
                tuple : details
        """
        details = (self.fan_status, self.light_status, self.speed,
                   self.light_setting, self.direction, self.name)
        return details

    def set_blades(self):
        """ Sets value for number of fan blades """
        if self.blades is None:
            self.blades = change_num_blades()
        else:
            return

    def set_bulbs(self):
        """ Sets value for number of light bulbs """
        if self.bulbs is None:
            self.bulbs = change_num_bulbs()
        else:
            return

    def change_fan_status(self, fan_status):
        """ Updates fan status (on / off) """
        self.fan_status = fan_status

    def change_light_status(self, light_status):
        """ Updates light status (on / off) """
        self.light_status = light_status

    def change_speed(self, speed):
        """ Updates fan speed setting (1-3) """
        self.speed = speed

    def change_light_setting(self, light_setting):
        """ Updates light level setting (1-5) """
        self.light_setting = light_setting

    def change_direction(self, direction):
        """ Updates fan spin direction setting
            (clockwise or counter-clockwise)
        """
        self.direction = direction
