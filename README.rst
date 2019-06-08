
XRDownloader  
============
        
|PyPI-Versions| |PyPI-Status| |PyPI-Downloads|

XploitsR | XRDownloader is a module for faster downloading of files.  
It supports all HTTP protocols and also supports auto resume failed downloads.  
Has a progress-bar to show download statistics also.

**Installation:**

.. code:: sh

    pip install xrdownloader

**Latest development release on GitHub**

|GitHub-Status| |GitHub-Stars| |GitHub-Commits| |GitHub-Forks| |GitHub-Updated|

**Pull and install**

.. code:: sh
    
    pip install -e git+https://github.com/XploitsR/XRDownloader.git@master#egg=XRDownloader
    
**Usage:**

.. code:: python

    # import xrdownloader module
      import xrdownloader
    
    # XRDownloader returns the response from ongoing downloads
      xr = xrdownloader.XRDownloader()
     
    # To download single file, just put in the url
      download("your-file-url")

    # To download multiple files, add [] and seperate the links with ,
      download(["link-1","link-2","link-3","and so on.."])

    # You can also specify a file that contains your links
      download("your-file") # example: download("myLinks.txt")

**Examples:**

**single file download**

.. code:: python

    import xrdownloader
    xr = xrdownloader.XRDownloader()
    response = xr.download("https://xploitsr.tk/assets/csxp_img/logo/icon.png")
    print(response)

        
**multiple file download**
   
.. code:: python

    import xrdownloader
    xr = xrdownloader.XRDownloader()
    response = xr.download(["https://www.somesite.co/file-1.pdf","https://www.somesite.co/file-2.pdf"])
    print(response)


**file that contains links of files to download**

.. code:: python

    import xrdownloader
    xr = xrdownloader.XRDownloader()
    response = xr.download("xploitsr-links.txt")
    print(response)

``All links you typed since day one of using xrdownloader is saved in a file named:``
**allXlinks.txt**
``in every directory you used xrdownloader module``

**Screenshot:**

|Logo|

.. |Logo| image:: https://raw.githubusercontent.com/XploitsR/XRDownloader/master/sub-logo.png
   :width: 50%
   :alt: screenshot of xrdownloader 
   :target: https://pypi.org/project/xrdownloader
.. |GitHub-Status| image:: https://img.shields.io/github/tag/XploitsR/XRDownloader.svg?maxAge=86400&logo=github&logoColor=white
   :target: https://github.com/XploitsR/XRDownloader/releases
.. |GitHub-Forks| image:: https://img.shields.io/github/forks/XploitsR/XRDownloader.svg?logo=github&logoColor=white
   :target: https://github.com/XploitsR/XRDownloader/network
.. |GitHub-Stars| image:: https://img.shields.io/github/stars/XploitsR/XRDownloader.svg?logo=github&logoColor=white
   :target: https://github.com/XploitsR/XRDownloader/stargazers
.. |GitHub-Commits| image:: https://img.shields.io/github/commit-activity/m/XploitsR/XRDownloader.svg?logo=git&logoColor=white
   :target: https://github.com/XploitsR/XRDownloader/graphs/commit-activity
.. |GitHub-Updated| image:: https://img.shields.io/github/last-commit/XploitsR/XRDownloader/master.svg?logo=github&logoColor=white&label=pushed
   :target: https://github.com/XploitsR/XRDownloader/pulse
.. |PyPI-Status| image:: https://img.shields.io/pypi/v/xrdownloader.svg?logo=python&logoColor=white
   :target: https://pypi.org/project/xrdownloader
.. |PyPI-Downloads| image:: https://img.shields.io/pypi/dm/xrdownloader.svg?label=pypi%20downloads&logo=python&logoColor=white
   :target: https://pypi.org/project/xrdownloader
.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/xrdownloader.svg?logo=python&logoColor=white
   :target: https://pypi.org/project/xrdownloader
