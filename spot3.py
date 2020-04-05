import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import io
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd

cid='e0f3eb6acdbe493cada7c48b6ec4cd4c'
secret='6442789f133d4dd38de9cce0be251570'

client_credentials_manager=SpotifyClientCredentials(client_id=cid,client_secret=secret)
sp=spotipy.Spotify(client_credentials_manager=client_credentials_manager)
response = requests.get('https://spotifycharts.com/regional/global/weekly/latest/')
print(response.status_code)
soup = BS(response.text)
print(soup.title)
w=soup.a['href']

x='https://spotifycharts.com'+w
res=requests.get(x)
s=requests.get(x).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
s=requests.get(x).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
cols=['Rank','Track','Artist','Streams','URL']
c.columns=cols
c=c.drop(0,0)

xx=[]
for i in range(len(c)):
    xxx=(c['URL'].values[i])
    xx.append(xxx.rsplit('/', 1)[1])

track_id=xx
c['track_id']=xx
rows = []
batchsize = 10
None_counter = 0

for i in range(0,len(track_id),batchsize):
    batch = track_id[i:i+batchsize]
    feature_results = sp.audio_features(batch)
    for i, t in enumerate(feature_results):
        if t == None:
            None_counter = None_counter + 1
        else:
            rows.append(t)            
print('Number of tracks where no audio features were available:',None_counter)

df_audio_features = pd.DataFrame.from_dict(rows,orient='columns')
print("Shape of the dataset:", df_audio_features.shape)

columns_to_drop = ['analysis_url','track_href','type','uri']
df_audio_features.drop(columns_to_drop, axis=1,inplace=True)

df_audio_features.rename(columns={'id': 'track_id'}, inplace=True)

print(df_audio_features.shape)
c=c.merge(df_audio_features)
c.to_csv('C://Users//verma//Downloads//top_tracks2.csv')