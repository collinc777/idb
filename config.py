# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

SQLALCHEMY_DATABASE_URI = 'postgres://swe16:swe16idb@idbtest.cevmyqqxetxv.us-west-2.rds.amazonaws.com:5432/Swe16db'

# Uncomment the line below if you want to work with a local DB
# SQLALCHEMY_DATABASE_URI = 'postgres:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True

# If set to True, Flask-SQLAlchemy will track modifications of objects and emit signals. 
# The default is None, which enables tracking but issues a warning that it will be disabled 
# by default in the future. This requires extra memory and should be disabled if not needed.
SQLALCHEMY_TRACK_MODIFICATIONS = False

