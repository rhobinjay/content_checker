from flask import render_template, Blueprint
from content_checker.models import User, ContentIntegratedLab

main = Blueprint("main", __name__)


@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/")
@main.route("/content", methods=["GET", "POST"])
def content():
    users = User.query.all()
    return render_template("content.html", users=users)


@main.route("/content/<string:username>", methods=["GET", "POST"])
def content_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    integratedlabs = ContentIntegratedLab.query.filter_by(user=user).all()
    return render_template(
        "content_user.html", user=user, integratedlabs=integratedlabs
    )
