import os

#[folder name, code, title_code, detail code
http_code = [
    ["Code 100", "100", "Informational Responses", "Continue"],
    ["Code 101", "101", "Informational Responses", "Switching Protocols"],
    ["Code 102", "102", "Informational Responses", "Processing"],
    ["Code 103", "103", "Informational Responses", "Early_Hints"],   
    
    ["Code 200", "200", "Success", "OK"],
    ["Code 201", "201", "Success", "Created"],
    ["Code 202", "202", "Success", "Accepted"],
    ["Code 203", "203", "Success", "Non-Authoritative Information"],
    ["Code 204", "204", "Success", "No Content"],
    ["Code 205", "205", "Success", "Reset Content"],
    ["Code 206", "206", "Success", "Partial Content"],
    ["Code 207", "207", "Success", "Multi-Status"],
    ["Code 208", "208", "Success", "Already Reported"],
    ["Code 226", "226", "Success", "IM Used"],
    
    
    ["Code 300", "300", "Redirection", "Multiple Choices"],
    ["Code 301", "301", "Redirection", "Moved Permanently"],
    ["Code 302", "302", "Redirection", "Found"],
    ["Code 303", "303", "Redirection", "See Other"],
    ["Code 304", "304", "Redirection", "Not Modified"],
    ["Code 305", "305", "Redirection", "Use Proxy"],
    ["Code 306", "306", "Redirection", "Switching Proxy"],
    ["Code 307", "307", "Redirection", "Temporary Redirect"],
    ["Code 308", "308", "Redirection", "Permanent Redirect"],
    
    ["Code 400", "400", "Client Error", "Bad Request"],
    ["Code 401", "401", "Client Error", "Unauthorized"],
    ["Code 402", "402", "Client Error", "Payment Required"],
    ["Code 403", "403", "Client Error", "Forbidden"],
    ["Code 404", "404", "Client Error", "Not Found"],
    ["Code 405", "405", "Client Error", "Method Not Allowed"],
    ["Code 406", "406", "Client Error", "Not Acceptable"],
    ["Code 407", "407", "Client Error", "Proxy Authentication Required"],
    ["Code 408", "408", "Client Error", "Request Timeout"],
    ["Code 409", "409", "Client Error", "Conflict"],
    ["Code 410", "410", "Client Error", "Gone"],
    ["Code 411", "411", "Client Error", "Length Required"],
    ["Code 412", "412", "Client Error", "Precondition Failed"],
    ["Code 413", "413", "Client Error", "Payload Too Large"],
    ["Code 414", "414", "Client Error", "URI Too Long"],
    ["Code 415", "415", "Client Error", "Unsupported Media Type"],
    ["Code 416", "416", "Client Error", "Range Not Satisfied"],
    ["Code 417", "417", "Client Error", "Exception Failed"],
    ["Code 418", "418", "Client Error", "I'm a teapot"],
    ["Code 421", "421", "Client Error", "Misdirected Request"],
    ["Code 422", "422", "Client Error", "Unprocessable Entity"],
    ["Code 423", "423", "Client Error", "Locked"],
    ["Code 424", "424", "Client Error", "Failed Depency"],
    ["Code 426", "426", "Client Error", "Upgrade Required"],
    ["Code 428", "428", "Client Error", "Precondition Required"],
    ["Code 429", "429", "Client Error", "Too Many Requests"],
    ["Code 431", "431", "Client Error", "Request Header Fields Too Lage"],
    ["Code 451", "451", "Client Error", "Unavailable For Legal Reasons"],
    
    ["Code 500", "500", "Server Error", "Internal Server Errors"],
    ["Code 501", "501", "Server Error", "Not Implentable"],
    ["Code 502", "502", "Server Error", "Bad Gateway"],
    ["Code 503", "503", "Server Error", "Service Unavailble"],
    ["Code 504", "504", "Server Error", "Gateway Timeout"],
    ["Code 505", "505", "Server Error", "HTTP Version Not Supported"],
    ["Code 506", "506", "Server Error", "Variant Also Negotiates"],
    ["Code 507", "507", "Server Error", "Insufficient Storage"],
    ["Code 508", "508", "Server Error", "Loop Detected"],
    ["Code 509", "509", "Server Error", "Not Extended"],
    ["Code 510", "510", "Server Error", ""],
    ["Code 511", "511", "Server Error", "Network  Authentication Required"],
    ["Code 512", "512", "Server Error", ""]
 
] 
default_page = "index.html"

for i in http_code:
    os.mkdir(i[0])
    with open(default_page, "r") as baca:
        with open(os.path.join(i[0], default_page), "w+") as tulis:
            tulis.write(baca.read().format(w=i[1], x=i[1], y=i[2], z=i[3]))
            
    
