import os
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'

    id       = Column('id', Integer, autoincrement=True, primary_key=True)
    title    = Column("title", String(250))
    location = Column("location", String(250))
    salary   = Column("salary", Integer, autoincrement=False)
    currency = Column("currency", String(10))
    responsibilities = Column("responsibilities", String(2000))
    requirements = Column("requirements", String(2000))



first, last = os.path.split(os.path.abspath(__name__))
db_name = os.path.join(first, "learnFlask_2.db")

engine = create_engine(url=f"sqlite:///{db_name}")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
    


title = 'Backend developer'
location = 'San Francisco, USA'
salary = 120000
currency = '$'
responsibilities = """
As a backend developer, primary responsibilities include:
Designing, building, and maintaining the server-side of web applications.
Writing code that forms the backbone of a website or app.
Collaborating with front-end developers, product managers, principal architects, and website testers to build the structure of a website or mobile app.
Ensuring the back-end performs quickly and responsively to front-end user requests.
Troubleshooting and debugging issues, and communicating with project managers, stakeholders, and QA teams.
"""
requirements = """
project managers, stakeholders, and QA teams.
Technical Skills
Familiarity with various tools, frameworks, and languages, such as Python, Java, Ruby, and others.
Understanding of cross-platform functionality and compatibility.
Ability to write high-quality, clean, and maintainable code.
Knowledge of database systems and data storage solutions.
Experience with SASS and Less, and understanding of accessibility and server compliance.
Solid OOP and software design knowledge.
Soft Skills
Excellent collaboration and communication skills.
Analytical thinking and problem-solving abilities.
Ability to work with teams to prove design methods are viable.
Technical expertise and attention to detail.
Diversity and Inclusion
Employers should strive to create a diverse and inclusive workplace by:
Providing benefits offerings that support a diverse candidate pool, such as family leave, flexible schedules, and tuition reimbursement.
Communicating a commitment to diversity and inclusion through company culture and values.
Ensuring job descriptions and requirements are free from unintended biases.
"""

def add_employee(title, location, salary, currency, responsibilities, requirements):
    employee = Job(title=title, location=location, salary=salary, currency=currency, responsibilities=responsibilities, requirements=requirements)
    session.add(employee)
    session.commit()


def load_jobs_from_db():
	result = session.query(Job).all()

	jobs = []
	for employee in result:
		jobs.append(employee.__dict__)
	return jobs


def load_job_from_db(id):
    result = session.query(Job).filter_by(id=id).all()
    if result:
        return result[0].__dict__
    return None

# if __name__ == "__main__":
#       add_employee(title, location, salary, currency, responsibilities, requirements)