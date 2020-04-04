import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd

cid='e0f3eb6acdbe493cada7c48b6ec4cd4c'
secret='6442789f133d4dd38de9cce0be251570'

client_credentials_manager=SpotifyClientCredentials(client_id=cid,client_secret=secret)
sp=spotipy.Spotify(client_credentials_manager=client_credentials_manager)

x=[]
y=[]
z=[]
a=[]
b=[]
for i in range(0,1000,20):
    track_results = sp.search(q='year:2017', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

print(type(track_results))

for i in range(0,1000,20):
    track_results = sp.search(q='year:2018', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

for i in range(0,1000,20):
    track_results = sp.search(q='year:2016', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

for i in range(0,1000,20):
    track_results = sp.search(q='year:2015', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

for i in range(0,1000,20):
    track_results = sp.search(q='year:2014', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

for i in range(0,1000,20):
    track_results = sp.search(q='year:2013', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

for i in range(0,1000,20):
    track_results = sp.search(q='year:2012', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

for i in range(0,1000,20):
    track_results = sp.search(q='year:2011', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

for i in range(0,1000,20):
    track_results = sp.search(q='year:2010', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

for i in range(0,1000,20):
    track_results = sp.search(q='year:2009', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

for i in range(0,1000,20):
    track_results = sp.search(q='year:2008', type='artist', limit=50,offset=i,market='US')
for items in (track_results['artists']['items']):
    x.append(items['followers'])
    y.append(items['genres'])
    z.append(items['name'])
    a.append(items['popularity'])
    b.append(items['id'])

print(len(x))

df_artists = pd.DataFrame({'artist_name':z,'followers':x,'genre':y,'popularity':a,'ID':b})
print(df_artists.shape)
df_artists.to_csv('C://Users//verma//Downloads//artists.csv')
