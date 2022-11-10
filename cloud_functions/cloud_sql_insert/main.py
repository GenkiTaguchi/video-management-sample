import functions_framework
import sqlalchemy
import os
# Set the following variables depending on your specific instance and database:
connection_name = os.environ.get('CONNECTION_NAME')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
table_name = os.environ.get('TABLE_NAME')
driver_name = 'postgres+pg8000'
query_string = dict(
    {"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})


@functions_framework.http
def insert(request):
    request_json = request.get_json(silent=True)
    table_field = ", ".join(request_json.keys())
    table_field_value = tuple(request_json.values())
    stmt = sqlalchemy.text(
        f'INSERT INTO {table_name} ({table_field}) VALUES {table_field_value}')

    db = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername=driver_name,
            username=db_user,
            password=db_password,
            database=db_name,
            query=query_string,
        ),
        pool_size=5,
        max_overflow=2,
        pool_timeout=30,
        pool_recycle=1800
    )
    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return f'Metadata {request_json} are successfully saved!!'
