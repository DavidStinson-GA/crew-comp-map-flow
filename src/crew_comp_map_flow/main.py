#!/usr/bin/env python
from random import randint
import json

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from crew_comp_map_flow.crews.competencies_crew.competencies_crew import CompetenciesCrew
from crew_comp_map_flow.crews.modules_crew.modules_crew import ModulesCrew
from crew_comp_map_flow.crews.qa_modules_crew.qa_modules_crew import QAModulesCrew
from crew_comp_map_flow.crews.learning_objectives_crew.learning_objectives_crew import LearningObjectivesCrew

from crew_comp_map_flow.data import documentation

class CompMapState(BaseModel):
    ### UX for Engineers for M&T Bank ###
    competencies: list[str] = []
    product_title: str = 'UX for Engineers'
    client_name: str ='M&T Bank'
    course_delivery_method: str = 'Instructor-led'
    course_delivery_modality: str = 'remote'
    course_duration_m: int = 1800
    course_description: str = 'This course equips developers with practical UX skills through hands-on exercises with real-world applications. With a strong focus on collaboration, participants will improve communication with UX teams and gain actionable strategies they can use right away.'
    course_business_outcomes: list[str] =[
        # 'Expand the mindset and steps in UX process to entire tech team include low and high fidelity technical design skills and UX research methodologies.',
        # 'Demonstrate ability to develop a low-fidelity design',
        'Demonstrate ability to develop a high-fidelity design',
        'Equip tech team with research methodologies',
        'Making developers more self-reliant', 
        'Speeding up design and development collaboration and process.'
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
        # 'Currency Design System',
        'Primer Design System',
    ]

    doc_voice: str = documentation["voice"]
    doc_writing_learning_objectives: str = documentation["writing_learning_objectives"]

# class CompMapState(BaseModel):
#     ### Gen AI Champions Workshop for TAG Heuer ###
#     competencies: list[str] = []
#     product_title: str = 'Gen AI Champions Workshop'
#     client_name: str ='TAG Heuer'
#     course_delivery_method: str = 'Instructor-led'
#     course_delivery_modality: str = 'remote'
#     course_duration_m: int = 420
#     course_description: str = """This intensive one-day programme develops internal AI Champions who will support Gen AI adoption across TAG Heuer's global operations. Participants will master advanced MaIA capabilities, identify high-impact use cases, and develop advocacy skills to drive Gen AI adoption across the nine different job families:

#         - General Management
#         - Tech: Connected Watch
#         - Tech: IS&T
#         - HR
#         - Operations
#         - Commercial
#         - Finance & Legal
#         - Product
#         - Marketing
#         """
#     course_business_outcomes: list[str] =[
#         'Confidently identify high-value Gen AI opportunities',
#         'Support workflow transformations with MaIA',
#         'Identify use cases for MaIA with cross-functional alignment',
#         'Coach peers through AI adoption challenges'
#     ]
#     client_priorities: list[str] = [
#         'Master advanced prompt engineering: system instructions, memory settings, structured prompt frameworks.',
#         'Coordinate across multiple Gen AI tools and models  (e.g., summarizing, forecasting, visual prototyping).',
#         'Lead Gen AI-focused workshops for peers: teach prompting, manage change, and address ethical concerns.',
#         'Explore the use of  effective prompts, visuals, and data templates for job family enablement.'
#     ]
#     primary_persona_job_role: str = 'Software Engineer'
#     learner_persona_description: str = 'TAG Heuer employees who are interested in learning about Gen AI, MaIA, and how to use them ethically, securely, and effectively to improve their workflows.'
#     learner_persona_attributes_and_background: list[str] = [
#         'Strong foundation in JavaScript, React, and Node.js.'
#         'Experience building web applications.'
#         'Familiar with modern web development practices and tools.'
#         'Strong interest in learning new technologies and approaches.'
#     ]
#     learner_persona_existing_knowledge: list[str] = [
#         'Familiar with the TAG Heuer brand and its values.'
#     ]
#     course_learning_outcomes: list[str] = [
#         'Explore Gen AI technologies that can drive innovation across business operations at TAG Heuer.',
#         "Identify high-impact Gen AI use cases tailored to TAG Heuer's diverse functions.",
#         'Map functional pain points to practical MaIA-powered applications that improve decision-making and efficiency.',
#         'Exam how different prompt structures and MaIA model types influence the quality, relevance, and speed of Gen AI outputs.',
#         'Develop and iterate prompting strategies like role-based context and tone specifications to optimize outputs for TAG Heuer workflows.',
#         'Apply advanced techniques like chain-of-thought prompting and formatting to create polished, on-brand digital artifacts.',
#         'Use MaIA to analyze long-form documents quickly and extract relevant summaries, risks, or action points across job functions.',
#         'Apply explainability features in MaIA to trace Gen AI responses back to original document sources and assess for tone, bias, and hallucinations.',
#         'Identify potential project scopes by job family, that clearly define objectives, outputs, guardrails, and success criteria using MaIA as a co-pilot.',
#         'Identify and address Gen AI risks related to hallucination, data integrity, regulatory compliance, brand consistency and environmental impact through structured prompts and checklists.',
#         'Apply practical techniques to accelerate Gen AI adoption and build internal momentum through MaIA use cases and workshops.',
#         'Coach colleagues through potential change resistance or digital discomfort using accessible prompt-based tools.'
#     ]
#     course_software_and_tools: list[str] = [
#         'MaIA',
#     ]

#     doc_voice: str = documentation["voice"]
#     doc_writing_learning_objectives: str = documentation["writing_learning_objectives"]

# class CompMapState(BaseModel):
#     ### Software Engineering Bootcamp for General Assembly ###
#     competencies: list[str] = []
#     product_title: str = 'Software Engineering Bootcamp'
#     client_name: str = ''
#     course_delivery_method: str = 'Instructor-led'
#     course_delivery_modality: str = 'remote'
#     course_duration_m: int = 25200
#     course_description: str = "Reskill non-technical talent into full-stack web engineering roles to immediately contribute to software projects. Participants will gain in-demand fundamental programming skills, computer science knowledge, and experience with multiple languages."
#     course_business_outcomes: list[str] =[
#         'Junior Engineer Development: Equip junior engineers with essential skills for efficient project contribution.',
#         'Non-Technical to Technical Transition: Transform non-technical staff into competent, job-ready software engineers.',
#         'Real-World Problem Solving: Empower teams to solve actual engineering challenges through hands-on projects.'
#     ]
#     client_priorities: list[str] = [
#         'Learn the fundamentals of front-end development to create interactive web experiences. Gain practical skills in key programming concepts and insights into the daily work life of a professional engineer.',
#         'Learn to build full-stack web applications, deepening your knowledge of client-facing and server-side development. Create complex applications by utilizing libraries and frameworks.,
#         'Learn to use React, a highly sought-after library in contemporary software engineering. By creating a full-stack MERN application, you'll concentrate on utilizing React to craft interactive user interfaces.',
#         'Rapidly learn a second language and gain experience working with new frameworks and database technologies. Develop a deeper understanding of software engineering fundamentals'
#     ]
#     primary_persona_job_role: str = 'Aspiring Software Engineer'
#     learner_persona_description: str = 'Students who are interested in entering the tech industry and want to learn the fundamentals of software engineering through web development and gain practical skills in key programming concepts.'
#     learner_persona_attributes_and_background: list[str] = [
#         'Generally interested in learning about software engineering and web development, but have no prior experience in the field.'
#         'No prior experience in software engineering or web development.'
#         'No prior experience in programming.'
#     ]
#     learner_persona_existing_knowledge: list[str] = [
#         'Able to use a computer, navigate the internet, and download and install software.'
#     ]
#     course_learning_outcomes: list[str] = [
#         'Create a front-end game with distinct win or loss conditions, using JavaScript, HTML, and CSS. Learn fundamental project design, planning, and management skills, including creating wireframes, and developing user stories. Deploy the project to the internet.',
#         "Plan and create a full-stack Node.js/Express application that implements authentication and authorization. The application will interact with a MongoDB database to create, read, update, and delete data related to a user. The application will be deployed to the internet. As part of planning for this project, you will build an ERD, write user stories, and design wireframes.",
#         'Develop a full-stack web application using React for the front-end and Node.js/Express for the backend and implements authentication and authorization. This project combines front-end interactivity with server-side functionality in the MERN stack. The back-end application will interact with a MongoDB database to create, read, update, and delete data related to a user. The application will be deployed to the internet. As part of planning for this project, you will build an ERD, write user stories, and design wireframes.',
#         'Develop a full-stack application using an additional programming language and framework. The application will be deployed to the internet. As part of planning for this project, you will build an ERD, write user stories, and design wireframes.',
#     ]
#     course_software_and_tools: list[str] = [
#         'Visual Studio Code',
#         'Git',
#         'GitHub',
#         'Python',
#         'Nmap',
#         'VirtualBox',
#         'Docker',
#         'Node.js',
#         'Express',
#         'React',
#         'MongoDB',
#         'Mongoose',
#         'PostgreSQL',
#     ]

#     doc_voice: str = documentation["voice"]
#     doc_writing_learning_objectives: str = documentation["writing_learning_objectives"]

class CompetencyFlow(Flow[CompMapState]):

    @start()
    def generate_comp_map(self):
        print("Starting to generate competencies")

    @listen(generate_comp_map)
    async def generate_competencies(self):
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
        modules_output = json.loads(result.raw)
        all_modules = []
        for competency in modules_output["competencies"]:
            for module in competency["modules"]:
                all_modules.append({
                    **module,
                    "competency": competency["competency"]
                })

        print(f"Total modules: {len(all_modules)}")

        module_id_to_competency = {
            module["id"]: module["competency"]
            for module in all_modules
        }


        print("QA'ing modules")
        qa_inputs = [
            {
                "module": module,
                "competency": module["competency"],
                **self.state.model_dump()
            }
            for module in all_modules
        ]

        qa_results = await QAModulesCrew().crew().kickoff_for_each_async(qa_inputs)

        qa_modules = []
        for res in qa_results:
            parsed = json.loads(res.raw)
            if "competency" not in parsed:
                parsed["competency"] = module_id_to_competency.get(parsed["id"])
            qa_modules.append(parsed)

        print("Generating learning objectives")
        lo_inputs = [
            {
                "module": module,
                "competency": module["competency"],
                **self.state.model_dump()
            }
            for module in qa_modules
        ]

        lo_results = await LearningObjectivesCrew().crew().kickoff_for_each_async(lo_inputs)

        modules_with_lo = []
        for res in lo_results:
            parsed = json.loads(res.raw)
            if "competency" not in parsed:
                parsed["competency"] = module_id_to_competency.get(parsed["id"])
            modules_with_lo.append(parsed)


        modules_by_comp = {}
        for m in modules_with_lo:
            comp = m["competency"]
            modules_by_comp.setdefault(comp, []).append(m)

        new_competencies = []
        for comp, modules in modules_by_comp.items():
            new_competencies.append({
                "competency": comp,
                "modules": modules
            })

        self.state.competencies = new_competencies



def kickoff():
    competency_flow = CompetencyFlow()
    competency_flow.kickoff()


def plot():
    competency_flow = CompetencyFlow()
    competency_flow.plot()


if __name__ == "__main__":
    kickoff()
