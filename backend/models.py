from datetime import datetime
from .app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
class Articles(db.Model):

    id = db.Column(db.Integer, primary_key=True)


    title = db.Column(db.String(length=80))


    body = db.Column(db.String(length=80))
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    
    def __repr__(self):

        # This is only for representation how you want to see user information after query.
        return "<User(id='%s', date='%s', title='%s', body='%s')>" % (
            self.id,
            self.date,
            self.title,
            self.body
        
        )
