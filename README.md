## Overview
**Citation AI** is a task-driven collaborative system that leverages multiple agents to automate the process of generating, curating, and validating research citations. This project is specifically tailored for research areas such as the impact of CRISPR-Cas9 on gene therapy. The system involves three specialized agents — Scientist, Researcher, and Critic — working together in a finite and clearly defined workflow.

---

## Features
- **Automated Literature Search Plan Creation**: The Scientist agent develops a comprehensive and actionable plan for citation retrieval.
- **Reference Compilation**: The Researcher agent executes the search plan, collects references, and organizes them.
- **Validation and Quality Assurance**: The Critic agent reviews and validates the citations for relevance, accuracy, and scientific rigor.
- **Finite Workflow**: A termination condition ensures the workflow concludes once the Critic agent completes its task, avoiding unnecessary interactions.
- **Extensibility**: Built using modular agent definitions, this system can be adapted for other research domains or workflows.

---

## Workflow Diagram
1. **Scientist Agent**: Develops the plan → Signals `PLAN COMPLETE`.
2. **Researcher Agent**: Executes the plan, collects references → Signals `SEARCH COMPLETE`.
3. **Critic Agent**: Validates references, ensures quality → Signals `VALIDATION COMPLETE`.

![image](https://github.com/user-attachments/assets/2e2747f0-c6e6-419a-88c8-838af8764458)

---

## Prerequisites
- Python 3.8 or higher
- OpenAI API key for GPT-based agents
- Required Python libraries:
  ```bash
  pip install asyncio autogen-agentchat autogen-core autogen-ext

## Usage
Set your OpenAI API Key: Replace "YOUR_OPEN_AI_KEY" in the OpenAIChatCompletionClient section with your API key.
The agents will communicate through a console interface.
Follow the interactions as the Scientist agent creates a plan, the Researcher compiles references, and the Critic validates them.

## Key Concepts
Assistant Agents: Modular agents with predefined roles and system prompts.
Termination Condition: Ensures a finite and streamlined workflow using the phrase VALIDATION COMPLETE.
Modular Design: Easily extendable to other domains or tasks.

## Future Enhancements
Integration with external databases (e.g., PubMed API).
Support for multiple research domains.
Enhanced UI for better interaction and visualization of the workflow.
