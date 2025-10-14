import typer
from typing_extensions import Annotated
from pathlib import Path
from .classifier import find_most_similar_commands
from .storage import save_data, get_data
from .config import settings

FILE_NAME = settings.data_file


def sassysh(
    query: Annotated[str, typer.Argument(help="The query to process")] = "",
):
    load_data = get_data(FILE_NAME)
    # Call the similarity function

    # Processing dummy
    print(f"Processing query: {query}\nLoaded data: {load_data}")
    similar_commands = find_most_similar_commands(query, load_data)
    if similar_commands:
        print("Found similar commands:")
        for cmd in similar_commands:
            print(cmd)

    # Save data
    sample_output = {
        "generalized_command": "testing",
        "user_query": [query],
        "statistics": {"times_called": 1},
    }
    save_data(sample_output, FILE_NAME)


app = typer.Typer(help="SassyShell CLI")
app.command()(sassysh)

if __name__ == "__main__":
    app()
