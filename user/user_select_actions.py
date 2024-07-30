from user.validation import validate_type_is_int
from user.user_option_input import (change_setting_options,
                                    new_light_setting_options,
                                    new_speed_setting_options,
                                    new_direction_setting_options)
from user.user_status_input import (change_fan_status_input,
                                    change_status_input,
                                    change_light_status_input)
from user.user_message import return_success_msg


def select_fan_by_id(action_type, fans_len):
    """ Collect user input to select specific fan from list

        Parameters
        ----------
            action_type : str
                Action to perform on selected fan (view, modify, delete)
            fans_len : int
                Number fans in MY_FANS list

        Returns
        ----------
            fan_id : int
                ID of selected fan
    """
    fan_id = -1
    valid_input_type = False
    while not valid_input_type or int(fan_id) < 1 or int(fan_id) > fans_len:
        fan_id = input(f"Enter fan ID to {action_type}: ")
        valid_input_type = validate_type_is_int(fan_id)

    return int(fan_id)


def select_new_fan_status(current_fan_status, current_speed, fan_name):
    """ Collect user input to select new fan status (on / off)

        Parameters
        ----------
            current_fan_status : str
                Current status of fan (on / off)
            current_speed : int
                Current fan speed (0-3)
            fan_name : str
                Name of fan

        Returns
        ----------
            new_fan_status : str
                Updated status of fan (on / off)
            proposed_speed : int
                Updated speed of fan (speed updated to 1 if fan turned
                on or updated to 0 if fan turned off)
    """
    print(f"The fan is currently turned {current_fan_status}.")

    if current_fan_status == "off":
        proposed_fan_status = "on"
        proposed_speed = 1
    else:
        proposed_fan_status = "off"
        proposed_speed = 0

    status_type = "fan"
    status_choice = change_status_input(status_type, proposed_fan_status)

    if status_choice == "Y":
        new_fan_status = proposed_fan_status
        mode = "Fan"
        action_type = f"turned {proposed_fan_status}"
        return_success_msg(mode, fan_name, action_type)
        return new_fan_status, proposed_speed
    else:
        new_fan_status = current_fan_status
        proposed_speed = current_speed
        print(f"Fan named {fan_name} remains turned {current_fan_status}.")
        return new_fan_status, proposed_speed


def select_new_light_status(current_light_status,
                            current_light_setting, fan_name):
    """ Collect user input to select new light status (on / off)

        Parameters
        ----------
            current_light_status : str
                Current status of light (on / off)
            current_light_setting : int
                Current light level setting (0-5)
            fan_name : str
                Name of fan

        Returns
        ----------
            new_light_status : str
                Updated status of light (on / off)
            proposed_light_setting : int
                Updated light level (level updated to 1 if light turned
                on or updated to 0 if light turned off)
    """
    print(f"The light is currently turned {current_light_status}.")

    if current_light_status == "off":
        proposed_light_status = "on"
        proposed_light_setting = 1
    else:
        proposed_light_status = "off"
        proposed_light_setting = 0

    status_type = "light"
    status_choice = change_status_input(status_type, proposed_light_status)

    if status_choice == "Y":
        new_light_status = proposed_light_status
        mode = "Light for fan"
        action_type = f"turned {proposed_light_status}"
        return_success_msg(mode, fan_name, action_type)
        return new_light_status, proposed_light_setting
    else:
        print(f"Light for fan named {fan_name} remains " +
              f"turned {current_light_status}.")
        new_light_status = current_light_status
        proposed_light_setting = current_light_setting
        return new_light_status, proposed_light_setting


def select_new_light_setting(current_light_status,
                             current_light_setting, fan_name):
    """ Collect user input to select new light level setting (1-5)

        Parameters
        ----------
            current_light_status : str
                Current status of light (on / off)
            current_light_setting : int
                Current light level setting (0-5)
            fan_name : str
                Name of fan

        Returns
        ----------
            light_status : str
                Updated status of light (on / off)
            light_setting : int
                Updated light level setting (1-5)
    """
    # User select light status (must be on to change level)
    details = change_light_status_input(current_light_status,
                                        current_light_setting, fan_name)
    light_status = details[0]
    light_setting = details[1]

    if light_status == "off":
        light_status = current_light_status
        light_setting = current_light_setting
        return light_status, light_setting

    # User select whether to change light level setting
    print(f"The light is currently at setting level {light_setting}.")
    setting_type = "light"
    setting_choice = change_setting_options(setting_type)

    if setting_choice == "N":
        print(f"The light for fan named {fan_name} remains " +
              f"at setting level {light_setting}.")
        return light_status, light_setting

    # User select new light level setting
    light_setting_choice = new_light_setting_options()
    if light_setting == light_setting_choice:
        print(f"The light is already set to level {light_setting}.")
        return light_status, light_setting
    else:
        light_setting = light_setting_choice
        mode = "Light for fan"
        action_type = f"changed to speed level {light_setting}"
        return_success_msg(mode, fan_name, action_type)
        return light_status, light_setting


def select_new_speed(current_fan_status, current_speed, fan_name):
    """ Collect user input to select new fan speed setting (1-3)

        Parameters
        ----------
            current_fan_status : str
                Current status of fan (on / off)
            current_speed : int
                Current fan speed setting (0-3)
            fan_name : str
                Name of fan

        Returns
        ----------
            fan_status : str
                Updated status of fan (on / off)
            speed : int
                Updated fan speed setting (1-3)
    """
    # User select fan status (must be on to change speed)
    change_type = "speed"
    details = change_fan_status_input(current_fan_status,
                                      current_speed, fan_name,
                                      change_type)
    fan_status = details[0]
    speed = details[1]

    if fan_status == "off":
        return current_fan_status, current_speed

    # User select whether to change fan speed setting
    print(f"The fan is currently at speed level {speed}.")
    setting_type = "speed"
    speed_choice = change_setting_options(setting_type)

    if speed_choice == "N":
        print(f"The fan named {fan_name} remains " +
              f"at speed level {speed}.")
        return fan_status, speed

    # User select new fan speed setting
    new_speed_choice = new_speed_setting_options()
    if speed == int(new_speed_choice):
        print(f"The fan is already set to speed level {speed}.")
        return fan_status, speed
    else:
        speed = int(new_speed_choice)
        mode = "Fan"
        action_type = f"changed to speed level {speed}"
        return_success_msg(mode, fan_name, action_type)
        return fan_status, speed


def select_new_direction(current_fan_status, current_speed, current_direction,
                         fan_name):
    """ Collect user input to select new fan direction
        (clockwise or counter-clockwise)

        Parameters
        ----------
            current_fan_status : str
                Current status of fan (on / off)
            current_speed : int
                Current fan speed setting (0-3)
            current_direction : str
                Current fan direction setting
                (clockwise or counter-clockwise)
            fan_name : str
                Name of fan

        Returns
        ----------
            fan_status : str
                Updated status of fan (on / off)
            new_direction : str
                Updated fan direction setting
                (clockwise or counter-clockwise)
            speed : int
                Updated fan speed setting (0-3)
    """
    # User select fan status (must be on to change direction)
    change_type = "direction"
    details = change_fan_status_input(current_fan_status,
                                      current_speed, fan_name,
                                      change_type)
    fan_status = details[0]
    speed = details[1]

    if fan_status == "off":
        return current_fan_status, current_direction, current_speed

    # User select where to change fan direction setting
    print(f"The fan is currently set to {current_direction} direction.")
    if (current_direction == "clockwise"):
        print("This is the ideal winter direction setting.")
    else:
        print("This is the ideal summer direction setting.")

    setting_type = "direction"
    direction_choice = change_setting_options(setting_type)

    if direction_choice == "N":
        print(f"The fan named {fan_name} remains at direction " +
              f"setting: {current_direction}.")
        new_direction = current_direction
        return fan_status, new_direction, speed

    # User select new fan direction setting
    new_direction_choice = new_direction_setting_options()
    if current_direction == new_direction_choice:
        print(f"The fan is already set to {current_direction} direction.")
        new_direction = current_direction
        return fan_status, new_direction, speed
    else:
        new_direction = new_direction_choice
        mode = "Fan"
        action_type = f"changed to direction setting: {new_direction}"
        return_success_msg(mode, fan_name, action_type)
        return fan_status, new_direction, speed
