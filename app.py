import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from modules.ner_inference import NER_Inference_Simple
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import TextAreaField, SubmitField

class NERForm(FlaskForm):
    sequence = TextAreaField('Input text', validators = [DataRequired()])
    submit = SubmitField('Find NERs')

def create_app():
    SECRET_KEY = os.urandom(32)

    app = Flask(__name__)
    Bootstrap(app)
    app.config['SECRET_KEY'] = SECRET_KEY

    ner_engine = NER_Inference_Simple()

    @app.route('/', methods = ['GET', 'POST'])
    def main():
        
        form = NERForm()
        if form.validate_on_submit():
            sequence = form.sequence.data
            result = ner_engine.predict(sequence)
            
            return render_template('index.html', result = result, form=form)
        result = []
        return render_template('index.html', result = result, form=form)

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)