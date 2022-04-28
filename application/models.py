from application import db
# import the sqlalchemy object (db) created for our app


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(15), nullable=False)
    Custom_Order = db.relationship('Order', backref='customer')


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(20), nullable=False)
    budget = db.Column(db.Float(20), nullable=False)
    detail = db.Column(db.Text, nullable=False)
    services = db.Column(db.String(20), nullable=False)
    recommend = db.Column(db.String(20), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

# class Calculator(db.Model):
#     quote_id = db.Column(db.Integer, primary_key=True)
#     distance = db.Column(db.Integer, nullable=False)
#     duration = db.Column(db.Integer, nullable=False)
#     no_people = db.Column(db.Integer, nullable=False)




