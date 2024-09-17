file_path =  "Statements09012880575361(1).xlsx"

import pandas as pd

df = pd.read_excel(file_path, engine="openpyxl").to_numpy()
