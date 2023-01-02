#-*- coding:UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import random
from matplotlib import font_manager
import numpy as np
df = pd.read_excel("PvtyPrv.xlsx")
select = [2007,2008,2009,2010,2012,2013,2014,2015,2017,2018,2019]
tag = df[['Year']].applymap(lambda x:x in select).any(1)
b = df[~tag]
c = b.reindex(columns = ['Geography','Year'])
print(c)
#b.to_excel('1.xlsx')