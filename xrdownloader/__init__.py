# Author: Solomon Narh (XploitsR Author)
# Copyright (c) 2019 XploitsR

"""
module -> Fast Files Downloader (^_^)

===========

=> XRDownloader is a module for faster downloading of files.
=> Very light weight,and highly efficient.
=> Aggressive security.
=> No loop holes.
=> Open source software.

======
Class:
======

   XRDownloader()

=========
Function:
=========

  download(url or /path/to/links-file)
  ==========================================


======
Usage:
======

     # import xrdownloader module
       import xrdownloader
       
     # call and assign it to a variable
       xr = xrdownloader.XRDownloader()

     # To download single file, just put in the url
 ==> Example: 
       res = xr.download("http://my.co/im.png")
       print(res)

     # To download multiple files, add [] and seperate the links with ,
 ==> Example: 
       res = xr.download(["http://my.co/im.png","http://u.com/i.pdf"])
       print(res)

     # You can also specify a file that contains your links
 ==> Example: 
       res = xr.download("myLinks.txt")
       print(res)
"""    

import re,time,sys
from .xrmain import main,pre,rawincount

__docformat__ = 'reStructuredText'

__version__ = '1.0.4'

__version_info__ = (1,0,1,2,3,4)

__version_details__ = 'progressbar has been added in version 1.0.4'

class XRDownloader:
   """defined class to call main() function"""
   def download(self,xrurl):
      """
      To download files, call this function
      
      Attributes
      ----------
      xrurl: your files url or path to your files url file
      ==> example: links.txt,anything.txt, ..etc
      """
      try:
        typeO = "wb"
        main(xrurl,typeO)
        pass
      except Exception as e:
        import urllib3
        if str(e).lower() == 'write() argument must be str, not bytes':
          typeO = "w"
          main(xrurl,typeO)
        elif urllib3.exceptions.NewConnectionError:
          print("[!] ConnectionError: invalid link or network error")
          sys.exit()
        else:
          print("[!] " + str(e))
          sys.exit()
      except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
      time.sleep(1)
      return "[^] Done (^_^)"
