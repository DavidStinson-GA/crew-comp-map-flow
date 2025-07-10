#!/usr/bin/env python
from random import randint
import json

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from crew_comp_map_flow.crews.competencies_crew.competencies_crew import CompetenciesCrew
from crew_comp_map_flow.crews.modules_crew.modules_crew import ModulesCrew

class CompMapState(BaseModel):
    competencies: list[str] = []
    product_title: str = 'UX for Engineers'
    client_name: str ='M&T Bank'
    course_delivery_method: str = 'Instructor-led'
    course_delivery_modality: str = 'remote'
    course_duration_m: int = 1800
    course_description: str = 'This course equips developers with practical UX skills through hands-on exercises with real-world applications. With a strong focus on collaboration, participants will improve communication with UX teams and gain actionable strategies they can use right away.'
    course_business_outcomes: list[str] =[
        'Expand the mindset and steps in UX process to entire tech team include low and high fidelity technical design skills and UX research methodologies.',
        'Making developers more self-reliant; speeding up design and development collaboration and process.'
    ]
    client_priorities: list[str] = [
        'The course should provide an understanding of baseline research techniques, methodologies and best practices for better cross-discipline collaboration.',
        'Engineers should be able to use tools like Miro to wireframe and communicate ideas and collaborate with the broader team.',
        'Understanding the end-to-end design process will help engineers incorporate UX concepts and approaches into in their decision making and workflow.',
        'Exposure and practice with collaborative tools like the Currency Design System can improve efficiency, velocity and reinforce cohesive product design.'
    ]
    primary_persona_job_role: str = 'Software Engineer'
    learner_persona_description: str = 'A software engineer with 3+ years of experience in software development, specializing in building web applications using modern JavaScript frameworks and libraries.'
    learner_persona_attributes_and_background: list[str] = [
        'Strong foundation in JavaScript, React, and Node.js.'
        'Experience building web applications.'
        'Familiar with modern web development practices and tools.'
        'Strong interest in learning new technologies and approaches.'
    ]
    learner_persona_existing_knowledge: list[str] = [
        'Familiar with implementing UI designs using HTML and CSS.'
    ]
    course_learning_outcomes: list[str] = [
        'Create polished, professional, and complete designs; and articulate design decisions made to peers and other UX professionals.',
        'Utilize foundational visual design techniques to enhance the overall design of digital products.'
        'Design product interactions with easy-to-use navigation that are logically structured using information architecture methodologies.',
        'Collaborate with a team of fellow designers to solve real-world design challenges using advanced technical design skills.',
        'Evaluate business requirements, metrics, key stakeholders, and technical constraints; and employ product management techniques to design products.'
    ]
    course_software_and_tools: list[str] = [
        'Visual Studio Code',
        'Miro',
        'Currency Design System',
    ]

class CompetencyFlow(Flow[CompMapState]):

    @start()
    def generate_comp_map(self):
        print("Starting to generate competencies")

    @listen(generate_comp_map)
    def generate_competencies(self):
        print("Generating competencies")
        result = (
            CompetenciesCrew()
            .crew()
            .kickoff(inputs=self.state.model_dump())
        )

        print("Competencies generated", result.raw)

        self.state.competencies = json.loads(result.raw)["competencies"]

        print("Generating modules")
        result = (
            ModulesCrew()
            .crew()
            .kickoff(inputs=self.state.model_dump())
        )
        print("Modules generated", result.raw)

def kickoff():
    competency_flow = CompetencyFlow()
    competency_flow.kickoff()


def plot():
    competency_flow = CompetencyFlow()
    competency_flow.plot()


if __name__ == "__main__":
    kickoff()
