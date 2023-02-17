from flask import Flask, render_template
from project import Project

app = Flask(__name__)

projects = [
    {
        'id': 'todo',
        'title': 'To-Do App',
        'description': 'A basic To-Do App made with PyQt6.',
        'image_url': '/imgs/todo/img1.png',
        'image_url2': '/imgs/todo/img2.png',
        'features': [
            'Add tasks to list',
            'Remove tasks from list',
            'Scrollable list for when you have a lot of tasks',
            'You can save your list and safely save your list',
            'You can load a previously saved list'
        ],
        'download_url': 'https://github.com/Tolya05/PyQt-To-do/raw/main/main.exe',
        'github_url': 'https://github.com/Tolya05/PyQt-To-do'
    },
    {
        'id': 'usr',
        'title': 'A username generator',
        'description': 'A basic PyQt6 app.',
        'image_url': 'imgs/username_generator/img1.png',
        'image_url2': 'imgs/username_generator/img1.png',
        'features': [
            'Takes up to 3 words as input',
            'Generates a list of usernames based on the input',
            'Light and Dark Mode',
            'Copy usernames to clipboard'
        ],
        'download_url': 'https://github.com/Tolya05/PyQt-Username-Generator/raw/main/main.exe',
        'github_url': 'https://github.com/Tolya05/PyQt-Username-Generator'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
