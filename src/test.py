from db import * 

print(len(Household.select()))


for household in Household.select():
    for transaction in household.transactions:
        print(transaction.WEEK_NO, transaction.DAY, transaction.PRODUCT.COMMODITY_DESC)
    print('============================================================')