from flask import Flask, jsonify, request
from question_01 import question_01
from companies_by_person import companies_by_person
from investors_by_company import investors_by_company
from config import utils

app = Flask(__name__)


@app.route('/avg-funding-by-person/<string:person_id>', methods=['GET'])
def avg_funding_by_person(person_id):
    person = question_01(person_id, utils.db_raw_dir)

    if person[0] == None:
        return [0]
    else:
        return jsonify(person)

@app.route('/companies-by-person/<string:person_id>', methods=['GET'])
def companies_person(person_id):
    companies = companies_by_person(person_id, utils.db_raw_dir)

    if companies[0] == None:
        return [0]
    else:
        return jsonify(companies)

@app.route('/investors-by-company/<string:company_linkedin_name>', methods=['GET'])
def investors_company(company_linkedin_name):
    investors = investors_by_company(company_linkedin_name, utils.db_raw_dir)

    if investors[0] == None:
        return [0]
    else:
        return jsonify(investors)


app.run(port=5000, host="localhost", debug=True)
