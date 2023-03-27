# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    # total_cash = int
    # for total_cash in pet_shop:
    #     if total_cash["admin"]["total_cash"] == 1000:
    #         return total_cash
    #     else:
    #         return "Error"
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
# for problems 3 & 4

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)

    return pets

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            found_pet = pet
            return found_pet
        elif pet["name"] == None:
                return None
            
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            found_pet = pet
    return pet_shop["pets"].remove(found_pet)
            
def add_pet_to_stock(pet_shop, new_pet):
    new_pet = {
            "name": "Bors the Younger",
            "pet_type": "cat",
            "breed": "Cornish Rex",
            "price": 100
        }
    pet_shop["pets"].append(new_pet)
    return len(pet_shop)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, cash):
    customers["cash"] -= cash

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

def customer_can_afford_pet(customers, new_pet):
    for cash in range(customers["cash"]):
        if cash > new_pet["price"]:
            can_buy_pet = True
            return can_buy_pet
        elif customers["cash"] < new_pet["price"]:
            return False
        elif customers["cash"] == new_pet["price"]:
            return True
 
# Extensions

def sell_pet_to_customer(pet_shop, pet, customer):
        # if pet and customer["cash"] >= True:    
        #     customer["pets"].append(pet)
        #     pet_shop["admin"]["total_cash"] += pet["price"]  
        #     customer["cash"] -= pet["price"]
        #     pet_shop["admin"]["pets_sold"] = len(customer["pets"])
        #     pet_shop["pets"].remove(pet)
        # elif pet == False:
        #     return None
        # elif customer["cash"] == False:
        #     return None
        if find_pet_by_name(pet_shop, pet) and get_customer_cash == True:
            get_customer_pet_count(customer, pet).append(pet)
            get_customer_cash(customer).remove(pet["price"])
            get_total_cash(pet_shop).append(pet["price"])
        
    


    




