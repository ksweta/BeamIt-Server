from beamit.app import app


class Profile(app.db.Model):
    email_id = app.db.Column(app.db.String(100), primary_key=True)
    name = app.db.Column(app.db.String(64))

    def __repr__(self):
        return "<Profile user_id: {}, name: {}>".format(
            self.email_id,
            self.name,
        )
