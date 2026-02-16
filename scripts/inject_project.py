import argparse
import subprocess
import shutil
import os
import sys

def run_command(command, cwd=None):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(
            command, cwd=cwd, check=True, text=True, capture_output=True, shell=True
        )
        print(f"COMMAND: {command}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"ERROR executing: {command}")
        print(e.stderr)
        # Don't raise here for git subtree add failures (merge conflicts), just return error or exit
        # Depending on criticality. Subtree add failure is critical for step 1.
        raise

def inject_project(project_name, repo_url, branch="main"):
    maestro_root = os.getcwd()
    project_dir = os.path.join(maestro_root, "projects", project_name)
    
    print(f"*** Injection Phase 1: Adding Remote & Subtree Add ***")
    
    remote_name = f"ejected-{project_name}"
    
    # Check if remote exists
    try:
        run_command(f"git remote remove {remote_name}")
    except:
        pass
        
    run_command(f"git remote add {remote_name} {repo_url}")
    run_command(f"git fetch {remote_name}")
    
    prefix = f"projects/{project_name}"
    
    # Subtree add
    # Using --squash to keep history clean in Maestro, or normal merge?
    # Spec says --squash in typical usage, but user might want history.
    # I'll default to --squash for now as per spec section 6.
    try:
        run_command(f"git subtree add --prefix={prefix} {remote_name} {branch} --squash")
    except subprocess.CalledProcessError:
        print("Subtree add failed. It might be because prefix already exists. Trying 'pull' instead...")
        # If project dir exists, maybe we want to pull updates
        run_command(f"git subtree pull --prefix={prefix} {remote_name} {branch} --squash")

    print(f"*** Injection Phase 2: Cleanup Framework Files ***")
    
    # Files to remove from the project directory because they are framework-level
    redundant_files = [
        "AGENTS.md",
        "manual.md",
        "agents",
        ".agent",
        "docs/standards", # directory
        ".github" # directory
    ]
    
    for item in redundant_files:
        path_to_remove = os.path.join(project_dir, item)
        if os.path.exists(path_to_remove):
            print(f"Removing redundant framework file: {path_to_remove}")
            if os.path.isdir(path_to_remove):
                shutil.rmtree(path_to_remove)
            else:
                os.remove(path_to_remove)
                
    print(f"*** Injection Phase 3: Knowledge Merge (Manual Check Required) ***")
    
    project_knowledge_dir = os.path.join(project_dir, "knowledge")
    maestro_knowledge_dir = os.path.join(maestro_root, "knowledge")
    
    if os.path.exists(project_knowledge_dir):
        print(f"Project has knowledge directory at {project_knowledge_dir}")
        print(f"Please manually compare contents with {maestro_knowledge_dir}")
        
        # Simple diff report
        project_files = set(os.listdir(project_knowledge_dir))
        for f in project_files:
            p_file = os.path.join(project_knowledge_dir, f)
            m_file = os.path.join(maestro_knowledge_dir, f)
            
            if os.path.exists(m_file):
                # Use git diff to show difference (if any)
                # But p_file is in the working tree now. m_file is also in working tree.
                # Just print notice
                print(f"[MERGE CHECK] Common file found: {f}")
            else:
                print(f"[NEW KNOWLEDGE] Found new file: {f}")
    
    print("*** Injection Complete ***")
    print("Please verify the 'projects/' directory and commit the result.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inject (Re-integrate) an ejected project back into Maestro.")
    parser.add_argument("project_name", help="Name of the project directory in projects/")
    parser.add_argument("repo_url", help="URL of the standalone repository")
    parser.add_argument("--branch", default="main", help="Branch to pull from (default: main)")
    
    args = parser.parse_args()
    
    inject_project(args.project_name, args.repo_url, args.branch)
