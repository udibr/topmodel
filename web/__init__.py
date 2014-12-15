from flask import Flask, g
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # Must be called before importing pyplot

from topmodel.file_system import LocalFileSystem, S3FileSystem
from topmodel import settings

# Make plots pretty
pd.set_option('display.mpl_style', 'default')
app = Flask(__name__)


@app.before_request
def before_request():
    if app.local:
        g.file_system = LocalFileSystem()
    else:
        config = settings.read_config('./config.yaml')
        g.file_system = S3FileSystem(config)

import web.views.pages
