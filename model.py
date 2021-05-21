from logger_demo.config import db

class db_app_log(db.Model):
    id = db.Column('id',db.Integer(),primary_key=True)
    log_level = db.Column('log_name',db.Integer())
    log_level_name = db.Column('log_level_name',db.String(40))
    log = db.Column('log',db.String(255))
    created_at = db.Column('created_at',db.String(60))



if __name__ == '__main__':
    db.create_all()


'''
CREATE TABLE DB_APP_LOG(
    ID INT AUTO_INCREMENT,
    LOG_LEVEL INT,
    LOG_LEVEL_NAME VARCHAR(40),
    LOG VARCHAR(255),
    CREATED_AT VARCHAR(60),
    PRIMARY KEY(id)
);

insert into db_app_log values(1,20,'','','')

'''