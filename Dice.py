import random
import plotly.express as px
import plotly.figure_factory as ff
count=[]
Dice_result=[]
for i in range(0,100):
    Dice1=random.randint(1,6)
    Dice2=random.randint(1,6)
    Dice_result.append(Dice1+Dice2)
    count.append(i)
fig=ff.create_distplot([Dice_result],["result"])
fig.show()
    