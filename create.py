import sys
import os
from github import Github

project_name = str(sys.argv[1])
path = 'C:\\Users\\velin\\Desktop\\Projects\\Python'
user = Github('velinskiy@gmail.com', 'MblwEY7%c^oE4#X@@').get_user()
    
    # cd C:\\Users\\velin\\Desktop\\Projects\\Python
    # python create.py create one

def create():
    print('navigating to the path...'.capitalize())
    os.chdir(path)
    
    print('creating new folder...'.capitalize())
    os.mkdir(str(project_name))
    
    new_path = str('{}\\{}').format(path, project_name)
    os.chdir(new_path)
    print('navigating to the local folder... '.capitalize(), new_path)

    cmd = 'git init'
    os.system(cmd)

    repo = user.create_repo(project_name)
    print('creating new repo... '.capitalize(), project_name)
    
    repo_url = 'https://github.com/VELINSKIY/{}.git'.format(project_name)
    print('git remote add '.capitalize(), repo_url)
    cmd = f'git remote add origin {repo_url}'
    os.system(cmd)
    
    new_path = str('{}\\{}').format(path, project_name)
    os.chdir(new_path)
    print('navigating to the local repo... '.capitalize(), new_path)
    
    project = project_name + '.py'
    
    with open(project, 'w'):
        print(f'opening {project} VS Code...'.capitalize())
        cmd = 'code .'
        os.system(cmd)
    
    print('adding files...'.capitalize())
    cmd = f'git add \'{project}\''
    os.system(cmd)
    
    print(f'Succesfully created repository \'{project_name}\'')

    
if __name__ == "__main__":
    create()