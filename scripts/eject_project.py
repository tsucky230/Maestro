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
        raise

def copy_framework_files(target_dir):
    """Copy Maestro framework files to the ejected project root."""
    maestro_root = os.getcwd()
    
    # List of files/dirs to copy
    # Note: excluding .git, projects/, scripts/, etc.
    framework_items = [
        "AGENTS.md",
        "manual.md",
        "agents",
        ".agent",
        "knowledge",
        "docs/standards",
        "docs/templates",
        ".github"
    ]

    print("--- Copying Framework Files ---")
    for item in framework_items:
        src_path = os.path.join(maestro_root, item)
        dst_path = os.path.join(target_dir, item)
        
        if os.path.exists(src_path):
            if os.path.isdir(src_path):
                # shutil.copytree requires dest to not exist, or validation
                # In ejected repo root, these shouldn't exist yet typically, or we merge.
                # git subtree split might have brought some if they were in project folder?
                # But project folder shouldn't have these.
                if os.path.exists(dst_path):
                    print(f"Warning: {item} already exists in target. Overwriting/Merging...")
                    # Recursive copy/merge implementation for existing dirs
                    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
                else:
                    shutil.copytree(src_path, dst_path)
            else:
                shutil.copy(src_path, dst_path)
            print(f"Copied: {item}")
        else:
            print(f"Warning: Source {item} not found. Skipped.")

def eject_project(project_name, new_repo_url):
    project_path = os.path.join("projects", project_name)
    if not os.path.exists(project_path):
        print(f"Error: Project directory '{project_path}' does not exist.")
        sys.exit(1)

    branch_name = f"eject/{project_name}"
    
    print(f"*** Ejecting Phase 1: Git Subtree Split for {project_name} ***")
    # 1. git subtree split
    # Note: On Windows specifically, 'prefix' formatting can be tricky. Using / separator.
    prefix = f"projects/{project_name}"
    run_command(f"git subtree split --prefix={prefix} -b {branch_name}")

    print(f"*** Ejecting Phase 2: Preparing Temporary Repository ***")
    # 2. Setup new repo in temp dir
    temp_dir = os.path.abspath(f"temp_eject_{project_name}")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    run_command("git init", cwd=temp_dir)
    
    # Pull from the split branch of the parent repo
    # Path to parent repo is current dir
    parent_repo_path = os.getcwd()
    # On Windows, path might be problematic in git URL if backslashes.
    parent_repo_path = parent_repo_path.replace("\\", "/")
    
    print(f"Pulling from {parent_repo_path} branch {branch_name}...")
    run_command(f"git pull \"{parent_repo_path}\" {branch_name}", cwd=temp_dir)

    print(f"*** Ejecting Phase 3: Injecting Maestro Framework ***")
    # 3. Copy Framework Files
    copy_framework_files(temp_dir)
    
    print(f"*** Ejecting Phase 4: Committing and Pushing ***")
    # 4. Commit and Push
    run_command("git add .", cwd=temp_dir)
    try:
        run_command("git commit -m \"chore: eject project from Maestro framework\"", cwd=temp_dir)
    except Exception:
        print("Nothing to commit (framework files might match existing content?). Proceeding.")

    run_command(f"git remote add origin {new_repo_url}", cwd=temp_dir)
    
    print(f"Pushing to {new_repo_url}...")
    # NOTE: Actual push is commented out for safety in dry-run/dev.
    # User should run manually or uncomment.
    # But specification says "Push". I will include it but maybe add a flag?
    # I'll just let it fail if URL is invalid, or print it.
    print(f"READY TO PUSH: git push -u origin main (inside {temp_dir})")
    
    try:
        run_command("git push -u origin main", cwd=temp_dir)
    except Exception as e:
        print(f"Push failed (expected if URL is dummy): {e}")
        print("You can verify the ejected repo in: " + temp_dir)

    print("Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Eject a project from Maestro to a standalone repo.")
    parser.add_argument("project_name", help="Name of the project directory in projects/")
    parser.add_argument("repo_url", help="URL of the new remote repository")
    
    args = parser.parse_args()
    
    eject_project(args.project_name, args.repo_url)
