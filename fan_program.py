import sys
import time
from fan.fan_functions import (create_fan, delete_fan, update_fan_id,
                               view_fan_details, create_fan_list,
                               modify_fan, MY_FANS)
from user.user_message import return_success_msg
from user.user_new_fan_input import user_name_fan
from user.user_menu_input import (menu_input, modify_fan_menu)
from user.user_option_input import (view_details_options, modify_fan_options)
from user.user_select_actions import select_fan_by_id

""" This is an object modeling program for a ceiling fan.
    User can interact with terminal to create new fan,
    delete existing fan, view list of all fans, view details
    for a specific existing fan, and modify fan settings
    (fan on/off status, light on/off status, speed, direction).
"""


def main_menu():
    """ Main menu function for user terminal interaction """
    menu_text = "What would you like to do?:\n1: Create new fan\n2: Delete " +\
        "existing fan\n3: View list of fans\n4: View specific fan details\n" +\
        "5: Modify fan settings\n6: Exit program"
    print(menu_text)
    selection = menu_input()

    # Create new fan
    if selection == 1:
        fan_name_create = user_name_fan()
        create_fan(fan_name_create)
        action_type = "created"
        mode = "Fan"
        return_success_msg(mode, fan_name_create, action_type)
        return_to_menu()

    # Delete existing fan
    elif selection == 2:
        num_fans = create_fan_list()
        if num_fans < 1:
            return_to_menu()

        action_type = "delete"
        fan_id = select_fan_by_id(action_type, len(MY_FANS))
        fan_name_delete = delete_fan(fan_id)
        update_fan_id(fan_id)
        mode = "Fan"
        return_success_msg(mode, fan_name_delete, action_type)
        return_to_menu()

    # View list, view details, modify
    elif selection in (3, 4, 5):
        num_fans = create_fan_list()
        if num_fans < 1:
            return_to_menu()

        # start point for option 3 = view list all fans
        if selection == 3:
            view_details_choice = view_details_options()
            if view_details_choice == "N":
                return_to_menu()

        if selection in (3, 4):
            action_type = "view specific details"
        else:
            action_type = "modify"

        fan_id = select_fan_by_id(action_type, len(MY_FANS))

        # start point for option 4 = view details specific fan
        if selection in (3, 4):
            view_fan_details(fan_id)
            modify_fan_decision = modify_fan_options()

            if modify_fan_decision == -1:
                return_to_menu()

        # start point for option 5 = modify fan
        modify_choice = -1
        print(modify_choice, type(modify_choice), "before while")
        while modify_choice < 6:
            modify_choice = modify_fan_menu()
            modify_fan(modify_choice, fan_id)

        return_to_menu()

    # Exit program
    else:
        exit_program()


def return_to_menu():
    """ Return to main menu function """
    input("Press 'Enter' key to return to the main menu.")
    main_menu()


def exit_program():
    """ Exit program function """
    print("Exiting...")
    time.sleep(1)
    sys.exit()


if __name__ == "__main__":
    main_menu()
