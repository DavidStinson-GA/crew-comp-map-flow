from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class QAModulesCrew():
    """QAModulesCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def led_qa(self) -> Agent:
        return Agent(
            config=self.agents_config['led_qa'],
            llm = LLM(
                # model="openai/gpt-4.1"
                # model="perplexity/sonar-pro"
                model="openai/o4-mini",
                additional_drop_params=["stop"]
            )
        )

    @task
    def qa_modules(self) -> Task:
        print("QA'ing modules")
        return Task(
            name="QAModules",
            config=self.tasks_config['qa_modules'],
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the QAModulesCrew crew"""

        return Crew(
            name="QAModules Crew",
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
