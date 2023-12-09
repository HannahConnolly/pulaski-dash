


### Install Python Virtual Environment

1. Create virtual environment .venv folder (containerized python)

`python3 -m venv .venv`

2. Activate virtual environment

`source .venv/bin/activate`

3. Install packages

`pip install -r requirements.txt`

4. Run app

`python3 app.py`

### Troubleshooting

My python broke, what happened?

 - make sure that the containerized enviroment is active `source .venv/bin/activate`
 - if this doesnt work. reinstall starting with `sudo rm -rf .venv` and begin at step 1
