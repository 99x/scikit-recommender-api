from flask import request
from flask import Flask, url_for
from scikits.crab import datasets

app = Flask(__name__)
from os.path import dirname
from os.path import join
import numpy as np
import pprint as pprint


@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

def get_movie_dataset():
    movies = datasets.load_sample_movies()
    pprint.pprint(movies.data)
    pprint.pprint(movies.user_ids)
    pprint.pprint(movies.item_ids)
    return movies

def create_ml_model_for_recomendations(data):
    from scikits.crab.models import MatrixPreferenceDataModel
    model = MatrixPreferenceDataModel(data)
    return model

def generate_recomendations(model):
    from scikits.crab.metrics import pearson_correlation
    from scikits.crab.similarities import UserSimilarity
    #Build the similarity
    similarity = UserSimilarity(model, pearson_correlation)
    from sklearn.base import BaseEstimator
    from scikits.crab.recommenders.knn import UserBasedRecommender
    #build the user Based recommender
    recommender = UserBasedRecommender(model, similarity, with_preference=True)
    #recommend item for the user 5 (Toby)
    recomendations = recommender.recommend(5)
    return recomendations

def execute_steps():
    movies  = get_movie_dataset()
    model = create_ml_model_for_recomendations(movies.data)
    recomendations = generate_recomendations(model)
    pprint.pprint(recomendations)
    return 0

@app.route('/import')
def api_import():
    execute_steps()
    return 'List of ' + url_for('api_articles')

@app.route('/import1')
def api_import1():
    movies = datasets.load_sample_movies()
    import pprint ## to make printed items clearer
    pprint.pprint(movies.data)
    pprint.pprint(movies.user_ids)
    pprint.pprint(movies.item_ids)
    from scikits.crab.models import MatrixPreferenceDataModel
    #Build the model
    model = MatrixPreferenceDataModel(movies.data)
    from scikits.crab.metrics import pearson_correlation
    from scikits.crab.similarities import UserSimilarity
    #Build the similarity
    similarity = UserSimilarity(model, pearson_correlation)
    from sklearn.base import BaseEstimator
    from scikits.crab.recommenders.knn import UserBasedRecommender
    #build the user Based recommender
    recommender = UserBasedRecommender(model, similarity, with_preference=True)
    #recommend item for the user 5 (Toby)
    recomendations = recommender.recommend(5)
    pprint.pprint(recomendations)
    
    return 'List of ' + url_for('api_articles')

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

def test(articleid):
    return 'You are reading ' + articleid


if __name__ == '__main__':
    app.run(host= '0.0.0.0')