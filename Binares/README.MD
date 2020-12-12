**Usage:**

***Linux:***
    
    uname -a
    chmod +x <filename>
    ./filename -h
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
    
