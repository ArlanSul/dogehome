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
    contact = db.Column(db.String(300), nullable=False)
    Inn = db.Column(db.String(300), nullable=False)
    information = db.Column(db.Text(), nullable=False)

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


@app.route("/shelters/<int:id>")
def shelters_num(id):
    num_shelters = Home.query.get(id)
    return render_template("shelters_num.html", num_shelters=num_shelters)


@app.route('/base', methods=["POST", "GET"])
def base():
    if request.method == "POST":
        title = request.form["title"]
        intro = request.form["intro"]
        contact = request.form["contact"]
        Inn = request.form["Inn"]
        information = request.form["information"]

        article = Home(title=title, intro=intro, contact=contact, Inn=Inn, information=information)
        db.session.add(article)
        db.session.commit()
        return redirect("/shelters")

    else:
        return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
