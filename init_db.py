# File to reset database when needed
import sqlalchemy
import sqlalchemy.orm
import models
import os

db_url = os.getenv("DATABASE_URL")

# Add test internship
def add_test_internship(session):
    internship = models.Internships(
        netid = 'amkumar',
        title = 'Software Engineering Intern',
        location = 'Tampa, FL',
        description = 'Worked for data science team',
        type = 'Internship: Industry - Public Sector',
        length = 3,
        company = 'MITRE',
        company_type = 'STEM Research',
        salary = 25,
        difficulty = 4,
        enjoyment = 3,
        upvotes = 0,
        major = 'COS',
        certificates = 'SML, Finance',
        grade = 'jr'
    )
    session.add(internship)

# Add test interview
def add_test_interview(session):
    interview = models.Interviews(
        netid = 'amkumar',
        round = 1,
        final_round = False,
        duration = '2 hours',
        company = 'Amazon',
        question_description = 'Nothing',
        how_interview = 'Website',
        tips = 'Leetcode',
        difficulty = 2,
        enjoyment = 4,
        upvotes = 0,
        major = 'COS',
        certificates = 'SML, Finance',
        grade = 'jr'
    )
    session.add(interview)

# Add test companies
def add_test_companies(session):
    company = models.Companies(
        name = 'MITRE',
        num_interviews = 0,
        num_internships = 1,
        interview_difficulty = 0,
        interview_enjoyment = 0,
        internship_difficulty = 4,
        internship_enjoyment = 3
    )
    session.add(company)
    company = models.Companies(
        name = 'Amazon',
        num_interviews = 1,
        num_internships = 0,
        interview_difficulty = 2,
        interview_enjoyment = 4,
        internship_difficulty = 0,
        # Internship enjoyment rating
        internship_enjoyment = 0
    )
    session.add(company)

# Add test users
def add_test_users(session):
    user = models.Users(
                netid = "amkumar",
                major = '',
                certificates = '',
                grade = '',
                interview_upvotes = [],
                internship_upvotes = []
            )
    session.add(user)

def main():
    # Create engine and drop and recreate all tables
    engine = sqlalchemy.create_engine(db_url)
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)

    with sqlalchemy.orm.Session(engine) as session:
        # Add fake test data if needed
        add_test_internship(session)
        add_test_interview(session)
        add_test_companies(session)
        add_test_users(session)
        session.commit()
        
    engine.dispose()

if __name__ == '__main__':
    main()


