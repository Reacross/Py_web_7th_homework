import psycopg2


conn_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

# Запит перший: Знайти 5 студентів із найбільшим середнім балом з усіх предметів:
select_1 = """
    SELECT s.id, s.first_name, s.last_name, ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id, s.first_name, s.last_name
    ORDER BY average_grade DESC
    LIMIT 5;
    """

# Запит другий: Знайти студента із найвищим середнім балом з певного предмета (id предмета вказано для прикладу):
select_2 = """
    SELECT s.id, s.first_name, s.last_name, ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE g.subject_id = 39                             
    GROUP BY s.id, s.first_name, s.last_name
    ORDER BY average_grade DESC
    LIMIT 1;
"""

# Запит третій: Знайти середній бал у групах з певного предмета (id предмета вказано для прикладу):
select_3 = """
    SELECT grp.name AS group_name, ROUND(AVG(g.grade), 2) AS average_grade
    FROM groups grp
    JOIN students s ON grp.id = s.group_id
    JOIN grades g ON s.id = g.student_id
    WHERE g.subject_id = 37
    GROUP BY grp.name;
"""

# Запит четвертий: Знайти середній бал на потоці (по всій таблиці оцінок):
select_4 = """
    SELECT ROUND(AVG(grade), 2) AS average_grade
    FROM grades;
"""

# Запит п'ятий: Знайти які курси читає певний викладач (id викладача вказано для прикладу):
select_5 = """
    SELECT subj.name AS subject_name
    FROM subjects subj
    WHERE subj.teacher_id = 34;
"""

# Запит шостий: Знайти список студентів у певній групі (id групи вказано для прикладу):
select_6 = """
    SELECT s.id, s.first_name, s.last_name
    FROM students s
    WHERE s.group_id = 20;
"""

# Запит сьомий: Знайти оцінки студентів у окремій групі з певного предмета (id групи і предмета вказано для прикладу):
select_7 = """
    SELECT s.id, s.first_name, s.last_name, g.grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE s.group_id = 19 AND g.subject_id = 38;
"""

# Запит восьмий: Знайти середній бал, який ставить певний викладач зі своїх предметів (id викладача вказано для прикладу):
select_8 = """
    SELECT ROUND(AVG(grade), 2) AS average_grade
    FROM grades g
    JOIN subjects subj ON g.subject_id = subj.id
    WHERE subj.teacher_id = 31;
"""

# Запит дев'ятий: Знайти список курсів, які відвідує певний студент (id студента вказано для прикладу):
select_9 = """
    SELECT subj.name AS subject_name
    FROM subjects subj
    JOIN grades g ON subj.id = g.subject_id
    WHERE g.student_id = 199;
"""

# Запит десятий: Список курсів, які певному студенту читає певний викладач (id студента та викладача вказано для прикладу)
select_10 = """
    SELECT subj.name AS subject_name
    FROM subjects subj
    JOIN grades g ON subj.id = g.subject_id
    WHERE g.student_id = 185 AND subj.teacher_id = 34;
"""

def execute_query(query):
    try:
        
        connection = psycopg2.connect(**conn_params)
        cursor = connection.cursor()
        
        
        cursor.execute(query)
        
        
        rows = cursor.fetchall()
        
        
        for row in rows:
            print(row)
        
        
        cursor.close()
        connection.close()
        
    except (Exception, psycopg2.Error) as error:
        print("Помилка при роботі з PostgreSQL", error)

if __name__ == "__main__":
    
    # execute_query(select_1)
    # execute_query(select_2)
    # execute_query(select_3)
    # execute_query(select_4)
    # execute_query(select_5)
    # execute_query(select_6)
    # execute_query(select_7)
    # execute_query(select_8)
    # execute_query(select_9)
    execute_query(select_10)

