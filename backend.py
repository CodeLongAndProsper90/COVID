import csv
import time
import os
import matplotlib.pyplot as plt
import cv2
from imageio import imwrite

def get_file():
  url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
  import requests
  r = requests.get(url)

  with open('cases.csv', 'wb') as f:
      f.write(r.content)

  # Retrieve HTTP meta-data
  print(r.status_code)
  print(r.headers['content-type'])
  print(r.encoding)

def get_cases(stat):
  x = []
  y = []
  dat = 0
  temp = [ c for c in stat]
  temp[0] = temp[0].upper()
  state = ""
  for item in temp:
    state+=item
  print(state)
  reader = csv.DictReader(open("cases.csv"))
  for raw in reader:

    if raw['state'] == state:
      dat+=1
      x.append(dat)
      y.append(raw['cases'])
    else:
      continue
  fig = plt.figure(figsize=(16,12))
  fig.suptitle("COVID-19 cases in "+ stat)
  axes= fig.add_axes([0.1,0.1,0.8,0.8])
  axes.plot(x, y)
  plt.ylabel('Cases')
  plt.xlabel("Days since 2020-01-21")
  fig.savefig('static/plots/plot.png', bbox_inches='tight')
def overwrite():
  import numpy as np
  img = np.zeros([100,100,3],dtype=np.uint8)
  img.fill(255) # or img[:] = 255
  imwrite('static/plots/plot.png', img)