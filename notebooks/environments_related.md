# virtual environment
```p
python3.9 venv env_genai
source env/bin/activate
```

# removing virtual env
```p
source venv/bin/activate
pip freeze > requirements.txt
pip uninstall -r requirements.txt -y
deactivate
rm -r venv/
```

# conda environment
```p
conda create env_genai
conda remove env_genai
conda env list
conda activate env_genai
```

# activate environment
```p
pip install -r requirements.txt
```

# jupyter kernels
https://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove

```p
jupyter kernelspec list
ipython kernel install --name "env_genai" --user
jupyter kernelspec remove env_genai
```

