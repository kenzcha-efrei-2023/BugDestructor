import json
import pandas as pd
from Dataset import file_sashimi
from Dataset import stringify
import numpy as np

def conv_json():
    with open("Valeur_absolue_dun_nombre.json", "r") as read_file:
        data = json.load(read_file)
    json_string = json.dumps(data)
    df = pd.read_json(json_string)
    print(df)
    with open('test/output', 'w') as f:
        for i in df["answer"] :
            f.write(file_sashimi.remove_char(file_sashimi.remove_char(i,'\n'),'\r')+"\n")

def create_dataf():
    with open("test/output", "r") as f :
        ar = np.array(f.readlines())
    with open("test/res", "r") as f :
        ar2 = np.array(f.readlines())
        for i in range(len(ar2)):
            ar2[i] = ar2[i][:-1]
    df = pd.DataFrame(ar, columns=["answer"])
    df["is_true"] = ar2
    # cut each answers in the dataframe into units (lexems)
    tab = file_sashimi.sashimi_df(df)
    # convert the lexems in chars
    tab = stringify.lex_to_str(tab)
    # put it in the dataframe
    df["answer"] = pd.array(tab)
    df.to_csv(r'val_abs.csv', index=False)

#conv_json()

create_dataf()