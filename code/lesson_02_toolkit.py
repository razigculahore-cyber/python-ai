"""Task 1.2: print my AI dev toolkit with the real installed versions."""

import shutil
import subprocess
import sys

# Each tool and the command that prints its version
tools = {
    "uv": ["uv", "--version"],
    "Editor": ["code", "--version"],
    "Git": ["git", "--version"],
    "Ollama": ["ollama", "--version"],
    "Claude Code": ["claude", "--version"],
}


def get_version(command):
    path = shutil.which(command[0])
    if path is None:
        return "not installed"
    result = subprocess.run([path, *command[1:]], capture_output=True, text=True)
    # Some tools print several lines; the first line holds the version
    first_line = result.stdout.strip().splitlines()[0]
    # Tools wrap the number in extra words ("git version 2.55.0"), so keep only the word that starts with a digit
    for word in first_line.split():
        if word[0].isdigit():
            return word
    return first_line


my_toolkit = {"Python": sys.version.split()[0]}
for name, command in tools.items():
    my_toolkit[name] = get_version(command)
my_toolkit["Editor"] = f"VS Code {my_toolkit['Editor']}"

print("My AI Dev Toolkit")
print("-----------------")
for name, version in my_toolkit.items():
    print(f"{name}: {version}")
