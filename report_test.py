import pandas as pd
import os

file = os.path.join(
        os.path.dirname(__file__), 'payments.xlsx'
)


data = pd.read_excel(file)


