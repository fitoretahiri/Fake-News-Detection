# Fake-News-Detection

FactChecker is a web based application. Its purpose is to check wether the provided news are reliable or not reliable.

## Machine Learning Model Details

A machine learning model was trained and used to predict if news content is reliable or fake. Various algorithms were considered, including:

- Logistic Regression: accuracy score of approximately `98.92%`
- Random Forest: accuracy score of approximately `99.26%`
- Decision Tree Algorithm: accuracy score of approximately `99.63%`

`Decision Tree` was saved in pickle file because it produced slightly higher accuracy score.

## Tech stack

FactChecker was programmed using:

1.  **Frontend**: HTML, Tailwind CSS
2.  **Backend**: Python Django
3.  **Database**: SQLite

## Details

FactChecker is a news blog. It contains news articles but the difference is that for every added content, the model will immediately predict wether the content is reliable or not. A message: `Content is reliable`, will be generated in green color or `Content is not reliable`, will be generated in red color. The website contains a button to check for your content as well. There you can simply paste your own content to check wether it is fake or reliable. The system generates the message mentioned above.

## Installation

1. Make sure you have Python installed in version at least 3.10.0
2. Activate Python virtual environment venv.
3. Apply migrations using the command: `python manage.py migrate`
4. Create super user to access admin dashboard and sqlite: `python manage.py createsuperuser`
5. Run the server using the command `python manage.py runserver` or by simply pressing `F5` in your keyboard.