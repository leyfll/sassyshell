import os
os.environ["GRPC_VERBOSITY"] = "ERROR"

import typer
from typing_extensions import Annotated
from pathlib import Path
from .classifier import find_most_similar_commands
from .storage import save_data, get_data
from .llm_client import get_results_from_llm
from .config import settings

FILE_NAME = settings.data_file


def sassysh(
    query: Annotated[str, typer.Argument(help="The query to process")] = "",
):
    user_input: dict[str, str] = {"user_query": query}
    load_data = get_data(FILE_NAME)
    
    similar_commands = find_most_similar_commands(query, load_data)
    context_summary = ""

    if similar_commands:
        context_summary += "Here are some previously asked queries by the user:\n\n"
        for cmd in similar_commands:
            context_summary += f"Generalized Command: {cmd.get('generalized_command', '')} \n User Queries: {', '.join(cmd.get('user_query', []))}\n\n"
            # print(cmd)
        
        user_input["context"] = context_summary


    response = get_results_from_llm(user_input)
    print(f"\n{response.message_to_user}\n")
        
    # Save data
    output = {
        "generalized_command": response.generalized_command,
        "user_query": [query],
        "statistics": {"times_called": 1}
    }
    save_data(output, FILE_NAME)


app = typer.Typer(help="SassyShell CLI")
app.command()(sassysh)

if __name__ == "__main__":
    app()
