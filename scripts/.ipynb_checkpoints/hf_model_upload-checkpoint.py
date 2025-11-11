from huggingface_hub import upload_folder, create_repo, login

# (1) Login once per environment (will prompt you for your token)
# login(token="your_HF_token")  # or run `huggingface-cli login` in terminal first

# (2) Define your local folder and repo
local_folder_path = "./out"
repo_id = "royam0820/nanochat-speedrun-001"

# (3) Create the repo if it doesn’t exist yet
create_repo(repo_id, repo_type="model", private=False, exist_ok=True)

# (4) Upload the folder
upload_folder(
    folder_path=local_folder_path,
    repo_id=repo_id,
    commit_message="Upload initial model and related files",
)

print(f"✅ Successfully uploaded '{local_folder_path}' to 'https://huggingface.co/{repo_id}'")
