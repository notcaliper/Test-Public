import os
from git import Repo

# Replace with your repository and branch details
repo_url = 'https://github.com/yourusername/your-repo.git'
branch_name = 'main'
local_path = 'path/to/local/clone'

# Clone the repository
if not os.path.exists(local_path):
    print(f"Cloning repository from {repo_url} to {local_path}")
    Repo.clone_from(repo_url, local_path, branch=branch_name)

# Open the repository
repo = Repo(local_path)

# Create a new file or update an existing file
file_path = os.path.join(local_path, 'example.txt')
with open(file_path, 'w') as file:
    file.write('Hello, GitHub!')

# Stage the file
repo.index.add([file_path])

# Commit the change
commit_message = 'Updated example.txt'
repo.index.commit(commit_message)

# Push the change to the remote repository
origin = repo.remote(name='origin')
origin.push()

print(f"Changes pushed to {repo_url} on branch {branch_name}")
