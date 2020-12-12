# POCSRF
A PoC (Proof of Concept) generator for CSRF vulnerabilities. 

POCSRF is designed to easily generate CSRF PoC files from the command line. Simple enter the target application, the request method and the values to be sent in the request and POCSRF will generate the html code for you.

**How to Use:**
 
    ./POCSRF -h

     ______   ______     ______     ______     ______     ______  
    /\  == \ /\  __ \   /\  ___\   /\  ___\   /\  == \   /\  ___\ 
    \ \  _-/ \ \ \/\ \  \ \ \____  \ \___  \  \ \  __<   \ \  __\ 
     \ \_\    \ \_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\   
      \/_/     \/_____/   \/_____/   \/_____/   \/_/ /_/   \/_/   


    POCSRF.py

    Required: <URI> <METHOD> <NAME_1=VALUE_1,NAME_2=VALUE_2,...>

    Optional:  
    -e --encoding:  Encoding type (text/plain, www/application, etc) default : text/plain
    -a --auto:      Automatically submit the request when the page is loaded 
    -of --filename: Name of the output file (default : CSRF_PoC.html)
    -v --verbose:   Verbose mode

**Notes**

Minimum version of python required is Python3 (Python 3.8 used to develop), binaries are available for:
      
   - Binaries Coming Soon
   
https://www.python.org/
