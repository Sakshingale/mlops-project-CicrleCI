from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.read().splitlines()
        # Remove empty lines and editable installs if any
        requirements = [req for req in requirements if req and not req.startswith("-e")]
    return requirements

setup(
    name="mlops_project_6",   # avoid hyphens in package name
    version="0.1.0",
    author="Sakshi Ingale",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.8",
)
