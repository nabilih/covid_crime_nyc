from .app import db


class crime(db.Model):
    __tablename__ = 'crime'

    index = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date)
    ComplaintType = db.Column(db.String(1000))
    Descriptor = db.Column(db.String(1000))
    locationType = db.Column(db.String(1000))
    incidentAddress = db.Column(db.String(1000))
    City = db.Column(db.String(1000))
    Borough = db.Column(db.String(1000))
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)

  
    def __repr__(self):
        return '<crime %r>' % (self.name)

class covid(db.Model):
    __tablename__ = 'covid'

    index = db.Column(db.Integer, primary_key=True)
    Borough = db.Column(db.String(1000))
    Date = db.Column(db.Date)
    TotalCrimes = db.Column(db.Integer)
    Cases = db.Column(db.Integer)
    Hospitalizations = db.Column(db.Integer)
    Deaths = db.Column(db.Integer)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
  
    def __repr__(self):
        return '<covid %r>' % (self.name)

class summary(db.Model):
    __tablename__ = 'summary'

    index = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date)
    TotalCases = db.Column(db.Integer)
    TotalHospitalizations = db.Column(db.Integer)
    TotalDeaths = db.Column(db.Integer)
    ComplaintType = db.Column(db.Integer)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
  
    def __repr__(self):
        return '<summary %r>' % (self.name)
