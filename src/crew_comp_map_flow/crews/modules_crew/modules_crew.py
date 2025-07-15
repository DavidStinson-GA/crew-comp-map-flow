from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ModulesCrew():
    """ModulesCrew crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def led(self) -> Agent:
        return Agent(
            config=self.agents_config['led'],
            verbose=True,
            llm = LLM(
                model="openai/gpt-4.1"
                # model="perplexity/sonar-pro"
            )
        )
    
    @agent
    def led_qa(self) -> Agent:
        return Agent(
            config=self.agents_config['led_qa'],
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
    def generate_modules(self) -> Task:
        return Task(
            name="Generate Modules",
            config=self.tasks_config['generate_modules'],
        )
    
    @task
    def qa_modules(self) -> Task:
        print("QA'ing modules")
        return Task(
            name="Modules QA",
            config=self.tasks_config['qa_modules'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ModulesCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            name="Modules Crew",
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
