# create a virtual env
conda create -n mlflow_autolog python=3.10

# install some packages
conda install mlflow pandas scikit-learn

# gt requirement.txt for pip packages
pip freeze > requirements.txt

# copy or move this requirements.txt to a different environment and use it to install the packages
pip install -r requirements.txt

# Export your active environment to a new file
conda env export > environment.yml
# conda env export -n <env-name> > environment.yml


# Execute your code
python <YOUR_ML_CODE.py>

# View Your Results in the MLflow UI
mlflow ui --port 8080
