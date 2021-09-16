# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1


# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set


# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres


# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets

album_set1, album_set2


# Find the intersections

intersection = album_set1 & album_set2
intersection


# Find the difference in set1 but not set2

album_set1.difference(album_set2)


# Check if superset

set(album_set1).issuperset(album_set2)   


# Check if subset

set({"Back in Black", "AC/DC"}).issubset(album_set1) 


# Check if superset

album_set1.issuperset({"Back in Black", "AC/DC"})   
# Find the union of two sets
album_set1.union(album_set2)
