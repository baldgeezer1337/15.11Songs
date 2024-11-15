import pandas as pd

songs=[]
with open("spotify.csv","r", encoding='utf') as csv_file:
         reader=csv.DictReader(csv_file)
         for line in reader:
                 songs.append(line)

df=pd.DataFrame(songs)

df.to_json('spotify.json', indent=4)

years=df['Year'].unique()
count_year=[]

for year in years:
        song_count=df[df['Years']==years].shape[0]
        count_year.append(song_count)

print(years)
print(count_year)