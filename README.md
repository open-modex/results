# The Results of the open_MODEX Models

This repository contains results obtained via the different models
developed during the [open_MODEX][0] project which is an effort to get
insight into the different approaches on energy system modelling by
comparing five different energy modelling frameworks. One part of this
comparison is the development of different energy models using each
framework. The different models conform to scenarios which are the same
for each framework. By comparing the results obtained using each
framwork's model for a given scenario, we obtain a practical way of
gauging the differences between the frameworks.


## Repository Structure

The repository root contains a folder for each framework that is part of
the comparison. These folders in turn contain subfolders for each
scenario. These subfolders are named by numeric identifiers whose
meaning follows the table under
[Directory Scenario Mapping](#directory-scenario-mapping).
Finally, the scenario folders contain CSV files with the results of a
model of the given scenario implemented using the given framework.
These CSV files are named according to the table under
[Result Filenames](#result-filenames). The repository root also contains
documentation or other auxiliary files which should be self explanatory.

Generally, the repository structure should look something like this:

```
Repository Root
|
|- Documentation and Auxiliary Files
|
|+ Framework Name
   |
   |+ Numeric Identifier
      |
      |- CSV Files w. Results
```


## Directory Scenario Mapping

| Numeric identifier | Name | Description | 
| ---: | :--- | :--- |
| 1 | om-onenode                        | A minimal scenario containing only one node. |
| 2 | om-onenode-storage                | Extends scenario 1 with a storage. |
| 3 | om-threenode-transmission         | A scenario having three nodes and constraints <br/> on the transmission capacities between them. |
| 4 | om-threenode-storage-transmission | Extends scenario 3 with a storage. |

## Result Filenames

| Filename | Description | Unit |
| :--- | :--- |
| `contraints.csv` | number of contraints/inequalities created in the energy system model | - |
| `memory.csv` | momory storage required to solve the problem | MB | 
| `objective.csv` | objective value of the optimisation problem | EURO | 
| `production_elec.csv` | number of variables created in the energy system model | MWh | 
| `timebuild.csv` | time indicator of machine needs to build the model | s | 
| `variables.csv` | number of variables created in the energy system model | - | 


[0]: https://reiner-lemoine-institut.de/en/open_modex-2/
