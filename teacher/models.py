from teacher import db

class Designation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    designation_name = db.Column(db.String(128))
    help_text = db.Column(db.String(128))
    teacher = db.relationship('Teacher', backref='person', cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, designation_name, help_text):
        self.designation_name = designation_name
        self.help_text = help_text


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)
    address = db.Column(db.Text)
    phone_number = db.Column(db.String(128))
    designation_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, name, age, address, phone_number, designation_id):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.designation_id = designation_id
