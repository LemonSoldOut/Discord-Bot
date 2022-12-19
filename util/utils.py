import os
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yaml
import pymysql

def checkDiscordInput(msg):
    if msg is None:
        return -1
    
    switch={
      'PYTHON':'python',
      'JAVA':'java',
      'C':'c',
      'GO':'go',
      'SHELL':'shell'
      }
    return switch.get(msg,"Invalid input")
# if __name__ == "__main__":
#     print(checkDiscordInput(1))

def checkOperatingSystem():
  if os.name == 'posix':
    os_name = 'linux' 
  elif os.name ==  'nt':
    os_name = 'windows'
  else:
    os_name = 'mac_os'
  return os_name


