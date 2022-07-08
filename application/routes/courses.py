from flask import Flask, Blueprint, render_template
from flask import request
# import tensorflow as tf
# from tensorflow.keras import datasets, utils
# from tensorflow.keras import models, layers, activations, initializers, losses, optimizers, metrics

import pandas as pd
import numpy as np

import jinja2
from pycaret.regression import *

bp = Blueprint('courses',__name__,url_prefix='/')

@bp.route('/courses.html')
def result():
    return render_template('courses.html')


@bp.route('/predict')
def PredictionSpecialSale():
    vname = request.args.get('vname')
    vmodel = request.args.get('vmodel')
    voption = request.args.get('voption')
    vyear = request.args.get('vyear')
    ftype = request.args.get('ftype')
    odometer = request.args.get('odometer')
    
    Input = pd.DataFrame({
        'model':[vmodel],
        'option':[voption],
        'year':[vyear],
        'fuel':[ftype],
        'odometer':[int(odometer)],
        'car':[vname],
    })
    loaded_model = load_model('final_AutoML_model')

    ModelOutput = loaded_model.predict(Input)
    

    return render_template('courses.html', Output = ModelOutput)