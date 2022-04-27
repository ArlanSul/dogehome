from flask import Flask, request, url_for, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    Inn = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return "<Home %r>" % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route("/shelters")
def shelters():
    art = Home.query.order_by(Home.id).all()
    return render_template("shelters.html", art=art)


@app.route('/base', methods=["POST", "GET"])
def base():
    if request.method == "POST":
        title = request.form["title"]
        intro = request.form["intro"]
        Inn = request.form["Inn"]

        article = Home(title=title, intro=intro, Inn=Inn)
        db.session.add(article)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
