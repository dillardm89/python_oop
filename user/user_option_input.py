from user.validation import (validate_type_is_int, validate_type_is_str)


def view_details_options():
    """ Collect user input for view fans option

        Returns
        ----------
            choice : str
                User response (Y or N)
    """
    choice = ""
    valid_input_type = False
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input("Would you like to view details for a " +
                       "specific fan? (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    return choice.upper()


def change_setting_options(setting_type):
    """ Collect user input for change speed option

        Returns
        ----------
            choice : str
                User response (Y or N)
    """
    valid_input_type = False
    choice = ""
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input(f"Do you wish to change the {setting_type} " +
                       "setting? (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    return choice.upper()


def modify_fan_options():
    """ Collect user input for modify fan option

        Returns
        ----------
            choice : str
                User response (Y or N)
    """
    choice = ""
    valid_input_type = False
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input("Would you like to modify this fan? (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    if choice.upper() == "N":
        selection = -1
        return selection
    else:
        selection = 1
        return selection


def new_light_setting_options():
    """ Collect user input for new light setting option

        Returns
        ----------
            new_setting_choice : int
                User response (1-5)
    """
    new_setting_choice = -1
    setting_input_type = False
    while (setting_input_type is not True or
            int(new_setting_choice) < 1 or int(new_setting_choice) > 5):
        new_setting_choice = input("Enter the new light setting: (1-5) ")
        setting_input_type = validate_type_is_int(new_setting_choice)

    return int(new_setting_choice)


def new_speed_setting_options():
    """ Collect user input for new fan speed setting option

        Returns
        ----------
            new_setting_choice : int
                User response (1-3)
    """
    new_speed_choice = -1
    speed_input_type = False
    while (speed_input_type is not True or
            int(new_speed_choice) < 1 or int(new_speed_choice) > 3):
        new_speed_choice = input("Enter the new speed setting: (1-3) ")
        speed_input_type = validate_type_is_int(new_speed_choice)

    return int(new_speed_choice)


def new_direction_setting_options():
    """ Collect user input for new fan direction setting option

        Returns
        ----------
            new_setting_choice : int
                User response (clockwise or counter-clockwise)
    """
    new_direction_choice = ""
    direction_input_type = False
    while (not direction_input_type or
           new_direction_choice.lower() not in ("clockwise",
                                                "counter-clockwise")):
        new_direction_choice = input("Enter the new direction setting: " +
                                     "(clockwise or counter-clockwise) ")
        direction_input_type = validate_type_is_str(new_direction_choice)

    return new_direction_choice.lower()
