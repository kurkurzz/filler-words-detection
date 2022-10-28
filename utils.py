import librosa

DATASET_PATH = 'SEP-28k dataset'

def get_filename(df):
    if df["Show"] == 'FluencyBank':
        epid_id = str(df["EpId"]).rjust(3, '0')
        filename = f'{df["Show"]}_{epid_id}_{df["ClipId"]}.wav'
    else:      
        filename = f'{df["Show"]}_{df["EpId"]}_{df["ClipId"]}.wav'
    return filename

def extract_mfcc(df):
    try:
        folder_name = 'clips'
        # if df['is_augmented'] == 0:
        #     folder_name = 'clips'
        # else:
        #     folder_name = 'augmented_fluencybank_um_clips'
        audio, sr = librosa.load(f'{DATASET_PATH}/{folder_name}/{df["filename"]}', sr=16000)
        mfcc = librosa.feature.mfcc(audio, sr, n_mfcc=13)
        return mfcc
    except:
        return None
	
def check_valid_shape(mfcc, shape):
    if mfcc is None:
        return 0
    if mfcc.shape != shape:
        return 0
    return 1