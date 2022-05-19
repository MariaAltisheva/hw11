from flask import Flask, render_template
import json
from utils11 import *
app = Flask(__name__)

@app.route("/")
def page_all_candidates(): #выводим стартовую страницу со списком кандидатов
    dictionary_candidates = get_data_from_json()
    return render_template('list.html', items=dictionary_candidates)

@app.route('/candidate/<int:x>') #выводим кандидата по номеру
def page_candidate(x):
    all_canddates = get_data_from_json()
    for i in range(len(all_canddates)): #перебираем список c данными словаря
        if i == (x - 1):
            name1 = all_canddates[i]['name']
            position1 = all_canddates[i]['position']
            skills1 = all_canddates[i]['skills']
            picture1 = all_canddates[i]['picture']
    candidate = render_template('single11.html', name=name1, position=position1, skills=skills1, picture=picture1)
    return candidate

@app.route('/search/<candidate_name>') #выводим кандидатов по скиллам
def page_name_candidate(candidate_name):
    name1 = get_candidates_by_name(candidate_name)[0]
    count1 = len(get_candidates_by_name(candidate_name))
    id = load_candidates_from_json().index(name1) + 1
    candidate = render_template('search11.html', count=count1, name=name1, x=id)
    return candidate

@app.route('/skill/<skill_name>') #выводим кандидатов по скиллам
def page_skill_candidate(skill_name):
    candidate_list = get_candidates_by_skill(skill_name)
    count = len(candidate_list)
    candidate = render_template('skill.html', count=count, items=candidate_list)
    return candidate


app.run(host='127.0.0.1', port=800, debug=True)
