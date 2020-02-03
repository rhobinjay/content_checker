from flask import request, jsonify, render_template
from content_checker.models import User, ContentIntegratedLab
from content_checker import app
import pdb


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/')
@app.route('/content', methods=['GET', 'POST'])
def content():
    users = User.query.all()
    return render_template('content.html', users=users)


@app.route('/content/<string:username>', methods=['GET', 'POST'])
def content_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    integratedlabs = ContentIntegratedLab.query.filter_by(user=user).all()
    # pdb.set_trace()
    return render_template('content_user.html', user=user, integratedlabs=integratedlabs)


########################################################
# API Calls
########################################################
@app.route('/content/check/<user>', methods=['POST'])
def function(user):
    if request.method == 'POST':
        schema_file = request.form.get('schema_file')
        expected = '/path/to/schema_file'
        return jsonify({
            'user_answer': schema_file,
            'expected': expected,
            'result': is_equal(schema_file, expected)
        })
    return jsonify({'test': 'get'})


@app.route('/content/check/1', methods=['POST'])
def item_1():
    if request.method == 'POST':
        schema_file = request.form.get('schema_file')
        expected = '/path/to/schema_file'
        return jsonify({
            'user_answer': schema_file,
            'expected': expected,
            'result': is_equal(schema_file, expected)
        })
    return jsonify({'test': 'get'})


def is_equal(arg1, arg2):
    try:
        assert arg1 == arg2
        return True
    except AssertionError:
        return False
