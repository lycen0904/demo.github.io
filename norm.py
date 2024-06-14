import librosa
import os,tqdm
import multiprocessing as mp
import soundfile as sf
from glob import glob

def resample_one(filename):
    singer=filename.split('/')[-2]
    songname=filename.split('/')[-1].split('_')[0]+'.wav'
    output_path='/Users/grace/Desktop/GitHub/lycen0904.github.io/vc_norm/'+singer+'/'+songname
    # if os.path.exists(output_path):
    #     return
    wav, sr = librosa.load(filename)
    # normalize the volume
    wav = wav / (0.00001+max(abs(wav)))*0.95
    # write to file using soundfile
    try:
        sf.write(output_path, wav, sr)
    except:
        print("Error writing file",output_path)
        return

def mkdir_func(input_path):
    singer=input_path.split('/')[-2]
    out_dir = '/Users/grace/Desktop/GitHub/lycen0904.github.io/vc_norm/'+singer
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

def resample_parallel():
    input_paths = glob('/Users/grace/Desktop/GitHub/lycen0904.github.io/vc_new/norm/*.wav')  
    print("input_paths",len(input_paths))
    # multiprocessing with progress bar
    for i in input_paths:
        resample_one(i)

def path_parallel():
    input_paths = glob('/Users/grace/Desktop/GitHub/lycen0904.github.io/vc_new/norm/*.wav')
    input_paths = list(set(input_paths)) # sort
    print("input_paths",len(input_paths))
    for input_path in input_paths:
        mkdir_func(input_path)

if __name__ == "__main__":
    path_parallel()
    resample_parallel()

