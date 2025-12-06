import yaml
import os
from agents.orchestrator import OrchestratorAgent

def load_book_outline(file_path):
    """Loads the book outline from a YAML file."""
    if not os.path.exists(file_path):
        print(f"Error: Book outline file not found at {file_path}")
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def main():
    print("Starting book writing process...")
    outline_path = "book_outline.yaml"
    book_outline = load_book_outline(outline_path)

    if book_outline:
        print("\nBook Outline Loaded:")
        # print(yaml.dump(book_outline, indent=2))
        
        orchestrator = OrchestratorAgent(name="Book Writing Orchestrator", description="Manages the book writing process.")
        result = orchestrator.execute_task("Write a book based on the outline", {"book": book_outline['book']})
        
        output_path = os.path.join("output", "book.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"\nBook saved to {output_path}")

    else:
        print("Failed to load book outline. Exiting.")

if __name__ == "__main__":
    # Ensure PyYAML is installed: pip install PyYAML
    main()

