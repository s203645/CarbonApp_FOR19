from flask import render_template, Blueprint
cv=Blueprint('cv',__name__)

@cv.route("/cv")
def cv_home():
    return render_template("cv.html", title="CV")