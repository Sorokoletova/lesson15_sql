import sqlite3
with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query_breed = """
               INSERT INTO breed (breed)
               SELECT DISTINCT breed
               FROM animals
               WHERE breed!=''
        """
    query_color1 = """
               INSERT INTO color1 (color1)
               SELECT DISTINCT color1
               FROM animals
               WHERE color1!=''
        """
    query_color2 = """
                   INSERT INTO color2 (color2)
                   SELECT DISTINCT color2
                   FROM animals
                   WHERE color2!=''
            """
    query_subtype = """
                       INSERT INTO subtype (outcome_subtype)
                       SELECT DISTINCT outcome_subtype
                       FROM animals
                       WHERE outcome_subtype!=''
                """
    query_condition = """
                        INSERT INTO outcome (outcome_type)
                        SELECT DISTINCT outcome_type
                        FROM animals
                        WHERE outcome_type!=''
                   """
    query_myanimals = """
                        INSERT INTO my_animals (index_animal, animal_type, animal_id, name_animal, age_upon_outcome, 
                        date_of_birth, outcome_month, outcome_year,breed, color1, color2, outcome_subtype, outcome_type)
                        SELECT "index", animal_type, animal_id, name, age_upon_outcome, date_of_birth, outcome_month, outcome_year, breed, color1, color2, outcome_subtype, outcome_type
                        FROM animals                      
                    """

# with sqlite3.connect("animal.db") as connection:
#     connection.row_factory = sqlite3.Row
#     query = connection.execute("""
#            SELECT *
#            FROM outcome""").fetchall()
#     for q in query:
#         value = dict(q)
#         connection.execute(f"""
#         UPDATE my_animals
#         SET idoutcome = {value["id"]}
#         WHERE outcome_type = '{value["outcome_type"]}'
#         """)


