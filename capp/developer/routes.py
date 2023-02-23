from flask import render_template, Blueprint
developer=Blueprint('developer',__name__)

@developer.route("/developer")
def developer_home():
    return render_template("developer.html", title="Developer")