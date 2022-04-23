
import subprocess
import os
import sys
from IPython.core.debugger import set_trace

key = "sp=racwl&st=2022-04-23T09:19:43Z&se=2022-04-23T17:19:43Z&spr=https&sv=2020-08-04&sr=c&sig=wZQvrrDjjKF4OcKAp4UP2OOQLgwLqMxdKZ3BmouRFw0%3D"
mycontainer = "databricks-data?"
exepath = "/home/ubuntu/azcopy_linux_amd64_10.14.1/azcopy"
local_directory = "/home/ubuntu/projects/RCA/"
endpoint = "https://assetmgmstorage.blob.core.windows.net/"+ mycontainer

myscript = "sudo " + exepath + " copy " + '"' + local_directory + "*.xlsx" + '"' + " " + '"' + endpoint + key + '"'

subprocess.call(myscript, shell=True)