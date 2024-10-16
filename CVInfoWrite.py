# coding: utf-8

#Author: Killo3967
#Description: This script create a CVInfo.txt file that contents the comic volumen number from the comic
#             customvalue "comicvine_volume" and write it in the directory of the comics serie. 
#             When you scrape the rest of the comics, the plugin "Comicvine Scrape" use this ID and assign 
#             it to the comics in the directory.
#             This way the scrapping is faster and you only need to search and scrape one comic, 
#             use this plugin and create the CVInfo.txt, and then scrape the rest, 
#             also reduce the number of request to ComicVine so it is no necesary to search all the comics, 
#             only get the data.
#             This file (CVInfo.txt) also prevent the lose of the database and permit to export the comic directory and then
#             scrape it off again without having to scrape it.
#             
#             Based in "gwhittey-pcode" project in https://gist.github.com/gwhittey-pcode/dbf853b36f1e790af672871ffa643694
#             
#Version: 1.4 
#Date:2024-10-16
 
#@Name CVInfoWrite
#@Hook Books
#@Enabled true
#@Description Writes a file name CVInfo.txt into folder of comic
#@Image CVInfoWrite_logo.png

import sys
debug = False

if debug:
    print(" ")
    print ("+++++++++++++    SYSTEM INFO     ++++++++++++++++")
    print (">>>>> EXECUTABLE: " + str(sys.executable))
    print (">>>>> VERSION: " + str(sys.version))
    print (">>>>> PLATFORM: " + str(sys.platform))
    print (">>>>> CODE PAGE: " + str(sys.getdefaultencoding()))
    for p in sys.path:
        print (">>>>> PATH: " + p)
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++")


def CVInfoWrite(books):
    print("")
    print("<<<<<<<< START PLUGIN TO CREATE CVINFO FILE  >>>>>>>>>>")
    for book in books:
        if books:
            s_comicvine_issue = book.Web
            s_comicvine_volume = book.GetCustomValue("comicvine_volume")
            print('\tCreating CVInfo.txt from comic: ' + book.FilePath)
            print('\tCVS_ID: ' + str (s_comicvine_volume))
            if s_comicvine_volume: 
                volume_url = "https://comicvine.gamespot.com/detective-comics/4050-%s/" % (s_comicvine_volume)
                cv_file = book.FileDirectory + '\CVInfo.txt'  
                try:
                    with open(cv_file, 'w') as f:
                        f.write(volume_url)
                        print("\tFile CVInfo.txt created with 4050-" + str(s_comicvine_volume) + " data")
                except PermissionError as e:
                    print("\tERROR ----> You have no rights to create CVinfo file in the comic directory" + str(e))
            else:
                print("\tERROR ----> This comic haven't ComicVine Volume data. Nothing to create.")
                print("\tPlease, scrape first this comic to get the data from ComicVine .")
        else:
            print('\tNo books selected. Exiting')
    print("<<<<<<<< END PLUGIN TO CREATE CVINFO FILE  >>>>>>>>>>")
    print("")
