import psycopg2

# Connect to your Supabase Postgres DB
conn = psycopg2.connect(
    host="db.wdpyzgcwxngzudnezvxa.supabase.co",
    database="postgres",
    user="postgres",
    password="Cokezero99123",  # Your DB password from Supabase settings
    port=5432,
    sslmode='require'
)

cursor = conn.cursor()

cursor.execute("""

    CREATE TABLE IF NOT EXISTS student (
        id SERIAL PRIMARY KEY,
        name VARCHAR(7) NOT NULL CHECK (name <> ''),
        major VARCHAR (20) DEFAULT 'undecided',
        grade INTEGER
    );
""")

cursor.execute("""
    INSERT INTO student (id, name, grade) VALUES (5,'', 97);
    INSERT INTO student VALUES (2, 'Kate', 'Sociology');
    INSERT INTO student VALUES (3, NULL, "Chemistry");
    INSERT INTO student VALUES (4, 'Jack', 'Biology);
    INSERT INTO student VALUES (5, 'Mike', 'Computer Science');
""")

cursor.execute("SELECT * FROM student;")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.commit()

