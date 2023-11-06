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
    
    all_dates = generate_dates(year = year, commits = commits)

    subprocess.run(["git", "init"], cwd='./temp_folder')
    subprocess.run(["touch", "README.md"], cwd='./temp_folder')
    subprocess.run(["git", "add", "."], cwd='./temp_folder')

    subprocess.run(['which', 'git'], cwd="./temp_folder")
    
    create_commits(all_dates=all_dates, env_vars=env_vars, cwd="./temp_folder")
    
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

    return all_dates

def create_commits(all_dates:list[datetime], *, env_vars:dict[str, str], cwd:str):
    all_dates.sort()
    for dt in all_dates:
        subprocess.run(['git', 'commit',
                    f'--date="{dt.strftime("%Y-%m-%d %H:%M:%S")}"',
                    '--allow-empty',
                    '-m', 'Commit number X'],
                    cwd=cwd,
                    env=env_vars.update({'GIT_AUTHOR_DATE':dt.strftime('%Y-%m-%d %H:%M:%S'), 'GIT_COMMITTER_DATE':dt.strftime('%Y-%m-%d %H:%M:%S')}))

if __name__=="__main__":
    main([], 2015)
    pass