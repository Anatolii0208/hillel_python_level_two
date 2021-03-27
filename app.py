
from flask import *
from flask_sqlalchemy import *
#creating bd
app = Flask(__name__)

#Is admin
isadmin = False
password = "abcd1234"
login = "User"

#cart - list
list_cart = []

#Work with bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Creating table in bd
class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    foto = db.Column(db.String(1000), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    caption = db.Column(db.String(1000))
    isActive = db.Column(db.Boolean, default = True)

    def __repr__(self):
        return self.title

#Main page processing
@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html',data=items)

#Page about processing
@app.route('/about')
def about():
    return render_template('about.html')

#Page createnew post processing
@app.route('/create',methods=['POST','GET'])
def create():
    global isadmin
    if isadmin == True:
        if request.method == "POST":
            foto = request.form['foto']
            title = request.form['title']
            price = request.form['price']
            caption = request.form['caption']
            item = Item(foto=foto, title=title, price=price, caption=caption)
            try:
                db.session.add(item)
                db.session.commit()
                return redirect('/')
            except:
                return "Mistake"
        else:
            return render_template('create.html')
    else:
        return render_template("not_admin.html")

#Admin page processing
@app.route('/admin',methods=['POST','GET'])
def admin():
    global login,password,isadmin
    if request.method == 'POST':
        if request.form['login'] == login and request.form['password'] == password:
            isadmin = True
            return render_template('becomeadmin.html')
        else:
            return render_template('incorect.html')
    else:
        return render_template('admin.html')

#Bottom buy processing
@app.route('/buy/<int:id>')
def item_buy(id):
    list_cart.append(Item.query.get(id).id)
    str1 = ''
    '''for el in list_cart:
        str1 += str(el['foto'])
        str1 += "\n"
        str1 += str(el['price'])
        str1 += "\n"
        str1 += str(el['caption'])
        str1 += "\n"
    return str1'''
    return redirect('/cart')

#Bottom delete processing
@app.route('/del/<int:id>')
def item_del(id):
    if len(list_cart) != 0 and Item.query.get(id).id in list_cart:
        list_cart.remove(Item.query.get(id).id)

    '''str2 = ''
    for el in list_cart:
        str2 += str(el['foto'])
        str2 += "\n"
        str2 += str(el['price'])
        str2 += "\n"
        str2 += str(el['caption'])
        str2 += "\n"
    return str2'''

    return redirect('/cart')

#Cart processing
@app.route('/cart')
def cart():
    items = []
    for el in list_cart:
        items.append(Item.query.get(el))
        #items = Item.query.order_by(Item.price).all()
    return render_template('cart.html', data=items)

#newgame 
@app.route('/game')
def game():
    return render_template("flappy_bird.html")

if __name__ == '__main__':
    app.run(debug=True)
