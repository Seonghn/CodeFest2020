import pandas as pd
from sklearn.model_selection import train_test_split


def prep(path,test_size, random_state):
    df = pd.read_csv(path)
    del df['apk_name']
    df['ware'].replace(['benign','malware'],range(2),inplace=True)
    y = df['ware']
    cpdf = df
    del cpdf['ware']
    x = cpdf
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)
    return x_train, x_test, y_train, y_test, x, y






