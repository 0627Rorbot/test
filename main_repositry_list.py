import os
from datetime import datetime, timedelta
from datetime import timedelta
from random import randint
from subprocess import Popen
from random import choice

# REPOSITORY = 'https://github.com/0627Rorbot/evidence-React-node-.git'
REPOSITORIES = [
    'https://github.com/0627Rorbot/evidence-React-node-.git',
    'https://github.com/0627Rorbot/rickandmorty.git',
    'https://github.com/0627Rorbot/Python-VR_First.git',
    'https://github.com/0627Rorbot/Json_to_image_Babric.js.git',
    'https://github.com/0627Rorbot/Face_recognize_Python_Html.git',
    'https://github.com/0627Rorbot/Face_recognize_PyQt5.git',
    'https://github.com/0627Rorbot/Lidar_3D_Visualization.git',
    'https://github.com/0627Rorbot/Face_Detection_And_Recognition.git',
    ]


MAX_COMMITS_PER_DAY = 2
WEEKEND_COMMIT = False
YEAR_FREQUENCY_PERCENT = 80

commit_messages = [
"Refactored database queries",
"Fixed typos in comments",
"Optimized performance of sorting algorithm",
"Added error handling for edge case",
"Implemented new UI design",
"Fixed security vulnerability",
"Updated dependencies to latest versions",
"Resolved merge conflicts",
"Added unit tests for authentication module",
"Documented API endpoints",
"Refactored CSS for improved styling",
"Added logging for debugging purposes",
"Fixed memory leak issue",
"Implemented feature toggle functionality",
"Updated configuration settings",
"Fixed broken links in documentation",
"Refactored error handling logic",
"Resolved compatibility issues with Python 3.9",
"Optimized database schema",
"Added support for internationalization",
"Fixed XSS vulnerability",
"Implemented password hashing for user authentication",
"Updated third-party libraries",
"Removed deprecated code",
"Fixed broken integration tests",
"Refactored code to adhere to PEP 8 guidelines",
"Implemented pagination for large datasets",
"Resolved performance bottleneck in database queries",
"Added support for file uploads",
"Fixed race condition in concurrent processes",
"Implemented email verification for user registration",
"Added support for OAuth authentication",
"Updated error messages for clarity",
"Refactored JavaScript code for better modularity",
"Fixed issue with CSRF protection",
"Implemented two-factor authentication",
"Added support for custom themes",
"Fixed bug in user session management",
"Implemented role-based access control",
"Refactored code for better code organization",
"Fixed issue with infinite loop in algorithm",
"Added support for web sockets",
"Implemented caching for improved performance",
"Updated documentation with examples",
"Fixed issue with timezone conversion",
"Refactored code for better readability",
"Implemented search functionality",
"Added support for geolocation",
"Fixed issue with database connection pooling",
"Implemented client-side validation for forms",
"Added support for dark mode",
"Fixed issue with infinite scroll",
"Implemented client-side pagination",
"Added support for webhooks",
"Fixed issue with file permissions",
"Implemented backup and restore functionality",
"Added support for Docker deployment",
"Fixed issue with data validation",
"Implemented audit logging",
"Added support for user avatars",
"Fixed issue with file downloads",
"Implemented RESTful API endpoints",
"Added support for error reporting",
"Fixed issue with memory",
]

def main():
    START_DATE = datetime(2021, 10, 1)

    for REPOSITORY in REPOSITORIES:        
        END_DATE = START_DATE + timedelta(days=150)

        directory = START_DATE.strftime('%Y-%m-%d') + '_' + END_DATE.strftime('%Y-%m-%d')

        if REPOSITORY is not None:
            start = REPOSITORY.rfind('/') + 1
            end = REPOSITORY.rfind('.')
            directory = REPOSITORY[start:end]
        os.mkdir(directory)
        # os.chdir(directory)
        run(['git', 'init'])

        n = 0
        day = START_DATE
        while day < END_DATE:
            day = START_DATE + timedelta(n)
            if (not WEEKEND_COMMIT or day.weekday() < 5) \
                    and randint(0, 100) < YEAR_FREQUENCY_PERCENT:
                for commit_time in (day + timedelta(minutes=m)
                    for m in range(contributions_per_day())):
                        contribute(commit_time)
            n = n + 1

        if REPOSITORY is not None:
            run(['git', 'remote', 'add', 'origin', REPOSITORY])
            run(['git', 'branch', '-M', 'main'])
            run(['git', 'push', '-u', 'origin', 'main'])

        print('\nRepository generation is completed successfully')

        START_DATE = END_DATE + timedelta(days=30)
        

def contribute(date):
    with open(os.path.join(os.getcwd(), 'helper.js'), 'a') as file:
        file.write(message(date) + '\n\n')
    commit = choice(commit_messages)
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', commit,
         '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])
    print(date.strftime('\t%Y-%m-%d %H:%M:%S'))


def run(commands):
    Popen(commands).wait()


def message(date):
    return date.strftime('Contribution: %Y-%m-%d %H:%M')

def contributions_per_day():
    return randint(1, MAX_COMMITS_PER_DAY)


if __name__ == "__main__":
    main()
