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
    


title = 'Frontend developer'
location = 'Remote'
salary = 120000
currency = 'Rs'
responsibilities = """
Design and Implementation:
Translate design concepts into functional and visually appealing interfaces
Write clean, modular, and reusable JavaScript code
Implement responsive web design and mobile-first development
Ensure cross-browser compatibility and accessibility
Code Maintenance and Refactoring:
Maintain and refactor existing frontend codebases
Optimize code for performance and scalability
Ensure code adheres to company coding standards and best practices
Testing and Quality Assurance:
Write unit tests and UI tests for frontend components
Ensure code meets testing and debugging standards
Collaborate with QA team to identify and fix bugs
Deployment and Release Management:
Deploy frontend code to production environments
Manage frontend build processes and configuration files
Collaborate with backend developers and DevOps team for seamless deployment
Staying Up-to-Date with Industry Trends:
Participate in ongoing education and training to stay current with frontend development trends and technologies
Share knowledge and best practices with team members
Contribute to open-source projects or participate in online communities to stay engaged with the frontend development ecosystem
"""
requirements = """
Technical Skills:
Proficiency in HTML5, CSS3, and JavaScript (ES6+)
Familiarity with front-end build tools such as Webpack, Gulp, or Rollup
Knowledge of responsive web design and mobile-first development
Understanding of CSS preprocessors like Sass or Less
Experience with JavaScript libraries and frameworks like React, Angular, or Vue.js
Familiarity with state management libraries like Redux or MobX
Basic understanding of web performance optimization techniques
Design and UI/UX:
Understanding of design principles and human-computer interaction
Familiarity with design tools like Sketch, Figma, or Adobe XD
Ability to create visually appealing and user-friendly interfaces
Knowledge of accessibility guidelines (WCAG 2.1) and implementation
Version Control:
Proficiency with Git and GitHub (or other version control systems)
Ability to manage codebase, branches, and merges
Understanding of Git workflows and collaboration
Testing and Debugging:
Familiarity with unit testing frameworks like Jest or Mocha
Understanding of UI testing and integration testing
Ability to debug code using browser dev tools and console logs
Communication and Collaboration:
Strong written and verbal communication skills
Ability to work collaboratively with designers, backend developers, and product managers
Understanding of agile development methodologies and Scrum principles
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

# if __name__ == "__main__":
    #   add_employee(title, location, salary, currency, responsibilities, requirements)