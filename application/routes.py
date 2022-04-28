from flask import render_template, request
from application import app, db
from application.forms import QueryForm
from application.forms import Calculator
from application.models import Customer, Order


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', title='Gallery')


@app.route('/prints')
def prints():
    return render_template('prints.html', title='Prints')


@app.route('/portraits')
def portraits():
    return render_template('portraits.html', title='Portraits')


@app.route('/weddings')
def weddings():
    return render_template('weddings.html', title='Weddings')

@app.route('/packages', methods=['GET', 'POST'])
def packages():
    form = Calculator()
    error = ""
    if request.method == 'POST':
        distance = form.distance.data
        duration = form.duration.data
        no_people = form.no_people.data
        result = (distance * 2) + (duration * 150) + (no_people * 30)
        final_result = '£' + str(result)
        # return 'result: %s' % result
        return render_template('packages.html', title='Calculator', result=final_result, form=form, message=error)

    return render_template('packages.html', title='Calculator', form=form, message=error)
    # return render_template('packages.html', title='Packages')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    error = ""
    form = QueryForm()
    if request.method == 'POST':
        email = form.email.data
        fullname = form.fullname.data
        telephone = form.telephone.data
        project_date = form.project_date.data
        location = form.location.data
        budget = form.budget.data
        detail = form.detail.data
        services = form.services.data
        recommend = form.recommend.data
        if len(email) == 0 or len(fullname) == 0:
            error = "Please supply both email and fullname"
        else:
            customer = Customer(email=email, fullname=fullname, telephone=telephone)
            order = Order(project_date=project_date, customer_id=1, location=location, budget=budget, detail=detail,
                           services=services, recommend=recommend)
            db.session.add(customer)
            db.session.add(order)
            db.session.commit()
            return 'Thank you!'
    return render_template('contact.html', title='Get In Touch', form=form, message=error)


# @app.route('/calculator', methods=['GET', 'POST'])
# def calculator():
#     form = Calculator()
#     error = ""
#     if request.method == 'POST':
#         distance = form.distance.data
#         duration = form.duration.data
#         no_people = form.no_people.data
#         result = (distance * 2) + (duration * 150) + (no_people * 30)
#         return 'result: %s' % result
#
#     return render_template('calculator.html', title='Calculator', form=form, message=error)


@app.route('/pricing')
def pricing():
    return render_template('pricing.html', title='Pricing')


@app.route('/header1')
def header1():
    return render_template('header.html', title='Header')


@app.route('/header2')
def header2():
    return render_template('header2.html', title='Header2')


@app.route('/navbar')
def navbar():
    return render_template('navbar.html', title='Navbar')

@app.route('/customer/<int:customer_id>', methods=['GET'])
def show_customer(customer_id):
    error = ""
    # use filter_by for any column
    # person = Person.query.filter_by(id=person_id).first()
    #  use get for the PK
    customer = Customer.query.get(customer_id)
    return render_template('customer.html', customer=customer, message=error, title="Customer")

@app.route('/people', methods=['GET'])
def show_people():
    error = ""
    people = Customer.query.all()
    if len(people) == 0:
        error = "There are no people to display"
        print(people)
    return render_template('people.html', people=people, message=error)

# @app.route('/customerorder/<id>', methods=['GET'])
# def customer_and_order(id):
#     error = ""
#     customer = Customer.query.get(id)
#     order = Order.query.get(id)
#     # cars= person.cars
#     if not customer:
#         error = "There is no person with ID: " + str(id)
#         print(customer)
#         print(order)
#     return render_template('customer_order.html', customer=customer, order=order, message=error, title="Customer and Order Info")



# @app.route('/customerorder/<int:customer_id>', methods=['GET'])
# def customer_and_order(customer_id):
#     error = ""
#     customer = Customer.query.get(customer_id)
#     order = Order.query.get(customer_id)
#     # cars= person.cars
#     if not customer:
#         error = "There is no person with ID: " + str(customer_id)
#         print(customer)
#         print()
#     return render_template('customer_order.html', customer=customer, order=order, message=error, title="Customer and Order Info")


@app.route('/customerorder/<int:customer_id>', methods=['GET'])
def customer_order(customer_id):
    error = ""
    customer = Order.query.get(customer_id)
    # order = customer.orders
    if not customer:
        error = "There is no person with ID: " + str(customer_id)
        print(customer)
        # print(order)
        # print(person_and_carinfo)
    return render_template('customer_order.html', customer=customer, message=error, title="Customer Order Info")


@app.route('/order', methods=['GET'])
def show_order():

    order = Order.query.all()

    return render_template('orders.html', order=order)


