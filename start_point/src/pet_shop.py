def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] += amount

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, num_sold):
    pet_shop['admin']['pets_sold'] += num_sold

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop, breed):
    breed_list = []
    for pet in pet_shop['pets']:
        if pet['breed'] == breed:
            breed_list.append(pet)
    return breed_list

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    index = 0
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            pet_shop['pets'].pop(index)
        else:
            index += 1

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)

# test doesn't specify name, seems pointless
def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer, amount):
    customer['cash'] -= amount

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    return new_pet['price'] <= customer['cash']

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet == None:
        return None
    if customer_can_afford_pet(customer, pet):
        sale_amount = pet['price']
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(pet_shop, pet)
        remove_customer_cash(customer, sale_amount)
        increase_pets_sold(pet_shop, 1)
        add_or_remove_cash(pet_shop, sale_amount)