from flask import Flask, render_template
from App.youtube import youtube_bp


def create_App():

    App = Flask(__name__)

    App.register_blueprint(
        youtube_bp,
        url_prefix="/youtube"
    )

    @App.route("/")
    def home():
        return render_template("index.html")

    @App.route("/html")
    def html():
        return render_template("index.html")

    return App

