# Template for Swimlane python projects

## Description

## Initialize repository

This template has all initial files included, there are a few configurations you still need to do.

- For simple script jobs, you can leave `src` directory name, for packages that might need to be published you
need to change it something meaningful. This will be your library name.
  
- Library name is used in tests sample test. Make sure you adjust or remove the tests that will be broken.

- Edit setup.json with the values specific for your project. One change is name should be the name of library.

- `setup.py` reads this file to submit as long description, remove this section before publishing your
package anywhere.
  
## Developer

Even for simple scripts it is recommended to put them in the `src` folder and follow initialization steps. So the
project build can be tested with `python setup.py build` and unit tests can be run with `pytest`. 

These commands are included in github action that will protect the main branch from a corrupted PR.