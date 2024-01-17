import subprocess 
  
Data = subprocess.check_output(['wmic', 'product', 'get', 'name']) 
a = str(Data) 
  
print("Lists of All Installed Softwares:")
try:     
    for i in range(len(a)): 
        print(a.split("\\r\\r\\n")[6:][i]) 
  
except IndexError as e: 
    print("All Done")

print("=="*25)



import requests
import time
def check_speed(file_url):
    start_time = time.time()
    file = requests.get(file_url, stream=True)
    total_length = file.headers.get('content-length')
    if total_length is not None: 
        download_speed = int(total_length) / (time.time() - start_time)
        # download_limit = download_speed / (1024**3)
        return download_speed
speed = check_speed("https://link.testfile.org/PDF100MB")
print("Download Speed: ", speed)
print("=="*25)


import cpuinfo
my_cpuinfo = cpuinfo.get_cpu_info()
print(f"CPU Model: {my_cpuinfo['brand_raw']}")
print("=="*25)


import os
import psutil
cpu_count = os.cpu_count()
threads_count = psutil.cpu_count() / psutil.cpu_count(logical=False)
print("No. of CPU core is:",cpu_count)
print("No. of Threads per CPU core is:",threads_count)
print("=="*25)



total_ram = psutil.virtual_memory().total/(1024**3)
print("Total RAM is:",total_ram,"GB")
print("=="*25)



from win32api import GetSystemMetrics
Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)
Width_in = float(Width)
Height_in = float(Height)
print("Width = ",Width_in)
print("Height = ",Height_in)
print("=="*25)



import uuid, re
print("The MAC Address is:", end=" ")
print(':'.join(re.findall('..','%012x'% uuid.getnode())))
print("=="*25)



import requests
ip = requests.get('https://checkip.amazonaws.com').text.strip()
print("Public IP Address:",ip)
print("=="*25)



import sys
version = sys.getwindowsversion()
print("Windows version:",version[2])
print("=="*25)