import os 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import MetaTrader5 as mt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from datetime import datetime, timedelta

