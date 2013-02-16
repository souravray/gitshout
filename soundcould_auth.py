import pprint
import soundcloud
    
client = soundcloud.Client(client_id='4eec1aa74b671b39539104d50f82d743',client_secret='1b9d84a2e1964874769a79215fa1a050',username='AnitRai',password='pravin')
#client = client.get('/me')
#track = client.get('/tracks/30709985')
#print track.title

track = client.post('/tracks', track={
	'title': 'This is a sample track',
	'sharing': 'private',
	e'asset_data': open('file.wav', 'rb')
})


print 'File Uploaded......!'
