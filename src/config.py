API_KEY_PATTERN_NAME = "API_KEY"

PATH_SYS_PROMPT = "./data/sys_prompt.txt"
SYS_VARIABLES = {"tools_manual": "NO TOOLS"}

PATH_USER_PROMPT = "./data/user_prompt.txt"
USER_VARIABLES = {
    "task_description": None,
    "context": None,
    "max_iterations": None,
    "expected_output": None,
}

STOP_PROMPT = [
    "Observation:",
    "Observation\n",
    "```Thought",
    "```\nThought",
]
