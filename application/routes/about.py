from flask import Flask, Blueprint, render_template

bp = Blueprint('about',__name__,url_prefix='/')

@bp.route('/about.html')
def result():
    return render_template('about.html')