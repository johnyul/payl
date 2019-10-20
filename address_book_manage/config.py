import os
import configparser


project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


"""
    configer
"""
configer = configparser.ConfigParser()
current_dir = os.path.dirname(os.path.realpath(__file__))
configer.read(os.path.join(current_dir, 'config.ini'), encoding="utf-8")

#print(configer['general']['id_format'])
#if not configer.has_section('date'):
#    configer.add_section('date')
# 
#if not configer.has_option('date', 'xxx'):
#    configer.set('date', 'yyy', 'zzz')

