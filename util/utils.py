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

if __name__ == "__main__":
    print(checkDiscordInput(1))
