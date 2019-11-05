# Modules Lesson
### Joe Holleran	
### Python 2 Fall 2019

https://docs.python.org/3/tutorial/modules.html

## What is a Module?

Module = definitions in a file that can be imported into other modules or the main module

* Module is a file containing Python definitions and statements
* The module name is the file name with .py at end

## Why would I use a Module? 

* You've created a longer program and would like to spread out the code over several files
* You may have a function that is used in numerous programs so you can create a module instead of copying the function into the program

## How do I create a Module?

* Create a file name in the current directory (Ex: abc.py)
* Within file (abc.py) you can write the definitions or statements (such as a function)
* The module is then accessed by import filename
* You can then access the individual functions within the module: filename.function
* Or you can import each of the functions directly: from filename import function1, function2
* If the module name is followed by as then the name following as is bound directly to the imported module (ex: import filename as fn; fn.function1(), fn.function2(), etc.)

## Module Search Path

When a module is imported the interpreter searches for a built-in module with that name.  If not found, it then searches for the file name in a list of directories:

* Directory containing the input script (or current directory)
* PYTHONPATH
* Installation-dependent default

## Compiled Python Files

Python will caches the compiled version of each module in \__pycache__\ directory

## dir() Function

dir() is a built-in function that allows you to find out the names a module defines

* dir(filename)

## Packages

Packages are collections of modules

* Create a directory (directory name will be the package name)
* Put the modules in the package directory
* Create a \__init\__.py file in the directory (\__intit\__.py lets Python know it is a package directory)

* from package file name import module file name
* Or PackageName.ModuleName()
* The module name after the . is a submodule


