def validate_type_is_int(user_input):
    """ Validate user input type is numeric

        Parameters
        ----------
            user_input : str
                User input for menu selection

        Returns
        ----------
            True / False : bool
                Whether user_input is numeric
    """
    return user_input.isnumeric()


def validate_type_is_str(user_input):
    """ Validate user input type is string (no numbers)

        Parameters
        ----------
            user_input : str
                User input for menu selection

        Returns
        ----------
            True / False : bool
                Whether user_input is string
    """
    return isinstance(user_input, str)
