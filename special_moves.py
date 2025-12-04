# COUNTER-ATTACK
def counter_attack(data):
    # 1.3x damage IF enemy attacks this turn; MISS otherwise.
    
    ptype = data['player_type']
    # move logic
    if data['enemy_move_type'] == "ATTACK":
        damage = ptype['attack_base_hp'] * 1.3
        data['enemy_hp'] -= damage
        return "Successful Counter-Attack!"
    
    return "Counter-Attack MISSED (enemy did not attack)!"
    
# LIFESTEAL
def lifesteal(data):
    # IF enemy has >60% HP AND player has <30% HP, THEN heal HALF base HP.
    ehp = data['enemy_hp']
    etype = data['enemy_type']

    php = data['player_hp']
    ptype = data['player_type']

    if ehp >= etype['base_hp'] * 0.6 and php <= ptype['base_hp'] * 0.3:
        data['player_hp'] += ptype['base_hp'] * 0.5
        return "Successful Lifesteal!"
    
    return "Lifesteal missed!"
    
    
# Dictionary of special move handlers
SPECIAL_FUNCTIONS = {
    "Counter-Attack": counter_attack,
    "Lifesteal": lifesteal,
}