def get_fan_status_statement(fan):
    """ Generate print statement for fan details

        Parameters
        ----------
            fan : object
                Fan object (called from ceiling_fan.py)

        Returns
        ----------
            statement : str
                Fan details
    """
    statement = f"{fan.id}: Fan named '{fan.name}' is turned " +\
        f"{fan.fan_status}. The light is turned {fan.light_status}"

    if fan.fan_status == "off" and fan.light_status == "off":
        statement = statement + ". It is equipped with " +\
            f" {fan.blades} blades and {fan.bulbs} light bulbs."
    elif fan.fan_status == "off" and fan.light_status == "on":
        statement = statement + f" and set to level {fan.light_setting}. " +\
            f"It is equipped with {fan.blades} blades and " +\
            f"{fan.bulbs} light bulbs."
    elif fan.fan_status == "on" and fan.light_status == "off":
        statement = statement + ". It is equipped with " +\
            f"{fan.blades} blades and {fan.bulbs} light bulbs. " +\
            f"It is moving in {fan.direction} direction at " +\
            f"speed level {fan.speed}."
    else:
        statement = statement + f" and set to level {fan.light_setting}. " +\
            f"It is equipped with {fan.blades} blades and " +\
            f"{fan.bulbs} light bulbs. It is moving in {fan.direction} " +\
            f"direction at speed level {fan.speed}."

    return statement
