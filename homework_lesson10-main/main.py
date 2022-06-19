from flask import Flask, render_template
from show_smth import show_with_pre, get_u_by_skills
from utils import get_all_candidates, get_candidate


app = Flask(__name__)

li1 = get_all_candidates()

@app.route('/')
def index():
    return render_template('output1.html', li = li1)

@app.route('/candidates/<int:id>')
def user(id):
    li2 = get_candidate(id)
    li3 = show_with_pre(li2)
    res = str = f'<img src= "{li2[0]}">'
    res += li3
    return res

@app.route('/skills/<skill>')
def can_do(skill):
    li2 = get_u_by_skills(skill)
    return render_template('output2.html', li = li2)



if __name__ == "__main__":
    app.run(debug=True)
