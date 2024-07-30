from fan.ceiling_fan import CeilingFan
from user.user_select_actions import (select_new_fan_status,
                                      select_new_direction,
                                      select_new_speed,
                                      select_new_light_status,
                                      select_new_light_setting)


# Create list of class objects with example fans
MY_FANS = [
    CeilingFan("example fan 123", 1, "on",
               "off", 4, 3, 2, 0, "clockwise"),
    CeilingFan("my bedroom fan", 2, "off", "on", 5, 4,
               0, 5, "clockwise"),
    CeilingFan("just another fan", 3, "on", "on", 6, 5,
               3, 2, "counter-clockwise"),
    CeilingFan("new off fan", 4, "off", "off", 6, 2,
               0, 0, "clockwise")
]


def create_fan(fan_name_create):
    """ Create new fan instance

        Parameters
        ----------
            fan_name_create : str
                Name of fan to be created
    """
    new_fan = CeilingFan(fan_name_create)

    MY_FANS.append(new_fan)
    new_fan.id = MY_FANS.index(new_fan) + 1


def delete_fan(fan_id):
    """ Delete existing fan

        Parameters
        ----------
            fan_id : int
                ID of fan to be deleted

        Returns
        ----------
            fan_name_delete : str
                Name of fan to be deleted
    """
    fan_name_delete = MY_FANS[fan_id - 1].name
    del MY_FANS[fan_id - 1]

    return fan_name_delete


def create_fan_list():
    """ Generate list of existing fans by ID and name

        Returns
        ----------
            total_fans : int
                Total number of fans in MY_FANS list
    """
    if len(MY_FANS) == 0:
        print("There are no fans to view. Try creating new fans first.")
        total_fans = 0
        return total_fans
    else:
        print("Below is the current fan list.")

        for fan in MY_FANS:
            print(f"{fan.id}: {fan.name}")

        total_fans = len(MY_FANS)
        return total_fans


def update_fan_id(fan_id):
    """ Update fan ID's in list after deleting fan
        (ensures ID's are sequential)

        Parameters
        ----------
            fan_id : int
                ID of deleted fan
    """
    i = fan_id - 1
    while i <= len(MY_FANS) - 1:
        MY_FANS[i].id -= 1
        i += 1


def view_fan_details(fan_id):
    """ View details of specific fan by ID

        Parameters
        ----------
            fan_id : int
                ID of fan to view details

    """
    print(MY_FANS[fan_id - 1])


def modify_fan(selection, fan_id):
    """ Handles user input for fan modification
        to call corresponding function

        Parameters
        ----------
            selection : int
                Menu item selected from main menu
            fan_id : int
                ID of fan to be modiified
    """
    if selection == 1:
        modify_fan_status(fan_id)
    elif selection == 2:
        modify_fan_speed(fan_id)
    elif selection == 3:
        modify_fan_direction(fan_id)
    elif selection == 4:
        modify_light_status(fan_id)
    elif selection == 5:
        modify_light_setting(fan_id)
    else:
        return


def modify_fan_status(fan_id):
    """ Modify fan status (on / off)

        Parameters
        ----------
            fan_id : int
                ID of fan to be modified
    """
    fan_details = MY_FANS[fan_id - 1].get_fan_details()
    current_fan_status = fan_details[0]
    current_speed = fan_details[2]
    fan_name = fan_details[5]

    details = select_new_fan_status(current_fan_status,
                                    current_speed, fan_name)
    fan_status = details[0]
    speed = details[1]
    MY_FANS[fan_id - 1].change_fan_status(fan_status)
    MY_FANS[fan_id - 1].change_speed(speed)


def modify_light_status(fan_id):
    """ Modify light status (on / off)

        Parameters
        ----------
            fan_id : int
                ID of fan to be modified
    """
    fan_details = MY_FANS[fan_id - 1].get_fan_details()
    current_light_status = fan_details[1]
    current_light_setting = fan_details[3]
    fan_name = fan_details[5]

    details = select_new_light_status(current_light_status,
                                      current_light_setting, fan_name)
    light_status = details[0]
    light_setting = details[1]
    MY_FANS[fan_id - 1].change_light_status(light_status)
    MY_FANS[fan_id - 1].change_light_setting(light_setting)


def modify_light_setting(fan_id):
    """ Modify light level setting (1-5)

        Parameters
        ----------
            fan_id : int
                ID of fan to be modified
    """
    fan_details = MY_FANS[fan_id - 1].get_fan_details()
    current_light_status = fan_details[1]
    current_light_setting = fan_details[3]
    fan_name = fan_details[5]

    details = select_new_light_setting(current_light_status,
                                       current_light_setting, fan_name)
    light_status = details[0]
    light_setting = details[1]

    if light_setting == 0:
        return
    else:
        MY_FANS[fan_id - 1].change_light_status(light_status)
        MY_FANS[fan_id - 1].change_light_setting(light_setting)


def modify_fan_speed(fan_id):
    """ Modify fan speed setting (1-3)

        Parameters
        ----------
            fan_id : int
                ID of fan to be modified
    """
    fan_details = MY_FANS[fan_id - 1].get_fan_details()
    current_fan_status = fan_details[0]
    current_speed = fan_details[2]
    fan_name = fan_details[5]

    details = select_new_speed(current_fan_status, current_speed, fan_name)
    fan_status = details[0]
    speed = details[1]

    if speed == 0:
        return
    else:
        MY_FANS[fan_id - 1].change_fan_status(fan_status)
        MY_FANS[fan_id - 1].change_speed(speed)


def modify_fan_direction(fan_id):
    """ Modify fan direction setting (clockwise or
        counter-clockwise)

        Parameters
        ----------
            fan_id : int
                ID of fan to be modified
    """
    fan_details = MY_FANS[fan_id - 1].get_fan_details()
    current_fan_status = fan_details[0]
    current_speed = fan_details[2]
    current_direction = fan_details[4]
    fan_name = fan_details[5]

    details = select_new_direction(current_fan_status, current_speed,
                                   current_direction, fan_name)
    fan_status = details[0]
    direction = details[1]
    speed = details[2]

    if direction is None:
        return
    else:
        MY_FANS[fan_id - 1].change_fan_status(fan_status)
        MY_FANS[fan_id - 1].change_speed(speed)
        MY_FANS[fan_id - 1].change_direction(direction)
