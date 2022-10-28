def get_filename(df):
    if df["Show"] == 'FluencyBank':
        epid_id = str(df["EpId"]).rjust(3, '0')
        filename = f'{df["Show"]}_{epid_id}_{df["ClipId"]}.wav'
    else:      
        filename = f'{df["Show"]}_{df["EpId"]}_{df["ClipId"]}.wav'
    return filename