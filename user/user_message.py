def return_success_msg(mode, user_fan_name, action_type):
    """ Print statement for selected action status

        Parameters
        ----------
            mode : str
                Item selected ('Fan' or 'Light for fan')
            user_fan_name : str
                Name of selected fan
            action_type : str
                Action for selected mode (create, delete, modify, etc.)
    """
    print(f"{mode} named {user_fan_name} has been successfully {action_type}.")
