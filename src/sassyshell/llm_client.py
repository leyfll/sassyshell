from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from .config import settings

class OutputFormat(BaseModel):
    message_to_user: str = Field(..., description="The message to display to the user")
    generalized_command: str = Field(..., description="The generalized version of the command to execute in the shell")

def get_llm_client():
    return init_chat_model(model=settings.llm_model_name, model_provider=settings.llm_model_provider, api_key=settings.llm_api_key).with_structured_output(OutputFormat)

llm = get_llm_client()

def get_results_from_llm(data: dict) -> OutputFormat:

    prompt = f"""You are an expert at translating user queries into shell commands.

    Here are some previously executed commands and their contexts (These might or might not directly relate to the current user query):
    {data.get('context', '')}

    If the user query is related to the context, use that information to be a bit sassy with your response, encouraging the user to learn the commands that they need help with often. If not, just provide a straightforward answer. You can use information like their provided stats to make better sassy comments.

    Keep the message to user short, not more than a few lines, and then give them the command that they asked for.

    For the generalized command, return a generalized definition of that command, replacing specific file names, paths, or parameters with placeholders like <file>, <directory>, <service_name>, etc. This helps in fetching relevant context easily for future queries.

    User query: {data.get('user_query', '')}
    """

    response =  llm.invoke(prompt)

    if not isinstance(response, OutputFormat):
        raise ValueError(f"LLM response is not in the expected format. Got: {response}")
    return response
