from sqlalchemy import create_engine, MetaData, inspect

engine = create_engine("mysql+pymysql://root:root@localhost:3306/bigbrew")
meta = MetaData()
conn = engine.connect()
inspect = inspect(engine)