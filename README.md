# rock_paper_scissors
A simple Rock, Paper and Scissors game between a human player and a bot.

### Steps to run the application on your local machine
```bash
virtualenv <name_python_env> -p python3.7
```
```bash
cd <some_directory_on_your_computer>
```
```bash
git clone https://github.com/ShahidYousuf/rock_paper_scissors.git
```
```bash
cd rock_paper_scissors
```
```bash
source <path_to_your_env>/bin/activate
```
```bash
pip install -r requirements.txt
```
Make sure your mysql database is created (create database <your_db_name> inside mysql)

Make your own local_settings setting up the DATABASE setting variable
```bash
python manage.py migrate --settings=<your.local_settings>
```
```bash
python manage.py runserver --settings=<your.local_settings>
```
check the application running on port 8000.

#### Contributions are welcome. Just create your own branch and send a pull request. Happy coding!
