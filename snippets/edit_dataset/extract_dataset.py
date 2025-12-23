from datasets import load_dataset
from huggingface_hub import whoami

USERNAME = whoami()["name"]
print(USERNAME)