from flask import render_template, request
from application import app, db
from application.forms import QueryForm
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

@app.route('/packages')
def packages():
    return render_template('packages.html', title='Packages')

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



