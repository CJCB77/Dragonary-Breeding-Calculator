breeding_costs = {
    'common':[5,10,20,30,40,50],
    'uncommon':[50,70,90,110,130,150],
}

class Dragon():
    def __init__(self,strength,cunning,resistance,eggs):
        self.strength = strength
        self.cunning = cunning
        self.resistance = resistance
        self.eggs = eggs
        self.rarity = self.get_rarity()
        self.cyt = 0

    def get_total_stats(self):
        stat_total = self.strength + self.cunning + self.resistance
        return stat_total
    
    def get_rarity(self):
        stats = self.get_total_stats()
        if stats < 50:
            rarity = 'common'
        elif stats >= 50  and stats < 90:
            rarity = 'uncommon'
        else:
            rarity = 'rare'
        
        return rarity

    def __str__(self):
        return self.rarity


def calculate_breeding_cost(parent1,parent2,breed):
    fee = 0
    if (parent1.rarity == 'uncommon' and parent2.rarity == 'uncommon') or  (parent2.rarity == 'uncommon' and parent1.rarity == 'uncommon'):
        if parent1.eggs > parent2.eggs:
            if parent1.eggs < 5:
                fee = breeding_costs['uncommon'][parent1.eggs]
            else:
                fee = breeding_costs['uncommon'][5]
        else:
            if parent1.eggs < 5:
                fee = breeding_costs['uncommon'][parent2.eggs]
            else:
                fee = breeding_costs['uncommon'][5]
        
    else:
        
        if parent1.eggs > parent2.eggs:
            if parent1.eggs < 5:
                fee = breeding_costs[parent1.rarity][parent1.eggs]
            else:
                fee = breeding_costs[parent1.rarity][5]
        else:
            if parent1.eggs < 5:
                fee = breeding_costs[parent1.rarity][parent2.eggs]
            else:
                fee = breeding_costs[parent1.rarity][5]
        
    if breed.rarity != parent1.rarity:
        if breed.rarity == 'uncommon':
            fee *= 1.5
        else:
            fee *= 2

    if breed.rarity == 'uncommon':
        fee += 5
    elif breed.rarity == 'rare':
        fee += 75
        
    return fee

def breed(dragon1,dragon2):
    strength = round(((dragon1.strength + dragon2.strength) * 1.2) / 2)
    cunning = round(((dragon1.cunning + dragon2.cunning) * 1.2) / 2)
    resistance = round(((dragon1.resistance + dragon2.resistance) * 1.2) / 2)
    dragon = Dragon(strength,cunning,resistance,0)

    fee = calculate_breeding_cost(dragon1,dragon2,dragon)
    dragon.cost = fee
    dragon1.eggs += 1
    dragon2.eggs += 1

    return dragon

def calculate_breeds(dragon1,dragon2):
    cyt_total = 0
    parents = [dragon1,dragon2]
    dragons = []
    generation_counter = 0

    while True:

        dragon = breed(parents[0],parents[1])
        dragons.append(dragon)
        if dragon.get_total_stats() > 89:
            break
        parents.append(dragon)
        generation_counter += 1
        if generation_counter == 2:
            generation_counter = 0
            del parents[0]
            del parents[0]
    
    for dragon in dragons:
        cyt_total += dragon.cost
    
    values = {'dragon_list':dragons, 'cyt':cyt_total}

    return values

    # for generation,dragon in enumerate(dragons):
    #     print(f"{generation+1} breed stats:")
    #     print(f"{dragon.strength} {dragon.cunning} {dragon.resistance}")
    #     print(f"Stat total: {dragon.get_total_stats()}")