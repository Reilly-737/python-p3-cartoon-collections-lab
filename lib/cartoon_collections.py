def roll_call_dwarves(dwarves):
    for i, name in enumerate(dwarves, start=1):
        print(f"{i}. {name}")
    

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]
    

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)
    

def find_the_cheese(snacks):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheese_types:
            return snack
    return None
    
