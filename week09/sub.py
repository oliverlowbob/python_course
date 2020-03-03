import subprocess
import os

#subprocess.run("ls")
#subprocess.run(["mkdir", "clone_folder"])
#subprocess.run(["cd", "clone_folder"])
if os.path.isdir("clone_folder"):
    pass
else:
    os.mkdir("clone_folder")
os.chdir("clone_folder")

subprocess.run(["git", "clone", "https://github.com/Python-Elective-Spring-2020/introduction-to-python.git"])
#subprocess.run("ls")
