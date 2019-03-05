import configparser
cfg = configparser.ConfigParser()
cfg.read('xxx.conf')
print(cfg)
print(cfg['english']['greeting'])


'''
CSV         xlrd
HDF5        h5py     PyTables

'''