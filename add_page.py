import os
import time
import json
page_title = input("Enter the page title: ")
category = input("Enter the page category: ")
date = input("Enter the date (Mon dd, yyyy): ")

data = {
    "Title": page_title,
    "Date": date,
    "Content": category + "/" + page_title + ".txt"

}


if not os.path.exists("entries/" + category + "/" ):
    os.makedirs("entries/" + category + "/")
if not os.path.exists("entries/" + category + "/" + page_title + ".json"):
    with open("entries/" + category + "/" + page_title + ".json", 'w') as f:
        json.dump(data,f)
if not os.path.exists("entry_data/" + category + "/" ):
    os.makedirs("entry_data/" + category + "/")
if not os.path.exists("entry_data/" + category + "/" + page_title + ".txt"):
    with open("entry_data/" + category + "/" + page_title + ".txt", 'w') as f:
        pass
print("Begin editing : " + "entry_data/" + category + "/" + page_title + ".txt\nDon't forget to build with `python3 load_template.py`")
