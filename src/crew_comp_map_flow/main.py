#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from crew_comp_map_flow.crews.competencies_crew.competencies_crew import CompetenciesCrew


class CompMapState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


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
            .kickoff(inputs={})
        )

        print("Poem generated", result.raw)
        self.state.poem = result.raw

def kickoff():
    competency_flow = CompetencyFlow()
    competency_flow.kickoff()


def plot():
    competency_flow = CompetencyFlow()
    competency_flow.plot()


if __name__ == "__main__":
    kickoff()
