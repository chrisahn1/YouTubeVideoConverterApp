import sqlite3


class ChannelDatabase:
    """Local database class that holds data."""

    locale = "youtube_channel.db"

    def __init__(self):
        """Initialize instance variables and creates connection to the database."""
        self.conn = sqlite3.connect(ChannelDatabase.locale)
        self.curr = self.conn.cursor()

    def create_tables(self):
        """Create the tables if they don't exist."""
        self.curr.execute('''CREATE TABLE IF NOT EXISTS locations (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL
                                )''')
        self.curr.execute('''CREATE TABLE IF NOT EXISTS animals (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                location_id INTEGER NOT NULL
                                )''')
        self.curr.execute('''CREATE TABLE IF NOT EXISTS observations (
                                id INTEGER PRIMARY KEY,
                                date TEXT NOT NULL,
                                temperature FLOAT NOT NULL,
                                location_id INTEGER NOT NULL,
                                animal_id INTEGER NOT NULL,
                                amount INTEGER
                                )''')
        self.conn.commit()


    def add_channel(self, channel_url):
        """Add a location to the database.
        Args:
            location_name (str): The location name.
        """
        self.curr.execute("INSERT INTO locations (name) VALUES (?)",
                          (channel_url,))
        self.conn.commit()


    def delete_channel(self, channel):
        """Delete a given location.
        Args:
            location (str): The name of the location to delete.
        """
        self.curr.execute("""
            SELECT id FROM locations WHERE name = ?
            """, (channel,))

        channel_id = (self.curr.fetchone())[0]

        self.curr.execute("""
            DELETE FROM observations
            WHERE observations.location_id = ?
            """, (channel_id,))
        self.curr.execute("""
            DELETE FROM animals
            WHERE animals.location_id = ?
            """, (channel_id,))
        self.curr.execute("""
            DELETE FROM locations
            WHERE locations.id = ?
            """, (channel_id,))
        self.conn.commit()



    def close(self):
        self.curr.close()
        self.conn.close()



