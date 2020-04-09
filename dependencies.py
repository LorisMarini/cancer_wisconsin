import os
import pandas as pd
import numpy as np
import warnings
import graphviz
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams

from scipy.optimize import curve_fit
from scipy.optimize import fsolve

from IPython.display import SVG
from IPython.core.interactiveshell import InteractiveShell
from IPython.core.display import display, HTML

import sklearn
from sklearn import tree

from sklearn.datasets import make_classification

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve

from sklearn.pipeline import make_pipeline

from sklearn.dummy import DummyClassifier
from sklearn.dummy import DummyRegressor

from sklearn.utils.random import sample_without_replacement
