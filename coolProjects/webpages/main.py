from pywebcopy import save_webpage, save_website
import os
while True:
    try:
        os.system("clear")
        link = input("What is the link of the website/webpage you would like to download? --> ")
        type = input("If it is website, enter in sudo password. Else, enter! --> ")
        asname = input("Store as name? --> ")

        if type != "1436":
            save_webpage(
                url=link,
                project_folder="/home/aarush/webpages/",
                project_name=asname,
                bypass_robots=True,
                debug=True,
                open_in_browser=True,
                delay=None,
                threaded=False,)
        
        else:
            save_website(
                url=link,
                project_folder="/home/aarush/webpages/",
                project_name=asname,
                bypass_robots=True,
                debug=True,
                open_in_browser=True,
                delay=None,
                threaded=False,
            )
         
    except:
        print("An error occured! ")
    
