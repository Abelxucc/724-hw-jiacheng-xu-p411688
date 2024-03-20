from flask import Flask, render_template, jsonify
from forms import FeedbackForm

app = Flask(__name__)
