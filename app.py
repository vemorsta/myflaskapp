from flask import Flask, flash ,render_template, redirect , request, url_for
from flask_login import login_user
from form import LoginForm, SignupForm
from models import user, session
from models import Card , session
from flask import session as s

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_random_secret_key'

# s["Username"]=user.username
# if s.get("username") : s.pop()

@app.route('/main')
@app.route('/')
def Main():
    return render_template('main.html')

@app.route('/add-card', methods=['GET','POST'])
def add_card():
    if request.method == 'POST':
        name = request.form['name']
        

        new_card = Card(name=name )
        session.add(new_card)
        session.commit()
        flash ("product added successfully in your bag.thanks for shopping <3", 'success')
        return redirect(url_for('add_card'))
    return render_template('add-card.html')


@app.route('/index')
def index():
    cards = session.query(Card).all()
    return render_template('index.html', cards=cards)

@app.route('/details/<int:id>')
def details(id):
    c = session.query(Card).get(id)
    return render_template('details.html', c=c)

@app.route('/delete/<int:id>')
def delete(id):
    c= session.query(Card).get(id)
    session.delete(c)
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if not (username and password):
            return render_template("signup.html", message="All fields are required.")
        flash('Account created successfully!', 'success')
        
        my_user = user(username=username , password=password)
        session.add(my_user)
        session.commit()
        
        return redirect(url_for('login'))
   
    return render_template('signup.html', form=form)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if s.get("username") :
        return redirect(url_for('Main')) 
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        s["username"]=username
        flash('Login successful!', 'success')
        return redirect(url_for('Main'))
   
    flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/Gaurav_Gupta')
def Gaurav_Gupta():
    return render_template('Gaurav_Gupta.html')

@app.route('/Dolce&Gabbana')
def Dolce_Gabbana():
    return render_template('Dolce&Gabbana.html')

@app.route('/Iris_van_Herpen')
def Iris_van_Herpen():
    return render_template('Iris_van_Herpen.html')


if __name__ == "__main__":
    app.run(debug=True)