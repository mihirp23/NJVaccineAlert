#!/usr/bin/env python3

###################################################################
# Author : Mihir Patel
#   Date : 3/8/21
#   Desc : Web Scrape the NJ Bergen county webpage to get
#          the latest status for covid vaccine appointments.
#   File : checknj.py
###################################################################
import requests, bs4
import time

###################################################################
def main():
###################################################################

    print("connecting to NJ covid resource website.....")
    req_obj = requests.get("https://www.hackensackmeridianhealth.org/covid19/")
    req_obj.raise_for_status()

    # passing the features argument to avoid warning
    soup_obj = bs4.BeautifulSoup(req_obj.text, features="html.parser")

    alert = soup_obj.select('#pagealert2')
    print(alert[0].get_text())

    req_obj.close()
        

# main()

###################################################################
if __name__ == "__main__":
###################################################################
    main()
