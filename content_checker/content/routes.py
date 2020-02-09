from flask import Blueprint, request, jsonify
import subprocess
from subprocess import Popen

content = Blueprint("content", __name__)


def get_fdb_schema(fdb):
    p = Popen(
        ["fdb_gen", fdb],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    output, errors = p.communicate()
    return output


@content.route("/content/create_fdb", methods=["POST"])
def create_fdb():
    """
        Item 1: 15%

        GIVEN: expected_fdb_schema
        user_fdb_schema = extract fdb schema
        comapre user_fdb_schema and expected_fdb_schema
    """
    if request.method == "POST":
        username = request.get_data("username")
        users_fdb = "/home/user/{}/training/integrated_lab/".format(username)
        get_fdb_schema()
        expected = {
            "user_answer": "",
            "expected": "",
            "result": True,
        }
        return jsonify(expected)
    pass


@content.route("/content/extract_files", methods=["POST"])
def extract_files(files_path):
    """
        Item 2: 10%

        GIVEN: expected list of raw files
        check if expected list of files are in the directory files_path
    """
    if request.method == "POST":
        pass
    pass


@content.route("/content/transform_files", methods=["POST"])
def transform_files(slc):
    """
        Item 3: 15%

        GIVEN: expected_transformed_files
        run ngen using slc
        compare the generated files to the expected files
    """
    if request.method == "POST":
        pass
    pass


@content.route("/content/load", methods=["POST"])
def load(fdb):
    """
        Item 4: 10%

        GIVEN: expected fdb
        diff fdb and expected fdb
    """
    if request.method == "POST":
        pass
    pass


@content.route("/content/create_worflow", methods=["POST"])
def create_worflow(username):
    """
        Item 5: 25%

        GIVEN:
            - workflow name: username_content_lab
            - quetex       : username_test
            - DBL          : CIE_MANILA_TRAIN_DBL
            - schedule     : Mon - Fri, 6PM ET
        get workflow
        assert workflow name
        assert quetex used
        assert DBL used
        assert schedule
    """
    if request.method == "POST":
        pass
    pass


@content.route("/content/run_worflow", methods=["POST"])
def run_worflow():
    """
        Item 6: 5%

        GIVEN: expected dates
        get worflow runs
        get dates
        assert dates and expected dates
    """
    if request.method == "POST":
        pass
    pass


@content.route("/content/fdb_add_field_shares", methods=["POST"])
def fdb_add_field_shares(fdb):
    """
        Item 7: 5%

        check if shares field exists in fdb
    """
    if request.method == "POST":
        pass
    pass


@content.route("/content/fdb_add_field_mcap", methods=["POST"])
def fdb_add_field_mcap(fdb):
    """
        Item 8: 5%

        check if mcap field exists in fdb
    """
    if request.method == "POST":
        pass
    pass


@content.route("/content/fdb_shares_mcap_data_check", methods=["POST"])
def fdb_shares_mcap_data_check(fdb):
    """
        Item 9: 10%

        GIVEN: expected fdb
        diff fdb and expected fdb
    """
    if request.method == "POST":
        pass
    pass


@content.route("/content/is_equal", methods=["POST"])
def is_equal(arg1, arg2):
    try:
        assert arg1 == arg2
        return True
    except AssertionError:
        return False
