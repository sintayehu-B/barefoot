from flask import Flask, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)



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
@app.route("/", methods=['GET'])
def get_articles():
    return jsonify({"hello ": "world"})


if __name__ =="__main__":
    app.run(debug=True)
