import sys
import pdb
import os

import numpy as np

sys.path.append(os.path.abspath('../download'))
sys.path.append(os.path.abspath('../text_analysis'))

# changed imports to include entire filepath from source
from Text_analysis.main.text_analysis.website_text import website_text

path = "../../out/"
year = None
wtext = website_text(domain = "webflakes.com", path = "../../out/", year = None)
lens = [len(x) for x in wtext.texts]

domain = 'www.finitecarbon.com'
wtext = website_text(domain = domain, path = path, year = year)



path = '../../out_public'
year = 2015
domain = 'www.northwesternenergy.com'
wtext = website_text(domain = domain, path = path, year = year)


i = np.where(self.website_info.website.str.contains('webflakes'))[0][0]
print (i)
