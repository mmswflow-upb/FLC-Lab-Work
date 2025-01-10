
import uuid
import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, request, redirect, render_template
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)
# Add CORS to app
cors = CORS(app)
# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://sql7756372:SmgLmiRQ6M@sql7.freesqldatabase.com/sql7756372"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable warnings
# Add SQLAlchemy to app
db = SQLAlchemy(app)

# Create class for a new table in the database
# Table Album with columns id-pk, band_name, genre, and album
class AlbumMohamadMario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(250), nullable=False)
    genre = db.Column(db.String(250), nullable=False)
    album = db.Column(db.String(250), nullable=False)

# Comment if you run the code more than once
with app.app_context():
    # Create table in db (call only once)
    db.create_all()
    # Commit changes
    db.session.commit()

# Route to main page; function to retrieve all data from the database
@app.route('/', methods=['GET', 'POST'])
def retrieveAll():
    try:
        # Query table Album
        albums = AlbumMohamadMario.query.all()
        holder = [{'id': i.id, 'band_name': i.band_name, 'genre': i.genre, 'album': i.album} for i in albums]
        # Return landing.html page-our home page
        return render_template('landing.html', holder=holder)
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Endpoint to add data to db
@app.route('/postData', methods=['POST'])
def postData():
    try:
        # Get values for bandName, genre, and album inputted by the user
        band_name = request.values.get('bandName')
        genre = request.values.get('genre')
        album = request.values.get('album')

        # Validate inputs
        if not band_name or not genre or not album:
            return "All fields are required.", 400

        # Create new record inside the table
        new_album = AlbumMohamadMario(band_name=band_name, genre=genre, album=album)
        db.session.add(new_album)
        db.session.commit()

        return redirect(url_for('retrieveAll'))
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Endpoint to delete data from db - deletes based on id
@app.route('/deleteData', methods=['POST'])
def deleteData():
    try:
        # Retrieve value for id inputted by the user
        album_id = request.values.get('id')
        if not album_id:
            return "ID is required.", 400

        # Delete record from db
        album_to_delete = AlbumMohamadMario.query.filter_by(id=album_id).first()
        if album_to_delete:
            db.session.delete(album_to_delete)
            db.session.commit()
        else:
            return "Record not found.", 404

        return redirect(url_for('retrieveAll'))
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Endpoint to update data in the db - updates based on id
@app.route('/update', methods=['POST'])
def updateData():
    try:
        # Retrieve values for id and updated fields
        album_id = request.values.get('id')
        new_band_name = request.values.get('bandName')
        new_genre = request.values.get('genre')
        new_album = request.values.get('album')

        if not album_id:
            return "ID is required.", 400

        # Update record in db
        album_to_update = AlbumMohamadMario.query.filter_by(id=album_id).first()
        if album_to_update:
            if new_band_name:
                album_to_update.band_name = new_band_name
            if new_genre:
                album_to_update.genre = new_genre
            if new_album:
                album_to_update.album = new_album
            db.session.commit()
        else:
            return "Record not found.", 404

        return redirect(url_for('retrieveAll'))
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)  # Use debug=True for development
