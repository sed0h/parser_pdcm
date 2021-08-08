import chardet

if __name__ == '__main__':
    dbc_file = 'dbcs/m_CANCluster.dbc'
    with open(dbc_file, 'rb') as f:
        data = f.read()
        encoding_type = chardet.detect(data)
        print(encoding_type)
    f = open(dbc_file, 'r', encoding=encoding_type['encoding'])
    for line in f.readline():
        print(line)