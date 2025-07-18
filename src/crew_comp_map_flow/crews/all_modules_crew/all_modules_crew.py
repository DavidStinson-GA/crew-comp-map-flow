from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AllModulesCrew():
    """AllModulesCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
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

    @agent
    def led(self) -> Agent:
        return Agent(
            config=self.agents_config['led_los'],
            verbose=True,
            llm = LLM(
                # model="openai/gpt-4.1"
                # model="perplexity/sonar-pro"
                model="openai/o4-mini",
                additional_drop_params=["stop"]
            )
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def qa_modules(self) -> Task:
        print("QA'ing modules")
        return Task(
            name="Modules QA",
            config=self.tasks_config['qa_modules'],
        )
    
    @task
    def generate_learning_objectives(self) -> Task:
        return Task(
            name="Generate Learning Objectives",
            config=self.tasks_config['generate_learning_objectives'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AllModulesCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            name="All Modules Crew",
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
