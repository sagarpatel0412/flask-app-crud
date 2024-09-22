from flask import Flask, jsonify, render_template
import requests
from app.model import db
from app.routes import user_bp
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()



def create_app():
    app = Flask(__name__)
    CORS(app)


    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['DEBUG'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True


    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        print("Home route accessed")
        return render_template('index.html')

    @app.route('/about')
    def about():
        print("Home route accessed")
        return render_template('about.html')

    @app.route('/blog')
    def blog():
        print("Home route accessed")
        return render_template('blog.html')

    @app.route('/blog-single')
    def blogSingle():
        print("Home route accessed")
        return render_template('blog-single.html')

    @app.route('/contact')
    def contact():
        print("Home route accessed")
        return render_template('contact.html')

    @app.route('/restaurant')
    def restaurent():
        print("Home route accessed")
        return render_template('restaurant.html')

    @app.route('/rooms-single')
    def roomsSingle():
        print("Home route accessed")
        return render_template('rooms-single.html')

    @app.route('/rooms')
    def rooms():
        print("Home route accessed")
        return render_template('rooms.html')

    @app.route('/fetch-products')
    def fetch_products():
        url = 'https://dummyjson.com/products'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Something went wrong'}), 500


    app.register_blueprint(user_bp,url_prefix='/api/v1')

    return app
