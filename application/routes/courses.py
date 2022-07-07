from flask import Flask, Blueprint, render_template

bp = Blueprint('courses',__name__,url_prefix='/')

@bp.route('/courses.html')
def result():
    return render_template('courses.html')