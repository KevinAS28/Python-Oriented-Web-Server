import re
Text = """

<html>
<head>
<title>Login to ForTHelL</title>
<link rel="stylesheet" href="loginnet.css">
</head>
<body>
<br>
<header>
<h1  class="title">Login to FortHell.net</h1>
<h4 class="subtitle">This page is for user of FortHell Firewall</h4> 
</header>

<article id="login">
<form method="post">
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<input  class="pass" type="password" placeholder="say the magic word " name   ="password"/><br><br>
<input class="submit" type  ="submit" formmethod="post" value="Login">
</form>
</article>
</body>
</html>"""
def Get_Var(data, *args):
 var = []
 for i in args:
  oke = re.search(r"""{}([\s]*)([\=])([\s]*)[\"]([\_\-\w|\d]*)[\"]""".format(i), data) #"{}".format("wow") re.search(pattern, text)
 return var
def Get_Input(data, *args):
 return data
if __name__=="__main__":
 print(Get_Var(Text, "name", "type"))



