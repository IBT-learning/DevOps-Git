import os
import datetime

current_date=datetime.datetime.now()
max_age=10

# for dirpath, dirname, filename in os.walk("/etc"):

for dir,dirpath,filename in os.walk("/var/log"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)          => comp=complete
        file_stat=os.stat(comp_path)
        file_ctime=file_stat.st_ctime
        file_creation_date= datetime.datetime.fromtimestamp(file_ctime)

        diff_in_days=(current_date - file_creation_date).days
        if diff_in_days > max_age:
            # os.remove(comp_path)
            print(comp_path, diff_in_days)

