from application import db
from application.models import Customer, Order


db.drop_all()
db.create_all()

testPerson1 = Customer(email='julie_d@gmail.com', fullname='Julie Dooley', telephone='0795463999')
testPerson2 = Customer(email='sally_reed@yahoo.com', fullname='Sally Reed', telephone='0748992111')

order1 = Order(project_date=20220609, customer_id=1, location='Camden', budget=800,
                      detail='Professional', services='Other', recommend='Google')

order2 = Order(project_date=20220923, customer_id=2, location='Richmond', budget=85,
                      detail='One Professional Photo', services='Portrait Photoshoot', recommend='Social Media')

# quote = Calculator(distance=10, duration=2, no_people=5)

orders = [order1, order2]

db.session.add(testPerson1)
db.session.add(testPerson2)


db.session.add_all(orders)
# db.session.add(quote)

db.session.commit()
