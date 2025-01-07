import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Create an OpenAI model client.
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-2024-08-06",
    # api_key="YOUR_OPEN_AI_KEY"
)

# Create the scientist/engineer agent.
scientist_agent = AssistantAgent(
    "scientist",
    model_client=model_client,
    system_message=(
        "You are a meticulous scientist tasked with creating a clear, actionable plan for identifying and ranking citations related to CRISPR-Cas9 gene therapy. "
        "Once your plan is ready, clearly indicate 'PLAN COMPLETE' to signal that your part is done. Avoid any unnecessary follow-up after submitting the plan."
    ),
)

# Create the researcher agent.
researcher_agent = AssistantAgent(
    "researcher",
    model_client=model_client,
    system_message=(
        "You are a focused researcher responsible for executing the plan provided by the scientist agent. "
        "Locate, reference, and compile citations in a structured manner. "
        "Once you have completed the task, clearly indicate 'SEARCH COMPLETE' to signal your part is done and stop further interactions."
    ),
)

# Create the critic agent.
critic_agent = AssistantAgent(
    "critic",
    model_client=model_client,
    system_message=(
        "You are a strict reviewer validating the accuracy and relevance of citations provided by the researcher. "
        "Ensure all citations meet the highest scientific standards. Once validation is complete, clearly indicate 'VALIDATION COMPLETE'. "
        "Avoid unnecessary follow-up once the task is finalized."
    ),
)

# Define a termination condition that stops the task after the critic approves.
text_termination = TextMentionTermination("VALIDATION COMPLETE")

# Create a team with the scientist, researcher, and critic agents.
team = RoundRobinGroupChat([scientist_agent, researcher_agent, critic_agent], termination_condition=text_termination)

async def main():
    # Run the team and display output in the console.
    await Console(team.run_stream(
        task=(
            "Develop a comprehensive set of citations for a research paper exploring the impact of CRISPR-Cas9 on gene therapy. "
            "1) The scientist agent should create a ranked plan for finding citations, focusing on foundational papers, recent advancements, and clinical trial data. "
            "2) The researcher agent will execute the search and compile references from databases like PubMed, Scopus, and Web of Science. "
            "3) The critic agent will validate the citations for scientific rigor and alignment with the research goals. "
            "The final set of references should be organized by relevance and ready for inclusion in a publication. "
            "Each agent should signal task completion explicitly to terminate their part in the workflow."
        )
    ))

# Properly invoke the asyncio event loop.
if __name__ == "__main__":
    asyncio.run(main())
