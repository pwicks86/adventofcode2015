from copy import deepcopy

f = open("input.txt")
#f = open("input2.txt")
d = f.readlines()
boss_dict = {}
for l in d:
    s = l.split(":")
    if ("Hit" in s[0]):
        boss_dict["hp"] = int(s[1])
    else:
        boss_dict[s[0]] = int(s[1])

def drain(me, boss):
    me["hp"] += 2
    boss["hp"] -= 2

def magic_missile(me,boss):
    boss["hp"] -= 4

def shield_on_cast(me,boss):
    me["armor"] += 7

def shield_on_decast(me,boss):
    me["armor"] -= 7

def poison_turn_cast(me, boss):
    boss["hp"] -= 3

def recharge_turn_cast(me,boss):
    me["mana"] += 101

spells = [
    dict(name = "Magic Missile", cost = 53, duration = 0, on_cast = magic_missile),
    dict(name = "Drain", cost = 73, duration = 0, on_cast = drain),
    dict(name = "Shield", cost = 113, duration = 6, on_cast = shield_on_cast,  on_decast=shield_on_decast),
    dict(name = "Poison", cost = 173, duration = 6, turn_cast = poison_turn_cast),
    dict(name = "Recharge", cost = 229, duration = 5, turn_cast = recharge_turn_cast)
]

me = { "hp":50, "mana":500, "armor": 0}
#me = { "hp":10, "mana":250, "armor": 0}

battleState = dict(active_spells = [], me = dict(me), boss = dict(boss_dict), spent_mana = 0)

def do_round(state, sp):
    new_state = deepcopy(state)
    # first check if we have enough mana
    if state["me"]["mana"] < sp["cost"]:
        # then this is a loss
        return None
    # then check if this spell is already active
    for a_spell in new_state["active_spells"]:
        if a_spell["name"] == sp["name"] and a_spell["duration"] > 1:
            return None
    new_state["me"]["hp"] -= 1
    if (new_state["me"]["hp"] <= 0):
        return None
    # make a copy of the spell and perform any oncasts
    new_spell = deepcopy(sp)
    try:
        new_spell["on_cast"](new_state["me"], new_state["boss"])
    except:
        pass

    new_state["spent_mana"] += new_spell["cost"]
    new_state["me"]["mana"] -= new_spell["cost"]
    # Now do the player turn
    for a_spell in new_state["active_spells"]:
        a_spell["duration"] -= 1
        if (a_spell["duration"] <= 0):
            try:
                a_spell["on_decast"](new_state["me"], new_state["boss"])
                continue
            except:
                pass
        try:
            a_spell["turn_cast"](new_state["me"], new_state["boss"])
        except:
            pass

    # Don't add instants to the active list
    if (new_spell["duration"] > 0):
        new_state["active_spells"].append(new_spell)

    # get rid of dead spells
    new_state["active_spells"] = [s for s in new_state["active_spells"] if s["duration"] > 0]

    # and the bosses turn
    for a_spell in new_state["active_spells"]:
        a_spell["duration"] -= 1
        if (a_spell["duration"] <= 0):
            try:
                a_spell["on_decast"](new_state["me"], new_state["boss"])
                continue
            except:
                pass
        try:
            a_spell["turn_cast"](new_state["me"], new_state["boss"])
        except:
            pass

    # get rid of dead spells
    new_state["active_spells"] = [s for s in new_state["active_spells"] if s["duration"] > 0]
    # check if we won
    if new_state["boss"]["hp"] <= 0:
        return new_state

   # do boss damage
    new_state["me"]["hp"] -= max(1,new_state["boss"]["Damage"] - new_state["me"]["armor"])
    if new_state["me"]["hp"] <= 0:
        return None

    return new_state


state_queue = []
state_queue.append(battleState)
while True:
    try:
        next_state = state_queue.pop(0)
    except:
        break
    quit = False
    for spell in spells:
        successor_state = do_round(next_state, spell)
        if successor_state is None:
            continue
        if successor_state["boss"]["hp"] <= 0:
            print(successor_state["spent_mana"])
            quit = True
            break
        else:
            state_queue.append(successor_state)
    if quit:
        break



