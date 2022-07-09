from flask import Flask, Blueprint, render_template
from flask import request
# import tensorflow as tf
from tensorflow.keras import datasets, utils
from tensorflow.keras import models, layers, activations, initializers, losses, optimizers, metrics

import pandas as pd
import numpy as np

# import jinja2
# from pycaret.regression import *

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
    odometer = int(request.args.get('odometer'))
    
    ## pycaret result
    # Input = pd.DataFrame({
    #     'model':[vmodel],
    #     'option':[voption],
    #     'year':[vyear],
    #     'fuel':[ftype],
    #     'odometer':[int(odometer)],
    #     'car':[vname],
    # })
    # loaded_model = load_model('final_AutoML_model')

    # ModelOutput = loaded_model.predict(Input)

    ## DL result
    train_df = pd.DataFrame(pd.read_csv('/Users/krc/git/usedcar_pricing/application/routes/train_df.csv')).iloc[:,1:]
    cols = list(train_df.drop('price',axis=1).columns)

    temp = [0] * 1104
    odometer_MinMax = (odometer - train_df['odometer'].min(axis=0)) / (train_df['odometer'].max(axis=0) - train_df['odometer'].min(axis=0))
    temp[0] = odometer_MinMax
    temp[cols.index('car_'+vname)] =1
    temp[cols.index('model_'+vmodel)] =1
    temp[cols.index('option_'+voption)] =1
    temp[cols.index('year_'+vyear)] =1
    temp[cols.index('fuel_'+ftype)] =1
    
    reconstructed_model = models.load_model("/Users/krc/git/usedcar_pricing/application/routes/DL_model")
    ModelOutput = reconstructed_model.predict(np.array(temp).reshape(1,-1))

    return render_template('courses.html', Output = ModelOutput[0][0])