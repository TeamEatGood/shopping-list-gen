from db import * 
from predict import shopping_list_for_household

print(shopping_list_for_household(2300, 247))

print(len(Household.select()))

'''for household in Household.select():
    print(household.id)
    print('============================================================')'''