# -*- encoding: utf-8 -*-
import pandas as pd
import numpy as np
from pandastable import Table, TableModel

from layout import *


def view(app, df):
    columns = app.lb2.get(0, END)
    if app.include.get():
        columns = columns
    else:
        columns = [x for x in df.columns.values if x not in columns]

    select_df =  df[list(columns)].replace(np.nan, '', regex=True)

    pt = Table(app.table_frame, dataframe=select_df)
    pt.show()


def show_selectedColumns_dataframe(df):
    try:
        df_name = df.name
    except:
        df_name = "DataFrame"

    app = layout()
    app.main.title(str(df_name)+" "+str(df.shape))
    button = Button(app.control_frame, text="View", command=lambda: view(app, df))
    button.pack()
    button.place(x=button_x, y=button_y, width=button_width)

    index = 0
    for column in list(df.columns.values):
        index = index + 1
        app.lb1.insert(index, column)

    app.mainloop()

if __name__ == "__main__":
    csvfile = "check.csv"
    df = pd.read_csv(csvfile)
    show_selectedColumns_dataframe(df)

