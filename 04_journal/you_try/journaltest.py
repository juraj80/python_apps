import os

def load(name):
    data = []
    filename = os.path.abspath(os.path.join('.','journals2',name+'.jrl'))
    if os.path.exists(filename):
        with open(filename,'r') as fin:
            for line in fin.readlines():
                data.append(line.rstrip())
    return data

def add_entry(data,text):
    data.append(text)


def save(name,data):
    print('Saving journal')
    filename = os.path.abspath(os.path.join('.', 'journals2', name + '.jrl'))
    print('filename',filename)
    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry+'\n')