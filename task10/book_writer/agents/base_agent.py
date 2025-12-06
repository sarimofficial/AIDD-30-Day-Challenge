class BaseAgent:
    """
    A base class for all agents in the system.
    """

    def __init__(self, name: str, description: str):
        """
        Initializes the BaseAgent.

        Args:
            name (str): The name of the agent.
            description (str): A brief description of the agent's purpose.
        """
        self.name = name
        self.description = description

    def execute_task(self, task: str, context: dict = None) -> str:
        """
        Executes a given task. This method is intended to be overridden by subclasses.

        Args:
            task (str): The task to be executed.
            context (dict, optional): Additional context for the task. Defaults to None.

        Returns:
            str: The result of the task execution.
        """
        print(f"[{self.name}] received task: {task}")
        # In a real implementation, this would involve LLM calls or other logic.
        return f"[{self.name}] has completed the task: {task}"

    def load_skill(self, skill_path: str) -> str:
        """
        Loads a skill (a reusable prompt or instruction) from a file.

        Args:
            skill_path (str): The path to the skill file.

        Returns:
            str: The content of the skill file.
        """
        try:
            with open(skill_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"Error: Skill file not found at {skill_path}"
        except Exception as e:
            return f"Error loading skill: {e}"

    def __str__(self):
        return f"Agent(Name: {self.name}, Description: {self.description})"
