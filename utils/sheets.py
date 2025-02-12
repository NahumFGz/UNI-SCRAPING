import pandas as pd
import pygsheets


def authenticate(credentials_path, name_id_or_url, key_type="name"):
    gc = pygsheets.authorize(service_file=credentials_path)

    if key_type == "name":
        sh = gc.open(name_id_or_url)
    elif key_type == "id":
        sh = gc.open_by_key(name_id_or_url)
    elif key_type == "url":
        sh = gc.open_by_url(name_id_or_url)

    return gc, sh


def sheet_to_dataframe(sh, sheet_name):
    worksheet = sh[1].worksheet_by_title(sheet_name)
    dataframe = worksheet.get_as_df(numerize=False)

    return dataframe


def dataframe_to_sheet(sh, new_dataframe, destination_sheet_name):

    # Si newDatFrame es vacio, crear una fila vacia
    if new_dataframe.shape[0] == 0:
        df_vacio = pd.DataFrame([[""] * len(new_dataframe.columns)], columns=new_dataframe.columns)
        new_dataframe = pd.concat([new_dataframe, df_vacio], ignore_index=True)

    # Obtener hoja destino
    worksheet = sh[1].worksheet_by_title(destination_sheet_name)
    worksheet.rows = 2

    try:
        worksheet.rows = new_dataframe.shape[0]
        worksheet.cols = new_dataframe.shape[1]
        worksheet.set_dataframe(new_dataframe, start="A1", copy_index=False)
    except:
        worksheet.rows = new_dataframe.shape[0] + 2
        worksheet.cols = new_dataframe.shape[1] + 2
        worksheet.set_dataframe(new_dataframe, start="A1", copy_index=False)
