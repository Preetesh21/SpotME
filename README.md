# Spotify Artists Analysis

The purpose of this project is to analyze and rate the artists based upon their popularity, genres and the extent of the followers which they possess.The work also includes the rating of the top tracks of the past decade based upon the different parameters as provided by the spotify track analyser and also compare the top tracks of the past decade with the ones which currently preside over the top charts in 2020.

![VGG16 Model Architecture](data/logo.jpg)


For the study, I will access the [Spotify Web API](https://beta.developer.spotify.com/web-api/), which provides data from the Spotify music catalog and can be accesed via standard HTTPS requests to an API endpoint. The Spotify API provides, among other things, track information for each song, including audio statistics such as *danceability*, *instrumentalness* or *temp*. I will focus on retrieving this audio feature information from different playlists of the previous year and also the artists. Each feature measures an aspect of a song. Detailed information on how each feature is calculated can be found in the Spotify API Website.

The project containes the code used for retreival of the data using the API and then the notebook where the data analysis has been performed also the details of the algorithm used to rate the artists and the tracks.

Library used:
```
pip install spotipy
```

