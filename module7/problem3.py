# Write a function called type_advantage(attacker, defender) that takes two Pokémon types as strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on simple type effectiveness rules.
def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    else:
        return "Neutral"
