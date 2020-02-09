from flask import request, jsonify, render_template
from content_checker.models import User, ContentIntegratedLab
from content_checker import app
import pdb


@app.route("/content/check/<user>", methods=["POST"])
def function(user):
    if request.method == "POST":
        schema_file = "smaple"  # request.form.get('schema_file')
        expected = "/path/to/schema_file"
        return jsonify(
            {
                "user_answer": schema_file,
                "expected": expected,
                "result": is_equal(schema_file, expected),
            }
        )
    return jsonify({"test": "get"})


@app.route("/content/check/1", methods=["POST"])
def item_1():
    if request.method == "POST":
        schema_file = request.form.get("schema_file")
        expected = "/path/to/schema_file"
        return jsonify(
            {
                "user_answer": schema_file,
                "expected": expected,
                "result": is_equal(schema_file, expected),
            }
        )
    return jsonify({"test": "get"})


@app.route("/content/create_fdb", methods=["POST"])
def create_fdb():
    if request.method == "POST":

        return jsonify({"user_answer": "", "expected": "", "result": True})
    return jsonify({"user_answer": "", "expected": "", "result": True})


def is_equal(arg1, arg2):
    try:
        assert arg1 == arg2
        return True
    except AssertionError:
        return False
