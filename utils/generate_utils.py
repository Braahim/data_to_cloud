import streamlit as st
import random
import datetime, time
import random
import logging
import pandas as pd
import numpy as np
import base64
import hashlib
import time

chemical_array = [
    "Mercure-Hg",
    "Nickel-Ni",
    "Chrome-Cr",
    "Zinc-Zn"

]

def generate_data(num_lines):
    data = []
    for i in range(num_lines):
        timestamp = datetime.datetime.now()
        element = random.choice(chemical_array)
        value = random.randint(0, 100)
        time.sleep(0.5)
        data.append((timestamp, element, value))
    return pd.DataFrame(data, columns=["Timestamp", "Element", "Value"])

