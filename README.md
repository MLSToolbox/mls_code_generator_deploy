# MLSToolbox Code generator components

MLSToolbox is composed by the following components that are included in this repository as folders.

<p align="center" width="100%">
   <img src="https://github.com/MLSToolbox/.github/blob/main/media/mls_code_generator/mls_code_generator_architecture.png" alt="MLSToolbox Code Generator architecture" width="500">
</p>

| Component| Description |
| ---------| ----------- |
| mls_toolbox_client | An Angular-based component for displaying a node-based editor to define ML pipelines |
| mls_toolbox_server | A Flask-based component for redirecting the mls_toolbox_client requests to the services provided by the mls_code_generator |
| mls_code_generator | A Python component for mainly generating Python code for the ML pipelines represented in the editor |
| mls_code_generator/mls_lib | A Python library containing object classes, used in the generated code, representing the structure and the main concepts required to instantiate any pipeline, its stages and the tasks that these stages perform |
| mls_code_generator/mls_code_generator_config | A component containing several extensible JSON files that define the graphical elements of the graphical editor representing the predefined steps of a ML pipeline |

# Documentation
You can find all the information you need in our [WIKI!](https://github.com/MLSToolbox/mls_code_generator/wiki)).

# Demos
This video shows how to use the MLSToolbox Pipeline Code generator to define a pipeline and generate the code to generate the model. More details about the example used in this video are available at [mls_code_generator Wiki](https://github.com/MLSToolbox/mls_code_generator/wiki/Diabetes-prediction).

https://github.com/user-attachments/assets/5c783523-529b-4cee-a7e6-7fc400e53633

You can find more videos at [mls_code_generator Wiki](https://github.com/MLSToolbox/mls_code_generator/wiki/Videos).

# Deployment
Each of the folder contains their own docker_build.shand docker_run.sh files. Once both are executed, the system should be up and running!

# Contributing

You can find the MLSToolbox Contribution Guidelines [here](https://github.com/MLS-Toobox/mls_toolbox/blob/main/CONTRIBUTING.md).

# Code of Conduct

You can find the MLSToolbox Code of Conduct [here](https://github.com/MLSToolbox/.github/blob/main/CODE_OF_CONDUCT.md)
