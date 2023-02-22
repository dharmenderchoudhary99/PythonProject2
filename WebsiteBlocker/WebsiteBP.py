import datetime
import time


end_time=datetime.datetime(2023,2,24)#Give time for how many days you should block the website
site_block=["https://www.facebook.com/login/"]
host_path="host directory path"
redirect = "LOCALHOST "#Enter your localhost id

while True:
    if datetime.datetime.now()<end_time:
        print("Blocking started")
        with open(host_path,"r+") as host_file:
            content=host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect+ " " +website+"\n")
                else:
                    pass
    else:
        with open(host_file,"r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            host_file.truncate()

        time.sleep(5)