from .base_agent import BaseAgent
from .sub_agents.research import ResearchAgent
from .sub_agents.outlining import OutliningAgent
from .sub_agents.writing import WritingAgent
from .sub_agents.editing import EditingAgent

class OrchestratorAgent(BaseAgent):
    """
    The main orchestrator agent that manages the book writing process.
    """

    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.sub_agents = {
            "research": ResearchAgent(),
            "outlining": OutliningAgent(),
            "writing": WritingAgent(),
            "editing": EditingAgent(),
        }

    def execute_task(self, task: str, context: dict = None) -> str:
        """
        Executes the main book writing task.

        Args:
            task (str): The main task (e.g., "Write a book based on the outline").
            context (dict, optional): The book outline and other context.

        Returns:
            str: The result of the book writing process.
        """
        print(f"[{self.name}] received task: {task}")

        if not context or "book" not in context:
            return "Error: Book outline not provided in the context."

        book_outline = context["book"]
        book_content = []
        book_content.append(f"# {book_outline.get('title', 'N/A')}\n")
        book_content.append(f"By {book_outline.get('author', 'N/A')}\n\n")

        for chapter in book_outline.get('chapters', []):
            chapter_title = chapter.get('title', 'Untitled Chapter')
            book_content.append(f"## {chapter_title}\n\n")

            # 1. Research (placeholder)
            research_task = f"Research the topics for the chapter: {chapter_title}"
            research_context = {"topics": chapter.get("topics", [])}
            research_result = self.sub_agents["research"].execute_task(research_task, research_context)

            # 2. Outlining
            outlining_task = f"Create a detailed outline for the chapter: {chapter_title}"
            outline = self.sub_agents["outlining"].execute_task(outlining_task, {"research": research_result})
            
            # 3. Writing
            writing_task = f"Write the chapter '{chapter_title}' based on the outline."
            written_chapter = self.sub_agents["writing"].execute_task(writing_task, {"outline": outline})

            # 4. Editing
            editing_task = f"Edit the chapter: {chapter_title}"
            edited_chapter = self.sub_agents["editing"].execute_task(editing_task, {"chapter_content": written_chapter})
            book_content.append(edited_chapter)
            book_content.append("\n\n")

        return "".join(book_content)