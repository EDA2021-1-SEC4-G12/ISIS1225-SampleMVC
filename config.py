import os
import sys
sys.path.append('../')

file_path = os.path.join(os.path.dirname('__file__'), '..')
file_dir = os.path.split(os.getcwd())[0]
# file_dir = os.path.dirname(os.path.realpath('__file__'))
# sys.path.insert(0, os.path.abspath(file_path))
data_dir = file_dir + '/Data/'