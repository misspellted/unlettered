# unlettered

The initial intent is to make use of an Azure Function to send a message to a channel in a Discord server.

After that?

World domination.

*cough*

I don't know.

## Setup

### Virtual Python Environment

To setup this project, it is recommended to create a virtual Python environment (using the `venv` module):

    python -m venv .dev

Or, if you have a different naming convention, use that. This is the folder referenced in the `.gitignore` file, so if you use a different one, make sure to add that one to your ignored entries.

When the virtual Python environment is created, activate it by using a command similar to the following:

    source .dev/bin/activate

Your platform may have different ways to activate, and if you used a different virtual environment name, update the command accordingly, or use your integrated development environment to activate the environment automatically.

The reason for activating the virtual environment is such that when `pip` is invoked, the packages/modules installed target the virtual environment, keeping the local system packages/modules as such only needed by the system Python environment, not our project(s). A clean environment is a good environment, and one step closer to reproducibility, a good attribute for development and testing environments.

## Notes

### Development Environment

Currently thinking of setting up a Virtual Box machine for development purposes, but also remembered something mentioned at work: Dev Containers. So... we'll see how this matures, if at all.. mowuahahaha... right. Professionalism... mostly.

### Infrastructure Repository

As it turns out, the Azure RM provider yields a way to make use of a `source_control` block within the `azurerm_function_app` resource. Therefore, it's probably better to keep the infrastructure separated. Initially, the idea was to keep it all self-contained, but that's probably not the best practice. So, before even the first commit of the 'provision-az-function' branch was made, the Terraform infrastructure as code files were ripped out, and put into the `unlettered-infra` repository.
