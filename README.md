# Contrary - Backend Data Engineering

<img src="https://img.shields.io/apm/l/vim-mode"/> <img src="https://img.shields.io/badge/Challenge-Contrary-green"/> <img src="https://img.shields.io/badge/DataEngineer-ETL-brightgreen"/>

This project has the objective to complete the test from Contrary - Backend Data Engineering.

---
# Getting Started
The project is gona be divided in 3 parts.

Part 1 - Ingestion

Part 2 - Analytics

Part 3 - Build an application

---
# Prerequisites
First you need to install the requirements of project.

    pip install requirements.txt
# Part 1 - Ingestion

In this part i created a script to delete table, create table and insert table for the both cases in the test. People and Companies. The database chosen is SQLite because is simple and complete for this test.
If change the quantity of data and respect the schema we don't gona have problem in the script.

Examples:

    python.exe ingest.py -u https://contrary-engineering-interview.s3.amazonaws.com/data/companies.csv

    python.exe ingest.py -u https://contrary-engineering-interview.s3.amazonaws.com/data/people.csv

Result:

    Insert data sucessful.

# Part 2 - Analytics

Here i focus on aswer the questions of test. All the SQL's is in the code.

Question 1

What is the average total funding of all of the companies that the person with ID = 92a52877-8d5d-41a6-950f-1b9c6574be7a has worked at?

    python.exe question_01.py -i 92a52877-8d5d-41a6-950f-1b9c6574be7a

    (108000000.0,)

Question 2

How many companies are in the companies table that no people in the people table have worked
for?

    python.exe question_02.py

    (8981,)


Question 3

What are the ten most popular companies that these 1,000 people have worked for?
    * This question is a litle trick, so we consider popular companies who has more HEADCOUNT.

    python.exe question_03.py

    ('Amazon', 880760)
    ('Accenture', 604596)
    ('IBM', 530041)
    ('Deloitte', 432835)
    ('US Army', 426913)
    ('Deloitte', 424347)
    ('Cognizant', 343834)
    ('JPMorgan Chase & Co.', 317375)
    ('Bank of America', 294471)
    ('Google', 292819)

Question 4 

Identify company founders in the people table. Then identify the companies that these people have
founded and list the top three largest companies by headcount, along with the name of that
company and the person ID of the founder(s)

    python.exe question_04.py

    ('bb0d8489-4360-4a94-bd3d-c079f75afc96', 'Dafiti', 2907)
    ('10e5dcc5-a642-4941-9701-9194101b27ed', '500 Startups', 1765)
    ('a292842c-475e-4b4f-9671-fb09536c472e', 'eBay for Business', 1336)

Question 5

For each person in the people table, identify their 2nd most recent job (if they only have 1 job,
please exclude them). What is the average duration in years of employment across everyone’s
2nd most recent job? Additionally, how many people have had more than 1 job?

    python.exe question_05.py

    (0.01, 814)


# Part 3 - Build an application

In this part i have to build an API to respond the suggests endpoints.

1)  /avg-funding-by-person/[person_id]
2)  /companies-by-person/[person_id]
3)  /investors-by-company/[company_linkedin_name]

        python.exe app.py

For test we just need to acess the localhost:5000/[endpoint] or any tool for API. I use Insomnia.

    /avg-funding-by-person/[person_id]
![image](https://user-images.githubusercontent.com/13987090/198903299-a40965f4-c7d9-4069-86cf-57b38eed5714.png)

    /companies-by-person/[person_id]
![image](https://user-images.githubusercontent.com/13987090/198903347-acd4b4da-a965-42ee-8149-d0c3c538e388.png)

    /investors-by-company/[company_linkedin_name]
![image](https://user-images.githubusercontent.com/13987090/198903401-122f8a1e-ada5-4e95-b88d-a9809b60b5bb.png)


# Next steps
For evolueted this project i consider create a docker-compose to build one orchestration tool like Airflow for automate and schedule the ingestion. 
# Licence
Licence MIT

# Author
Leonnardo Pereira - Backend Data Engineer