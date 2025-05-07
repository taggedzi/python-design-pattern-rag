# Local config and setup.

- Make sure you already have Ollama installed. Make sure you have already created your virtual envronment with either venv or conda.  Make sure you have installed the python ollama library and other dependencies in the `requirements.txt` file located in the root of the depo.

- Download the model of your choosing. So far for this task (after MUCH testing) I have discoverd that on my local system `falcon3:7b` has given the best output results in a decent amount of time.
  ```bash
    C:\ollama pull falcon3:7b
  ```

- After installing navigate to a directory of your choosing and place the ModelFile.

- Then navigate to the Modelfile in the repo. IF you chose a different model please replace the name used by Ollama in the FROM section with the name of the model you wish to use before running the following command.
  ```bash
    C:\python-design-pattern-rag\ollama create pattern-rag-gen -f Modelfile
  ```
  This will create a model for the sole purpose of mapping out and processing these files.

- Now you can navigate back up to the project root directory and run:
  ```bash
    (venv) C:\python-design-pattern-rag\python .\chunk_all_patterns.py
  ```
  This will take some time.

- Once this is done your chunks directory in the root should be filled with markdown files named by the pattern they present. You will also find a json index in the root directory of the project.
