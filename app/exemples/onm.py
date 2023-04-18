import sqlite3

conm = sqlite3.connect('./chinook.db')
cur = conm.cursor()

sql = '''
SELECT CustomerId, FirstName, LastName FROM customers;
'''

cur.execute(sql)
customers = cur.fetchall()

conm.close()



class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

customer_object = []
for customer in customers:
    customer_obj = Customer(
        customer_id=customer["CustomerId"],
        first_name=customer["FirstName"],
        last_name=customer["LastName"],
    )
    customer_object.append(customer_obj)

for customer in customer_object:
    # print(f'Full Nmae: {customer.first_name} {customer.last_name}')
    print(f'Full Name: {customer.get_full_name()}')


'''
ORM 
0 - object (class Customers)
R - relation (sql table)
M - mapping (join)

Django ORM
SqlAlchemy
'''