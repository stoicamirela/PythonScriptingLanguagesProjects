#Task: get a list of at least 5 albums, year and artist (this exact order) and display artist followed by the title of the album
#i used a list of 5 tuples that contain the respective informations

albums = [('Lifted', '2019', 'CL'), ('Bad', '1987', 'Michael Jackson'),
          ('Spirits Having Flow', '1979', 'Bee Gees'), ('Begin here', '1965', 'The Zombies'),
          ('Morrison Hotel', '1970', 'The Doors1')]

for i in range(len(albums)):
    print(albums[i][2], "-", albums[i][0])
