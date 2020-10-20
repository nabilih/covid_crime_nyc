from .app import db


class crime(db.Model):
    __tablename__ = 'crime'

    index = db.Column(db.bigint, primary_key=True)
    Date = db.Column(db.date)
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

    index = db.Column(db.bigint, primary_key=True)
    Borough = db.Column(db.String(1000))
    Date = db.Column(db.date)
    TotalCrimes = db.Column(db.bigint)
    Cases = db.Column(db.bigint)
    Hospitalizations = db.Column(db.bigint)
    Deaths = db.Column(db.bigint)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
  
    def __repr__(self):
        return '<covid %r>' % (self.name)

class summary(db.Model):
    __tablename__ = 'summary'

    index = db.Column(db.bigint, primary_key=True)
    Date = db.Column(db.date)
    TotalCases = db.Column(db.integer)
    TotalHospitalizations = db.Column(db.integer)
    TotalDeaths = db.Column(db.integer)
    ComplaintType = db.Column(db.bigint)


    Hospitalizations = db.Column(db.bigint)
    Deaths = db.Column(db.bigint)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
  
    def __repr__(self):
        return '<summary %r>' % (self.name)
