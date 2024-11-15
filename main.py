import json
import csv


songs=[]
titles=[]
years=[]
count_year=[]

with open("spotify.csv","r", encoding='utf') as csv_file:
         reader=csv.DictReader(csv_file)
         for line in reader:
                 songs.append(line)

with open("spotify.json","w", encoding='utf8') as json_file:
    json.dump(songs, json_file, indent=4)

count=0
for song in songs:
       print(song['Title'])
       if song['Year'] not in years:
              years.append(song['Year'])

song_count=0
for year in years:
    for song in songs:
           if song['Year']==year:
                song_count+=1
    count_year.append(song_count)
print(year)
print(count_year)
              

print(years)
print(count_year)


''' reader=csv.reader(f)
for i in reader:
titles.append(i[0])
year.append(i[3])
print(titles[1::1])
print(list(year[1::1]))'''