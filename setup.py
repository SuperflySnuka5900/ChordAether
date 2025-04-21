import os
import subprocess
import sys
from pathlib import Path
import shutil

VENV_DIR = Path(".venv")

def run(command):
    subprocess.check_call(command, shell=True)

def get_python_path():
    return VENV_DIR / "bin" / "python" if os.name == "posix" else VENV_DIR / "Scripts" / "python.exe"

def get_pip_path():
    return VENV_DIR / "bin" / "pip" if os.name == "posix" else VENV_DIR / "Scripts" / "pip.exe"

def create_virtualenv():
    python_path = get_python_path()
    if not python_path.exists():
        print(f"🌀 Creating virtual environment in {VENV_DIR}...")
        run(f"{sys.executable} -m venv {VENV_DIR}")
        if not python_path.exists():
            print("❌ Failed to create virtual environment.")
            sys.exit(1)
    else:
        print(f"✅ Virtual environment already exists at {python_path}")

def install_requirements(file="requirements.txt"):
    pip_path = get_pip_path()
    if not pip_path.exists():
        print("⚠️ pip not found in virtual environment. Aborting.")
        return
    if Path(file).exists():
        print(f"📦 Installing from {file}...")
        try:
            run(f"{pip_path} install -r {file}")
        except subprocess.CalledProcessError:
            print("❌ Error installing requirements.")
    else:
        print(f"⚠️ {file} not found. Skipping.")

def auto_activate():
    print("\n🚀 All done! Activating virtual environment...\n")
    if os.name == "posix":
        shell = os.environ.get("SHELL", "")
        shell_cmd = "zsh" if "zsh" in shell else "bash"
        os.execvp(shell_cmd, [shell_cmd, "-i", "-c", f"source {VENV_DIR}/bin/activate; exec {shell_cmd}"])
    elif os.name == "nt":
        subprocess.run(f"cmd.exe /k {VENV_DIR}\\Scripts\\activate.bat")
    else:
        print("⚠️ Auto-activation not supported on this OS.")

def clean_old_envs():
    print("\n🧹 Checking for old virtual environments to clean...")
    for folder in Path(".").iterdir():
        if folder.is_dir() and folder.name.lower().endswith("env") and folder.name != VENV_DIR.name:
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
    auto_activate()

if __name__ == "__main__":
    main()