# Run with command: 'python -m app.scripts.create_database'

from sqlalchemy.engine import reflection
from sqlalchemy.schema import (
        MetaData,
        Table,
        DropTable,
        ForeignKeyConstraint,
        DropConstraint,
        )
from app import database
# Import of models is required for drop_all and create_all to work properly
from app import models

def drop_everything(db):
    # From http://www.sqlalchemy.org/trac/wiki/UsageRecipes/DropEverything

    conn=db.engine.connect()
    # the transaction only applies if the DB supports
    # transactional DDL, i.e. Postgresql, MS SQL Server
    trans = conn.begin()

    inspector = reflection.Inspector.from_engine(db.engine)
    # gather all data first before dropping anything.
    # some DBs lock after things have been dropped in 
    # a transaction.
    metadata = MetaData()

    tbs = []
    all_fks = []
    for table_name in inspector.get_table_names():
        fks = []
        for fk in inspector.get_foreign_keys(table_name):
            if not fk['name']:
                continue
            fks.append(
                ForeignKeyConstraint((),(),name=fk['name'])
                )
        t = Table(table_name,metadata,*fks)
        tbs.append(t)
        all_fks.extend(fks)

    for fkc in all_fks:
        conn.execute(DropConstraint(fkc))

    for table in tbs:
        conn.execute(DropTable(table))

    trans.commit()

# Drop old database, then make a new one.
print('Clearing current database...')
drop_everything(database)
print('Creating new database...')
database.create_all()
database.session.commit()
print("Database created.")