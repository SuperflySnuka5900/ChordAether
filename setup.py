import os
import subprocess
import sys
from pathlib import Path
import shutil

VENV_DIR = ".venv"

def run(command):
    subprocess.check_call(command, shell=True)

def get_pip_path():
    return f"{VENV_DIR}/bin/pip" if os.name == "posix" else f"{VENV_DIR}\\Scripts\\pip"

def create_virtualenv():
    if not Path(VENV_DIR).exists():
        print(f"🌀 Creating virtual environment in {VENV_DIR}...")
        run(f"{sys.executable} -m venv {VENV_DIR}")
    else:
        print(f"✅ Virtual environment '{VENV_DIR}' already exists.")

def install_requirements(file="requirements.txt"):
    if Path(file).exists():
        print(f"📦 Installing from {file}...")
        run(f"{get_pip_path()} install -r {file}")
    else:
        print(f"⚠️ {file} not found. Skipping.")

def merge_old_requirements():
    if Path("old-requirements.txt").exists():
        print("🔁 Merging old dependencies...")
        install_requirements("old-requirements.txt")
        print("📝 Updating requirements.txt with merged packages...")
        run(f"{get_pip_path()} freeze > requirements.txt")
    else:
        print("ℹ️ No old-requirements.txt found. No merge needed.")

def auto_activate():
    print("\n🚀 All done! Activating virtual environment...\n")
    if os.name == "posix":
        shell = os.environ.get("SHELL", "")
        if "zsh" in shell:
            os.execvp("zsh", ["zsh", "-i", "-c", f"source {VENV_DIR}/bin/activate; exec zsh"])
        else:
            os.execvp("bash", ["bash", "-i", "-c", f"source {VENV_DIR}/bin/activate; exec bash"])
    elif os.name == "nt":
        subprocess.run(f"cmd.exe /k {VENV_DIR}\\Scripts\\activate.bat")
    else:
        print("⚠️ Auto-activation not supported on this OS.")

def clean_old_envs():
    print("\n🧹 Checking for old virtual environments to clean...")
    for folder in Path(".").iterdir():
        if (
            folder.is_dir() and
            folder.name.lower().endswith("env") and
            folder.name != VENV_DIR
        ):
            answer = input(f"🗑️ Found '{folder.name}'. Delete it? [y/N] ").strip().lower()
            if answer == "y":
                shutil.rmtree(folder)
                print(f"✅ Deleted {folder.name}")
            else:
                print(f"⏭️ Skipped {folder.name}")

def main():
    clean_old_envs()
    create_virtualenv()
    install_requirements()
    merge_old_requirements()
    auto_activate()

if __name__ == "__main__":
    main()
