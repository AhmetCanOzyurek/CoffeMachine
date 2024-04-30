from  Machine_data import MENU,resources, money




def report_rsrcs(user_request):

    for key in resources:
        print(f"{key.capitalize()}: {str(resources[key])}ml")
    print(f"Money: ${money["mon"]}")


def calculate_coins(user_req):
    changes = {"quarters":0.25 ,"dimes": 0.10,"nickles": 0.05,"pennies": 0.01}
    print("Please insert coins.")
    change_sum= 0

    for change in changes:
        amount = int(input(f"how many {change}?: "))
        for i in range (0,amount):
             change_sum += changes[change]

    if change_sum < MENU[user_req]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        money["mon"] += float("{:0.3f}".format(MENU[user_req]["cost"]))
        change_sum -= MENU[user_req]["cost"]
        formatted_change = float("{:0.3f}".format(change_sum))
        print(f"Here is ${formatted_change} in change.")



def make_coffee(user_request):

    resources["water"]  -= MENU[user_request]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_request]["ingredients"]["coffee"]

    if not user_request == "espresso":
       resources["milk"] -= MENU[user_request]["ingredients"]["milk"]
    if user_request not in MENU:
        return "That coffee doesn't even exist."

def check_resources(user_re):
        if resources["water"] < MENU[user_re]["ingredients"]["water"]:
            print(f"Sorry there is not enough water.")
            return  False
        elif resources["milk"] < MENU[user_re]["ingredients"]["milk"]:
            print(f"Sorry there is not enough milk.")
            return False
        elif resources["coffee"] < MENU[user_re]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough coffee.")
            return False

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

