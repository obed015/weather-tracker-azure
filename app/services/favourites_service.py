import sqlite3
from typing import List, Dict
from app.config import Settings


class FavouritesService:
    def __init__(self, db_path: str | None = None):
        self.db_path = db_path or Settings.DB_PATH

    def get_all(self) -> List[Dict]:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, city_name, country, created_at
            FROM favourite_cities
            ORDER BY city_name ASC
            """
        )
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def add(self, city_name: str, country: str = "") -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR IGNORE INTO favourite_cities (city_name, country)
            VALUES (?, ?)
            """,
            (city_name.strip(), country.strip()),
        )

        conn.commit()
        conn.close()

    def delete(self, city_id: int) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM favourite_cities WHERE id = ?",
            (city_id,),
        )

        conn.commit()
        conn.close()
