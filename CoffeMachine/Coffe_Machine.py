from  Machine_data import MENU,resources, money
from Machine_functionality import (report_rsrcs, check_resources,
                                   calculate_coins, make_coffee)


should_continue = True

while should_continue:
    user_req = input("What would you like? (espresso/latte/cappuccino): ")

    if user_req == "off":
        should_continue = False
    elif user_req == "report":
        report_rsrcs(user_req)
    else:
        if not check_resources(user_req) == False and not calculate_coins(user_req) == False:
            make_coffee(user_req)
            print(f"Here is your {user_req} ☕️. Enjoy!")

