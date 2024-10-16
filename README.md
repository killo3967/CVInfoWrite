# CVInfoWrite
ComicRack script to create CVInfo.txt file 

This script create a CVInfo.txt file that contents the comic volumen number from the comic
customvalue "comicvine_volume" and write it in the directory of the comics serie. 
When you scrape the rest of the comics, the plugin "Comicvine Scrape" use this ID and assign 
it to the comics in the directory by this way the scrapping is faster and you only need to search
and scrape one comic, use this plugin and create the CVInfo.txt, and then scrape the rest, 
also reduce the number of request to ComicVine so it is no necesary to search all the comics, 
only get the data.
The file (CVInfo.txt) also prevent the lose of the database and permit to export the comic directory and then
scrape it off again without having to scrape it.

Based in "gwhittey-pcode" project in https://gist.github.com/gwhittey-pcode/dbf853b36f1e790af672871ffa643694
