from db import *
import csv
with open('data/product.csv') as csvfile:
    product_csv = csv.reader(csvfile)
    for i, row in enumerate(product_csv):
        print(i/92355.0)
        if i != 0:
            product = Product(id=row[0], COMMODITY_DESC=row[4], SUB_COMMODITY_DESC=row[5])
            product.save(force_insert=True)
print('done with product table')
users = 0
with open('data/transaction_data.csv') as csvfile:
    transaction_csv = csv.reader(csvfile)
    for i, row in enumerate(transaction_csv):
        if i != 0:
            print(users/2500)

            household, created = Household.get_or_create(id=row[0])
            if created:
                users += 1
            product = Transaction(household=household, 
                                  BASKET_ID=int(row[1]), 
                                  DAY=int(row[2]), 
                                  PRODUCT=int(row[3]), 
                                  QUANTITY=int(row[4]), 
                                  SALES_VALUE=float(row[5]), 
                                  TRANS_TIME=int(row[8]), 
                                  WEEK_NO=int(row[9]))
            product.save()
