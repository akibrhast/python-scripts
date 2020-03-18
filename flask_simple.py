import os
import virtualenv
import sys


def main(argv):
    PROJECT_NAME=''
    command=''
    try:
        command=argv[0]
        PROJECT_NAME = argv[1]
        create_project(PROJECT_NAME)
    except IndexError as e:
        print(e)
        print("USAGE: flask_simple.py -n Project_Name")

def create_project(PROJECT_NAME):
    try:
        os.makedirs(PROJECT_NAME)
        os.chdir(PROJECT_NAME)
        os.makedirs("./templates") #create templates directory
        os.makedirs("./static/css") #create static/css directory
        os.makedirs("./static/js") #create static/js directory
        create_virtualenv(PROJECT_NAME)
    except FileExistsError:
        print("Directory already exists")
    

def create_virtualenv(PROJECT_NAME):
    activate_script = os.path.join("env", "bin", "activate_this.py")
    os.system("virtualenv env")
    exec(open("env/Scripts/activate_this.py").read(), {'__file__': "env/Scripts/activate_this.py"})
    os.system("pip install flask requests")

    get_files_from_github()

def get_files_from_github():
    import requests
    baseHtmlFile = requests.get("https://raw.githubusercontent.com/akibrhast/flask_base_template/master/base.html").text
    baseRoutesFile = requests.get("https://raw.githubusercontent.com/akibrhast/flask_base_template/master/routes.py").text
    with open("templates/base.html","w") as file:
        file.write(baseHtmlFile)
    with open("routes.py","w") as file:
        file.write(baseRoutesFile)
    with open("static/css/base.css","w") as file:
        file.write('')
    with open("static/css/bootstrap_override.css","w") as file:
        file.write('')

    #get base.html from github
    #create base.css under static/css
    #create bootsrap_override.css under static/css


if __name__ == "__main__":
   main(sys.argv[1:])