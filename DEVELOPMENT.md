# Development Guide
This document provides a guide on how to set up your development environment and contribute to this project.
## Prerequisites
- Docker: Install Docker on your machine. You can download it from the official Docker website.
- Python 3.8+: Make sure you have Python 3.8 or a higher version installed on your system.

## Setting Up Your Development Environment

1. Clone the repository: `git clone https://github.com/spinnernicholas/label-studio-cli.git`
2. Navigate to the project directory: `cd label-studio-cli`
3. Install dependencies: `pip install -e .[dev]`
4. Start Label Studio server for development: `scripts/dev up`

## Development Project Commands
The following commands can be used for the development of this project:
### Label Studio Docker Dev Container Controls
- `scripts/dev up <docker up args>`: Starts the Label Studio dev container.
- `scripts/dev down <docker down args>`: Stops the Label Studio dev container.
- `scripts/dev shell`: Opens a shell inside the running dev container.
- `scripts/dev exec <command>`: Executes a command inside the running dev container.

These commands are located in the `scripts/dev.bat` file.
## Building the Project
Describe how to build the project, if applicable.
## Running Tests
Describe how to run tests, if applicable.
## Submitting a Pull Request
1. Fork the repository.
2. Create a new branch for your changes: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m "Add my feature"`
4. Push your branch to your fork: `git push origin my-feature-branch`
5. Open a pull request from your fork to the original repository.

## Reporting Issues
Describe how to report issues, if applicable.
## Additional Resources
- Link to any additional documentation or resources that might be helpful for developers.