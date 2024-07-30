from user.validation import validate_type_is_str


def change_status_input(status_type, proposed_status):
    """ Collect user input for whether to change status

        Parameters
        ----------
            status_type : str
                Changing status for light or fan
            proposed_status : str
                Proposed new status (on / off)

        Returns
        ----------
            choice : str
                User response (Y or N)
    """
    valid_input_type = False
    choice = ""
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input("Do you wish to turn the " +
                       f"{status_type} {proposed_status} (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    return choice.upper()


def change_fan_status_input(current_fan_status, current_speed,
                            fan_name, change_type):
    """ Collect user input for whether to change fan status
        (if changing fan speed or direction)

        Parameters
        ----------
            current_fan_status : str
                Current status of fan (on / off)
            current_speed : int
                Current fan speed (0-3)
            fan_name : str
                Name of fan
            change_type : str
                Type of change (speed or direction)

        Returns
        ----------
            fan_status : str
                Updated status of fan
            new_speed : int
                Updated speed of fan (changed to 1 if fan turned
                on from off or no change if fan already on)
    """
    if current_fan_status == "on":
        fan_status = current_fan_status
        new_speed = current_speed
        return fan_status, new_speed

    print("The fan is currently turned off. " +
          f"It must be on to change the {change_type}.")

    # User select whether to change fan status
    status_type = "fan"
    proposed_status = "on"
    fan_status_choice = change_status_input(status_type, proposed_status)

    if (fan_status_choice == "Y"):
        fan_status = proposed_status
        new_speed = 1
        print(f"The fan named {fan_name} is now turned on")
        return fan_status, new_speed
    else:
        print(f"The fan named {fan_name} will remain off.")
        fan_status = current_fan_status
        new_speed = current_speed
        return fan_status, new_speed


def change_light_status_input(current_light_status,
                              current_light_setting, fan_name):
    """ Collect user input for whether to change light status
        (if changing light level setting)

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
                Updated status of light
            new_light_setting : int
                Updated light level setting (changed to 1 if light turned
                on from off or no change if light already on)
    """
    if current_light_status == "on":
        light_status = current_light_status
        new_light_setting = current_light_setting
        return light_status, new_light_setting

    print("The light is currently turned off. " +
          "It must be on to change the setting.")

    # User select whether to change fan status
    status_type = "light"
    proposed_status = "on"
    light_status_choice = change_status_input(status_type, proposed_status)

    if (light_status_choice == "Y"):
        light_status = proposed_status
        new_light_setting = 1
        print(f"The light for fan named {fan_name} is now turned on")
        return light_status, new_light_setting
    else:
        print(f"The light for fan named {fan_name} will remain off.")
        light_status = current_light_status
        new_light_setting = current_light_setting
        return light_status, new_light_setting
