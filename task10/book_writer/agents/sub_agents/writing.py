from ..base_agent import BaseAgent

class WritingAgent(BaseAgent):
    """
    A sub-agent specialized in writing content for chapters.
    """
    def __init__(self, name: str = "WritingAgent", description: str = "Writes chapter content based on outlines."):
        super().__init__(name, description)

    def execute_task(self, task: str, context: dict = None) -> str:
        """
        Executes a writing task.

        Args:
            task (str): The writing instruction (e.g., "Write chapter 'Introduction'").
            context (dict, optional): Additional context, e.g., {"outline": "..."}.

        Returns:
            str: Simulated chapter content.
        """
        print(f"[{self.name}] executing task: '{task}'")
        outline_data = context.get("outline", "no outline provided") if context else "no outline provided"
        # In a real scenario, this would generate creative content based on the outline.
        return f"[{self.name}] Draft content for '{task}' based on outline: ({outline_data}). (Simulated chapter text)"