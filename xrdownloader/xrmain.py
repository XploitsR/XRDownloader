#!/usr/bin/env python3
# -*-coding: utf8;-*-

#####################\
# XRDownloader v1.0.4
#####################/

#----------------------------------------------------------------------------
# MIT License

# Copyright (c) 2019 XploitsR

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#------------------------------------------------------------------------------

import urllib3
import certifi
import os,time
import sys,re

# count number of lines in the file links file
def rawincount(filename):
    num_lines = 0
    with open(filename) as f:
      for line in f:
        if len(line.strip()) < 1:
          continue
        else:
          num_lines += 1
    return num_lines
# xrdownloader's banner
def banner():
     import pyfiglet
     print(pyfiglet.figlet_format("XRDOWNLOADER", font='slant'))
# print preparing to download
def pre(arg):
  os.system("clear")
  banner()
  time.sleep(2)
  print("""
##############################################################|
#   [*] Preparing to download-->({0})->file(s)
##############################################################|
""".format(arg))
  time.sleep(2)

# write fetched data to a file
def write_to_file(dataHeader,url_split,typeO,dataStream):
   import math
   from tqdm import tqdm
   total_size = dataHeader; 
   block_size = 1024
   wrote = 0
   print(" ")
   # write downloaded file to its named-file on same directory
   with open(str(url_split),typeO) as f:
     if f is not None:
         for cont in tqdm(dataStream, total=math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
            wrote = wrote  + len(cont)    
            f.write(cont)
         if total_size != 0 and wrote == total_size:
           print("[+] downloaded->{0}".format(str(url_split)))
           f.close()

def main(xrurl,typeO):
        """
        Contains all functions
        """
        
        # check for empty value
        if len(str(xrurl)) < 1:
           time.sleep(2)
           print("""
##############################################################|
#   [!] Don't be silly, url cant be empty.
##############################################################|
""")
           sys.exit()
        # check if input is not a list
        if type(xrurl) != list:
           try:  
            check_usrF = os.path.isfile(xrurl)
           except:
            check_usrF = False
           # check if xrurl is a file
           if check_usrF == True:
              f = open(str(xrurl).strip())
              if len(str(f).strip()) > 1:
                if rawincount(xrurl) == 0:
                  time.sleep(2)
                  print("""
##############################################################|
#   [!] Don't be silly, file cant be empty
##############################################################|
""")
                  sys.exit()
                else:
                 pre(rawincount(xrurl))
                 xrurl = f
           else:
              pre(len([xrurl]))
              xrurl = [xrurl]
        # check if input is exact... list
        elif type(xrurl) == list:
           pre(len(xrurl))
           xrurl = xrurl
        count = 0
        # start iterating the urls
        for url in xrurl:
          # convert url to string -> str:
          url = str(url).lower()
          if len(url.strip()) < 1:
             continue
          url_split = str(url.strip()).split("/")
          chk_git = str(url_split[-1]).lower().split(".")
          if chk_git[-1] == "git":
             print("""
##############################################################|
#   [!] Don't be silly, can't download git files
##############################################################|
""")
             print("[-] please download git files with (git clone) command in your terminal")
             sys.exit()
          count += 1
          # check for invalid link type
          if len(str(url_split[-1]).strip()) < 1:
             url_split[-1] = "{0}-unknown-file".format("-".join(url_split))
          print("""
###############################################################|
#   [+] Downloading-->{0}---->({1})                      
###############################################################|
                """.format(str(url_split[-1]),count))
          # declare urllib3 module properties and methods
          user_agent = {'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
          http = urllib3.PoolManager(
          cert_reqs='CERT_REQUIRED', 
          ca_certs=certifi.where(),
          headers=user_agent)
          data = http.request('GET',url.strip(),preload_content=False)
          # 200 means succeeded in connecting to site
          if data.status == 200:
           if str(url.strip()) is not None:
            # check if file downloading already exists
            check_Fexists = os.path.isfile(str(url_split[-1]))
            if check_Fexists == True:
                 while True:
                   print("[!] {0} file already exists".format(str(url_split[-1])))
                   print("[>] please do you want to overwrite it? yes/no")
                   usr = str(input("[#] >>>: "))
                   # verify user input choice
                   if len(usr.strip()) > 0 and usr.lower().strip() == "yes":
                      print("[O] ok->Overwriting({0})".format(str(url_split[-1])))
                      start = True
                      break
                   elif len(usr.strip()) > 0 and usr.lower().strip() == "no":
                      print(" ")
                      print("[>] Or do you want to rename it? yes/no")
                      usr = str(input("[#] >>>: "))
                      if len(usr.strip()) > 0 and usr.lower().strip() == "yes":
                         # Generate random alphanumeric char
                         import uuid
                         ranNum = str(uuid.uuid4()).split("-")[1]
                         url_split[-1] = "{0}-{1}".format(ranNum,url_split[-1])
                         start = True
                         break
                      elif len(usr.strip()) > 0 and usr.lower().strip() == "no":
                         print("[S] ok->Skipped({0})".format(str(url_split[-1])))
                         start = False
                         break
                         
                      else:
                         print("[!] Don't be silly, choose from above list")
                         time.sleep(2)
                         print(" ")
                   else:
                      print("[!] Don't be silly, choose from above list")
                      time.sleep(2)
                      print(" ")
                 # procced if yes
                 if start == True:
                   if 'Content-Length' not in data.headers:
                      print("[:(] please wait...")
                      with open(str(url_split[-1]),typeO) as f:
                        f.write(data.data)
                        print("[+] downloaded->{0}".format(str(url_split[-1])))
                        f.close()
                   else:
                      try:
                       write_to_file(int(data.headers['Content-Length']),url_split[-1],typeO,data.stream(1024))
                      except (RuntimeError,KeyboardInterrupt,Exception):
                       print("[!] Somethhing happened...Exiting...")
                       sys.exit()
            else:
                if 'Content-Length' not in data.headers:
                   print("[:(] please wait...")
                   with open(str(url_split[-1]),typeO) as f:
                      f.write(data.data)
                      print("[+] downloaded->{0}".format(str(url_split[-1])))
                      f.close()
                else:
                   try:
                     write_to_file(int(data.headers['Content-Length']),url_split[-1],typeO,data.stream(1024))
                   except (RuntimeError,KeyboardInterrupt,Exception):
                     print("[!] Somethhing happened...Exiting...")
                     sys.exit()
          # 404 means..file not found
          elif data.status == 404:
           print("[!] DownloadError: File not found")
           sys.exit()
          # if any other http error occures, exit program
          else:
           print("[!] HTTPError: Couldn't fetch data,retry ")
           sys.exit()

if __name__ == '__main__':
   sys.exit()
