from flask import Flask, render_template
import requests
import json
import logging
from logging.handlers import RotatingFileHandler
import db_api

SERVICE_PORT = 8000

app = Flask(__name__)


@app.route('/data/')
def show_data():
    """
    Function to show the table data
    """
    try:
        data = db_api.select_all_data_from_table()
    except Exception as excep:
        app.logger.error('Error occurred while showing table data'
                         + str(excep))
    return render_template('index.html', rows=data)


@app.route('/data/<string:id>')
def show_data_by_id(id):
    """
    Function to show the specific row
    Queried by the id
    """
    try:
        id_data = db_api.select_data_by_id(id)
    except Exception as excep:
        app.logger.error('Error occurred while retrieving ID'
                         + str(excep))
    return render_template('index.html', rows=id_data)


if __name__ == "__main__":
    # Logging
    handler = RotatingFileHandler('app_logger.log', maxBytes=10000,
                                  backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=SERVICE_PORT)
