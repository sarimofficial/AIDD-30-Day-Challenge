from ..base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    """
    The ResearchAgent is responsible for gathering information on specific topics.
    """
    def __init__(self, name: str = "ResearchAgent", description: str = "Gathers information on given topics."):
        super().__init__(name, description)

    def execute_task(self, task: str, context: dict = None) -> str:
        """
        Executes a research task.

        Args:
            task (str): The research task (e.g., "Find information on AI ethics").
            context (dict, optional): Additional context, e.g., {"topics": ["AI ethics"]}.

        Returns:
            str: A simulated research result.
        """
        topics = context.get("topics", ["general knowledge"]) if context else ["general knowledge"]
        print(f"[{self.name}] Executing task: '{task}' for topics: {', '.join(topics)}")
        # In a real scenario, this would involve web scraping, database queries, etc.
        return f"Research results for {', '.join(topics)}: [Simulated data for '{task}']"
