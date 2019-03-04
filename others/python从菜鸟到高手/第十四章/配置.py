import configparser
cfg = configparser.ConfigParser()
cfg.read('xxx.conf')
print(cfg)
print(cfg['english']['greeting'])