from flask import Flask, Blueprint, render_template

bp = Blueprint('appointment',__name__,url_prefix='/')

@bp.route('/appointment.html')
def result():
    return render_template('appointment.html')