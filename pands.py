import  pandas as ps


# extacting data from website

#Simpsons=ps.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_1_(1989%E2%80%9390)')
#print(len(Simpsons))
#using football-data uk website
#extracting cvs file 
df_premier21=ps.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')
#rename columns
df_premier21.rename(columns={'AvgCAHA':'home_goals'},inplace=True)
print(df_premier21)