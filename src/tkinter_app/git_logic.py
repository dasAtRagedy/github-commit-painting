import subprocess

def main(commits:list[int], year:int):
    global env_vars
    env_vars = {
        'GIT_AUTHOR_NAME': 'Dont Carmen',
        'GIT_AUTHOR_EMAIL': 'dont@care.man'
    }

    subprocess.run(["rm", "-rf", "./temp_folder"])
    subprocess.run(["mkdir", "temp_folder"])

    subprocess.run(["git", "init"], cwd='./temp_folder')
    subprocess.run(["touch", "README.md"], cwd='./temp_folder')
    subprocess.run(["git", "add", "."], cwd='./temp_folder')

    subprocess.run(['which', 'git'], cwd="./temp_folder")
    
    # commit, one of many
    subprocess.run(['git', 'commit', 
                    '--date="2010-10-25 11:15:11"',
                    '--allow-empty',
                    '-m', 'Commit number X'], cwd='./temp_folder', env=env_vars.update({'GIT_AUTHOR_DATE':'2010-10-25 11:15:11', 'GIT_COMMITTER_DATE':'2010-10-25 11:15:11'}))
    
    # subprocess.run(["git", "remote", "add", "origin", "example.com/example_repo.git"])
    # subprocess.run(["git", "push", "-u", "origin", "master"])

if __name__=="__main__":
    main([], 2015)