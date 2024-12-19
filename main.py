from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def init_db():
    with sqlite3.connect("cartoons.db") as conn:
        conn.execute("")
        init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        genre = request.form.get("genre")
        
        with sqlite3.connect("cartoons.db") as conn:
            conn.execute("(name, genre)", (name, genre))
        return redirect(url_for("index"))
    
    
    with sqlite3.connect("cartoons.db") as conn:
        cartoons = conn.execute("").fetchall()
    return render_template("index.html", cartoons=cartoons)


if __name__ == "__main__":
    app.run(debug=True)
