# Named Entity Recognition Demo
## Introduction
This a simple application showcasing [Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition) using [Transformers](https://huggingface.co/docs/transformers/index) as back-end and [Flask](https://flask.palletsprojects.com/en/2.3.x/) front-end.

## Instructions
### Running the application with Docker
This is the easiest way to run the app:

1. Clone the repository
2. Navigate to the root directory of the repository and run `docker compose up`
3. Open your browser and navigate to `http://localhost:5000/`

### Running the application without Docker
If you don't want to use Docker, you can run the application manually:

1. Clone the repository
2. Import conda environment from yml file: `conda env create -f environment.yml --name <env_name>`
3. Activate the environment: `conda activate <env_name>`
4. Run the application: `python app.py`. (Docker version uses `gunicorn` WSGI to run the app)
5. Open your browser and navigate to `http://localhost:5000/`

#### Running the tests
To run the tests, run `pytest` in the root directory of the repository once you have environment ready.
You can also run `pytest --cov=.` to get the coverage report.

## Usage
Once you have the application running, you enter/paste your text into the textbox and click 'Find named entities' button.
The application will return the text with named entities highlighted in colors according to the legend and confidence scores available when hovering over those.

## Future improvements
* Separate the front-end and back-end into separate services
* Add more models (and let user choose the model to use in the app)
* Experiment with different tokenizers and aggregation strategies