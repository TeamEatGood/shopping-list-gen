from peewee import *

db = SqliteDatabase('data2.db')

class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    COMMODITY_DESC = CharField()
    SUB_COMMODITY_DESC = CharField()

class Household(BaseModel):
    pass

class Transaction(BaseModel):
    household = ForeignKeyField(Household, related_name='transactions')
    BASKET_ID = IntegerField()
    DAY = IntegerField()
    PRODUCT = ForeignKeyField(Product, related_name='transactions')
    QUANTITY = IntegerField()
    SALES_VALUE = DoubleField()
    TRANS_TIME = IntegerField()
    WEEK_NO = IntegerField()
db.connect()
db.create_tables([Product, Household, Transaction], safe=True)
