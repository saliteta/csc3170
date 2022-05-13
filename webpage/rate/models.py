from rate import db, login_manager
from rate import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#first version, no foreign key right now

class Student(db.Model):
    Student_email = db.Column(db.String(length = 50), primary_key = True)
    Student_name = db.Column(db.String(length = 30), nullable = False, unique = False)
    password_hash = db.Column(db.String(length = 60), nullable = False, unique = False)
    Department_id = db.Column(db.String(length = 3), nullable = False, unique = True)      # this is a foreign key
    Major = db.Column(db.String(length = 5), nullable = True, unique = False)    

class Instructior(db.Model):
    Instructor_email = db.Column(db.String(length = 60), primary_key = True)
    Instructor_name = db.Column(db.String(length = 30), nullable = False, unique = False)
    password_hash = db.Column(db.String(length = 60), nullable = True, unique = False)
    Department_id = db.Column(db.String(length = 3), nullable = False, unique = True)      # this is a foreign key
    Title = db.Column(db.String(20), nullable = False, unique = False)
    Information = db.Column(db.Text())
    #some time we need to add average rate, which is called average quality

class Course(db.Model):
    Course_id = db.Column(db.String(7), primary_key = True)
    Course_name = db.Column(db.String(60), nullable = False, unique = True)
    Information = db.Column(db.Text())
    #add Avg_difficulty

class Session(db.Model):
    Session_id = db.Column(db.Integer(), primary_key = True)
    Session_time = db.Column(db.String(30), nullable = False, unique = False)
    '''there are some attributes I did not add into, since don't kmow other types'''

class Department(db.Model):
    Department_id = db.Column(db.String(length = 3), primary_key = True)
    Department_name = db.Column(db.String(length = 50), nullable = False, unique = True)

class Rate(db.Model):
    Rate_id = db.Column(db.Integer(), primary_key = True)
    Rate_time = db.Column(db.DateTime(), nullable = False, unique = False)
    Quality = db.Column(db.Integer(), nullable = False, unique = False)
    Difficulty = db.Column(db.Integer(), nullable = False, unique = False)
    Session_id = db.Column(db.Integer(), nullable = False, unique = True) # actually is a foreign key
    Student_email = db.Column(db.String(length = 50), primary_key = True, unique = True) # actually is a foreign key


'''here is the practice'''





class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    email_address = db.Column(db.String(60), nullable = False, unique = True)
    password_hashing = db.Column(db.String(60), nullable = False, unique = False)
    budget = db.Column(db.Integer(),nullable = False, unique = False, default = 0) # set the default value is 1000
    items = db.relationship('Item', backref = 'owned_user', lazy = True)# backref is the pointer that point back to the upper relation
    #eg user owns iphone, given iphone, want to know who the owner is? using the backref
    #lazy = True ?????

    #following line use the hashing function to encrypt the password with a decorator
    @property
    def password(self):
        return self.password
    @password.setter
    def password(self, plain_text_password):
        self.password_hashing = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hashing, attempted_password)#since we haved hashing our function, we don't know how to the real data
        #therefore, we need to hash the input password and compare it with the self.password_hashing


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id')) # the owner is the id of the user, which is foreign key

    def __repr__(self) -> str:
        return f"Item {self.name}"
        #at the default stage, you can do the 