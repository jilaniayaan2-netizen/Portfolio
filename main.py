from flask import Flask, render_template

# Create Flask App
app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html', project_list=projects)

# Projects 
projects = [
    {
        "id": 1,
        "title": "Ant Escape",
        "language": "C#/Unity",
        "description": "Ant Escape is a top down game, similar to a dungeon crawler. You play as Fred, an ant who got separated from his colony. To get back to his colony, he has to complete over 10 levels filled with enemies and even defeat a boss.",
        "image": "antEscape.png",
        "github": "https://github.com/jilaniayaan2-netizen/Ant-Escape",
        "itchio": "https://rainy-studios.itch.io/ant-escape"
    },
    {
        "id": 2,
        "title": "VR Guy's Bizarre Adventure",
        "language": "C#/Unity",
        "description": "VR Guy’s Bizarre Adventure is one of the first games I made, it's a side scrolling platform with 10 levels. You can do all the basic movements to pass levels but for some obstacles, you will need to use VR Guy’s special abilities; invisibility and a sword attack.",
        "image": "vrGuy.png",
        "github": "https://github.com/jilaniayaan2-netizen/VR-Guy-s-Bizarre-Adventure",
        "itchio": "https://rainy-studios.itch.io/vr-guys-bizzare-adventure"
    },
    {
        "id": 3,
        "title": "Journey of Bean",
        "language": "C#/Unity",
        "description": "Journey of Bean is my first 3D game. In the game you play as a bean and have to complete a 3D obstacle course without falling or dying. It includes various obstacles such as cannons, spinners, and platforms.",
        "image": "bean.png",
        "github": "https://github.com/jilaniayaan2-netizen/Journey-of-Bean",
        "itchio": "https://rainy-studios.itch.io/journy-of-bean"
    }
]

if __name__ == "__main__":
    app.run()
