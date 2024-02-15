def d1(func):
    def d2(username,password):
        if username == "admin" and password == "admin":
           return "welcome",username 
        elif username == "support" and password == "support":
            return "welcome", username
        elif username == "sales" and password == "sales":
            return "welcome", username
        else:
            return "Invalid credentials"
        
    return d2
@d1
def d3(username,userpassword):
    return username, userpassword

d = d3("admin", "admin")
print(d)
    
     
             