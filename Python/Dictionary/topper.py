#8.18
score={'Amar':[1,2,3,4],'Akbar':[5,6,7,8],'Anthony':[9,10,1,2]}
net={k:sum(v) for k,v in score.items()}
maxscore=max(net.values())
print('Topper :',list(net.keys())[list(net.values()).index(maxscore)],maxscore)