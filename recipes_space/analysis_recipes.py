import json
import numpy as np
import matplotlib.pyplot as pl
import mpld3

def get_OFS(recipes):
   N=0
   res=[]   

   for r in recipes:
      oeuf=0
      farine=0
      sucre=0
      for ing in r['ingredients']:
         if "oeuf" in ing['content']:  oeuf=ing["quantity"] 
         if "farine" in ing['content']: farine=ing["quantity"]
         if "sucre" in  ing['content']: sucre=ing["quantity"]
      if (farine * oeuf * sucre): 
       f=farine/oeuf
       s=sucre/oeuf
       N+=1
       res.append([r['name'], f, s])
   return res

#fname="/home/kodda/Dropbox/recipes_space/750g_recipes.json"
#recipes=json.load(open(fname))
#res=get_OFS(recipes)


fig, ax = pl.subplots(subplot_kw=dict(facecolor='#EEEEEE'))
N = 100

scatter = ax.scatter(np.random.normal(size=N),
                     np.random.normal(size=N),
                     c=np.random.random(size=N),
                     s=1000 * np.random.random(size=N),
                     alpha=0.3,
                     cmap=pl.cm.jet)
ax.grid(color='white', linestyle='solid')

ax.set_title("Scatter Plot (with tooltips!)", size=20)

labels = ['point {0}'.format(i + 1) for i in range(N)]
tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
mpld3.plugins.connect(fig, tooltip)

mpld3.show()

