import os
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
pname = input("Enter the project name: ")

os.system("mkdir " + pname)
os.chdir(dir_path + "\\" + pname)
with open("internal_install.bat", "w") as f:
	command = "py -m venv venv"
	command += " & venv\\Scripts\\activate"
	command += " & pip install flask"
	command += " & pip install flask-cors\n"
	f.write(command)
	
os.system("internal_install")
os.remove("internal_install.bat")

os.system("mkdir src")
os.chdir(dir_path + "\\" + pname + "\\src")
with open("main.py", "w") as f:
	command = "from flask import Flask, render_template\n"
	command += "\n"
	command += "app = Flask(__name__)\n"
	command += "\n"
	command += "@app.route('/')\n"
	command += "@app.route('/index')\n"
	command += "def index():\n"
	command += "	return render_template('index.html')\n"
	command += "\n"
	command += "\n"
	command += "\n"
	command += "if __name__ == '__main__':\n"
	command += "	app.run()"
	f.write(command)

os.system("mkdir templates")
os.chdir(dir_path + "\\" + pname + "\\src\\templates")
with open("index.html", "w") as f:
	html = []
	html.append("<html>")
	html.append("	<head>")
	html.append("		<title> Home Page </title>")
	html.append("	</head>")
	html.append("	<body>")
	html.append("		<p> Hello, World! from Home Page </p>")
	html.append("	</body>")
	html.append("</html>")
	f.write("\n".join(html))
	
os.chdir(dir_path + "\\" + pname)
	
with open("start_console.bat", "w") as f:
	command = "start venv\\Scripts\\activate\n"
	f.write(command)
	
with open("start_flask_server.bat", "w") as f:
	command = "venv\\Scripts\\activate & python src\\main.py"
	f.write(command)
	
with open("README.txt", "w") as f:
	text = []
	text.append('[Web Sistemi i Tehnologije]')
	text.append('')
	text.append('Skripta start_console.bat pokrece konzolu u novom virtual enviromentu za trenutni projekat')
	text.append('Skripta start_flask_server.bat pokrece main.py skriptu unutar src foldera')
	text.append('')
	text.append('Za sve dodatne informacije: mveniger@raf.rs')
	f.write("\n".join(text))
	
print("Install done")























