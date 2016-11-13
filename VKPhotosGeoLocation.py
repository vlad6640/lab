import vk
import time
print('VKPhotos Geo Location')
session = vk.Session('7fd52be80a52349b82d84d744e6c70d4514650bb7c6207dec7e817bc266f20ef382ea13c9060417ee3072')
api = vk.API(session)
friends = api.friends.get()
friends_info = api.users.get(user_ids=friends)
geolocation = []
for friend in friends_info:
        print('ID: %s Имя: %s %s' % (friend['uid'], friend['last_name'], friend['first_name']))
        id = friend['uid']
        albums = api.photos.getAlbums(owner_id=id)
        print('\t...альбомов % s...' % len(albums))
        for album in albums:
            try:
                photos = api.photos.get(owner_id=id, album_id=album['aid'])
                print('\t\t...обрабатываем фотографии альбома...')
                for photo in photos:
                    if 'lat' in photo and 'long' in photo:
                        geolocation.append((photo['lat'], photo['long']))
                print('\t\t...найдено %s фото...' % len(photos))
            except:
                pass
            time.sleep(0.5)
        time.sleep(0.5)
js_code = ""
for loc in geolocation:
    js_code += 'new google.maps.Marker({position: {lat: %s, lng: %s}, map: map }); \n' % (loc[0], loc[1])
html = open('map.html').read()
html = html.replace('/* PLACEHOLDER */ ', js_code)
f = open('VKPhotosGeoLocation.html', 'w')
f.write(html)
f.close()
