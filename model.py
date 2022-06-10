from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    
    Game.query.delete()

    #Add sample games
    g1 = Game(name="Trivia", description="Ask questions and get answers")
    g2 = Game(name="Charades", description="Act out the word")

    db.session.add_all([g1, g2])
    db.session.commit()

if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
