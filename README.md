# AMG Frogsekai Discord Bot

## Table of Contents

1. [Setting up development](##setting-up-development)
2. [Contribution guide](##contribution-guide)

## Setting up development

A virtual environment is an important component to any Python project because there are a lot
of Python libraries and they are huge. By keeping them in a virtual environment, you have a
different setup per project and so if you have two different libraries with the same name
where each is being used in different projects, they won't overlap and intrude on each other.
Also, once you have completed a project, it is a lot easier to clean a virtual environment
than clean your machine.

1. Ensure your Python3 is at least 3.7. It is possible you only have Python 3 installed so it
may be found under the command `python`.

```bash
% python3 --version
Python 3.8.2
```

2. Create a virtual environment named `env` using the following command. This directory is in
the `.gitignore` because Python has a lot of files and it's not scalable nor feasible to be
keeping track of all of them inside the repository.

```bash
% python3 -m pip --version
pip 21.2.4 from <where pip is installed on your computer>
% python3 -m pip install --user virtualenv
...
% python -m venv env
```

If pip is not version 21, upgrade it by using the command: `python3 -m pip install --user --upgrade pip`.

3. Now you should have a directory called `env` which holds the information about your virtual 
environment, but you're not in your virtual environment. To start the virtual environment, 
use the following commands.

```bash
% source env/bin/activate
```

If you are using Windows, the script will be located in the directory `env/Scripts` instead of `env/bin`.

If you have a basic terminal setup, the terminal will show the virtual environment is activated by having a
`(env)` at the very start of the command prompt.

```bash
(env) %
```

4. The final step is to install the libraries required which have all been conveniently included in a file
named `requirements.txt`.

```bash
(env) % python3 -m pip install -r requirements.txt
```

Even though different developers have different virtual environments, by managing the libraries required
(dependencies) in the `requirements.txt`, this ensures everyone is using the same libraries.

5. To leave the virtual environment:

```bash
(env) % deactivate
```

6. The next time you want to start working on the bot, it is not required to install `requirements.txt` 
but it is good practice to, just in case something has changed or been added.

```bash
% source env/bin/activate
(env) % python3 -m pip install -r requirements.txt
(env) % # do some git stuff and maybe some coding stuff too
(env) % deactivate
```

## Contribution guide

To be updated later.
