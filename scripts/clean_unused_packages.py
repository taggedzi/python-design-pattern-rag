import os
import ast
import subprocess
import pkg_resources
from pathlib import Path

def get_installed_packages():
    return {pkg.key for pkg in pkg_resources.working_set}

def get_imported_modules(code_root):
    imported = set()

    for file in Path(code_root).rglob("*.py"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read(), filename=str(file))
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            imported.add(alias.name.split('.')[0])
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            imported.add(node.module.split('.')[0])
        except Exception as e:
            print(f"⚠️ Skipping {file}: {e}")
    return imported

def find_unneeded_packages(imported_modules, installed_packages):
    builtin_modules = stdlib_modules()
    safe_imports = imported_modules - builtin_modules
    return sorted(installed_packages - safe_imports)

def stdlib_modules():
    # Includes common builtins — this list is a best-effort, not exhaustive
    import sys
    if hasattr(sys, 'stdlib_module_names'):
        return set(sys.stdlib_module_names)
    else:
        import distutils.sysconfig as sysconfig
        stdlib = sysconfig.get_python_lib(standard_lib=True)
        return {p.name for p in Path(stdlib).iterdir() if p.is_dir()}

def uninstall_packages(packages):
    for pkg in packages:
        confirm = input(f"Uninstall '{pkg}'? [y/N]: ").lower()
        if confirm == "y":
            subprocess.run(["pip", "uninstall", "-y", pkg])

if __name__ == "__main__":
    print("🔍 Scanning for unused packages...")
    code_root = "."  # You can customize this path
    installed = get_installed_packages()
    imported = get_imported_modules(code_root)
    unused = find_unneeded_packages(imported, installed)

    print(f"\n📦 Unused packages ({len(unused)}):")
    for pkg in unused:
        print(f"  - {pkg}")

    if unused:
        uninstall = input("\n❓ Do you want to uninstall them now? [y/N]: ").lower()
        if uninstall == "y":
            uninstall_packages(unused)
