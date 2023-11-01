import subprocess
from datetime import datetime, timedelta
from random import uniform

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
                    '-m', 'Commit number X'], 
                    cwd='./temp_folder', 
                    env=env_vars.update({'GIT_AUTHOR_DATE':'2010-10-25 11:15:11', 'GIT_COMMITTER_DATE':'2010-10-25 11:15:11'}))
    
    all_dates = generate_dates(year = year, commits = commits)

    
    # subprocess.run(["git", "remote", "add", "origin", "example.com/example_repo.git"])
    # subprocess.run(["git", "push", "-u", "origin", "master"])

def generate_dates(*, year:int, commits:list[int]) -> list[datetime]:
    start_date = datetime(year, 1, 1, 0, 0, 0)
    end_date = datetime(year, 12, 31, 23, 59, 59)
    delta = timedelta(days=1)

    current_date = start_date
    all_dates = []
    box_index = 0

    while current_date <= end_date:
        for _ in range(0, commits[box_index]):
            all_dates.append(current_date + timedelta(hours=uniform(5.0, 23.99)))
        current_date += delta
        box_index += 1
    
    print(type(current_date))

    return all_dates

if __name__=="__main__":
    main([], 2015)
    pass