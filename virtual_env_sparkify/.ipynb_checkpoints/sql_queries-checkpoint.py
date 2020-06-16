# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, start_time int, user_id int, level text,\
song_id int, artist_id int, session_id int, location text, user_agent text);
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (\
    user_id SERIAL PRIMARY KEY, first_name text, last_name text, gender text, level text);
""")

song_table_create = ("""  CREATE TABLE IF NOT EXISTS songs (\
    song_id SERIAL PRIMARY KEY , title text , artist_id int , year int, duration float);
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (\
    artist_id SERIAL PRIMARY KEY, name text, location text, latitude float, longitude float);
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time int , hour int, day int, week int, month int, year int, weekday int);
""")

# INSERT RECORDS

songplay_table_insert = (""")
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]