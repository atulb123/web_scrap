from flask import Flask, render_template, request, redirect
from flask_cors import cross_origin
import requests
import urllib3
import testing
app = Flask(__name__)
http = urllib3.PoolManager()


@app.route("/")
@cross_origin()
def home_page():
    return render_template("homepage.html")


@app.route("/search", methods=["GET", "POST"])
@cross_origin()
def search():
    if request.method == "POST":
        search_results = testing.get_all_reviews(request.form["search_name"])
        return render_template("searchpage.html", search_results=search_results)
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run()
