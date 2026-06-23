# Autotest project on Python

### Cloning repo
Go to directory you want to keep the repo:
```bash
cd <root_directory_of_the_projects>
```
Clone this repository by the command:
```bash
git clone https://github.com/olegtemirbulatov/autotest.git
```

### Installing dependencies
1. Create virtual environment
```bash
python -m venv venv
```
2. Activate it
```bash
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

### Running tests
Just run a command below:
```bash
pytest .
```

### Running UI tests (login to GitHub)
Go to directory you want to keep the repo:
```bash
cd <root_directory_of_the_projects>
```
Create a file `.env`.

Fill this file with your credentials to login to GitHub:
```
GH_USER = "<your email or username>"
GH_PASS = "<your password>"
```
Run tests by the command below 
```bash
pytest . --headed
```
The flag `--headed` enables showing the browser window.
Or just add this flag to pytest.ini:
```
[pytest]
addopts = -ra --headed
```