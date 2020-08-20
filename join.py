
import os
import zipfile
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(100000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['pihor.zip.000.COOL', 'pihor.zip.001.COOL', 'pihor.zip.002.COOL', 'pihor.zip.003.COOL', 'pihor.zip.004.COOL', 'pihor.zip.005.COOL', 'pihor.zip.006.COOL', 'pihor.zip.007.COOL', 'pihor.zip.008.COOL', 'pihor.zip.009.COOL', 'pihor.zip.010.COOL', 'pihor.zip.011.COOL', 'pihor.zip.012.COOL', 'pihor.zip.013.COOL', 'pihor.zip.014.COOL', 'pihor.zip.015.COOL', 'pihor.zip.016.COOL', 'pihor.zip.017.COOL', 'pihor.zip.018.COOL', 'pihor.zip.019.COOL', 'pihor.zip.020.COOL', 'pihor.zip.021.COOL', 'pihor.zip.022.COOL', 'pihor.zip.023.COOL', 'pihor.zip.024.COOL', 'pihor.zip.025.COOL', 'pihor.zip.026.COOL', 'pihor.zip.027.COOL', 'pihor.zip.028.COOL', 'pihor.zip.029.COOL', 'pihor.zip.030.COOL', 'pihor.zip.031.COOL', 'pihor.zip.032.COOL'],'pihor.zip')
print('unziping')
with zipfile.ZipFile('pihor.zip', 'r') as zip_ref:
    zip_ref.extractall('pihor')
os.remove('pihor.zip')
os.remove('join.py')
