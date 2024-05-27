
class Config(object):
    APPLICATION_NAME = 'account-shield-storage-webapi'
    KEY_SALT = b'$2b$10$IHVrssCLQyKJAuQ46/FFJ.'

class OpNCSConfig(Config):
    DEBUG = True
    ENV = 'OP_NCS'
    ACCESS_KEY = '1A7I2TOWA2BTSNMXXVH5'
    SECRET_KEY = 'DJJ0TDWcF3kw2AgNLUqcBVKDmlGAR14rxCX9MIgj'
    ACCESS_TOKEN = 'bf8879b3b3375566d88b07856ecfe623'
    HASHED_ACCESS_KEY = b'$2b$10$IHVrssCLQyKJAuQ46/FFJ./mz6C7bIkZLh.Pa2g2FkyylDMHBuj8m'
    HASHED_SECRET_KEY = b'$2b$10$IHVrssCLQyKJAuQ46/FFJ.AsMYQ/ijDYKwu7l8M0Bm0f7x.nIBotu'
    ACCOUNT_SHILED_BUCKET_NAME = 'account-shield'
    STATUS_2_PURGE_UPLOAD_PATH = 'status_2_upload'
    S3_ENDPOINT = 'https://baobab.ncsoft.com'

class RcNCSConfig(Config):
    DEBUG = False
    ENV = 'RC_NCS'
    ACCESS_KEY = '1X68YX0EAQQ6744LZA3Q'
    SECRET_KEY = 'RwppXgwDqCDoNG6Rc8spuRxz7vkE0m7zGugWPYzO'
    ACCESS_TOKEN = 'bf8879b3b3375566d88b07856ecfe623'
    HASHED_ACCESS_KEY = b'$2b$10$IHVrssCLQyKJAuQ46/FFJ./mz6C7bIkZLh.Pa2g2FkyylDMHBuj8m'
    HASHED_SECRET_KEY = b'$2b$10$IHVrssCLQyKJAuQ46/FFJ.AsMYQ/ijDYKwu7l8M0Bm0f7x.nIBotu'
    ACCOUNT_PURGE_BUCKET_NAME = 'account-shield'
    CHILDREN__GAMEPLAY_REPORT_BUCKET_NAME = 'children-gameplay-report'
    CHILDREN__GAMEPLAY_REPORT_UPLOAD_PATH = 'children-gameplay-report-rc'
    NOTIFY_UPLOAD_PATH = 'notify_upload_rc'
    NOTIFY_READ_COMPLETE_PATH = 'notify_read_complete_rc'
    NOTIFY_ERROR_PATH = 'notify_error_rc'
    PURGE_UPLOAD_PATH = 'purge_upload_rc'
    STATUS_2_PURGE_UPLOAD_PATH = 'status_2_upload_rc'
    MASS_PURGE_UPLOAD_PATH = 'mass_purge_upload_rc'
    TW_REACTIVATE_UPLOAD_PATH = 'tw_reactivate_upload_rc'
    TOONILAND_PURGE_UPLOAD_PATH = 'tooniland_rc'
    PURGE_READ_COMPLETE_PATH = 'purge_read_complete_rc'
    PURGE_ERROR_PATH = 'purge_error_rc'
    S3_ENDPOINT = 'http://hugo.cloud.ncsoft'

class SandboxNCSConfig(Config):
    DEBUG = False
    ENV = 'SANDBOX_NCS'
    ACCESS_KEY = '1A7I2TOWA2BTSNMXXVH5'
    SECRET_KEY = 'DJJ0TDWcF3kw2AgNLUqcBVKDmlGAR14rxCX9MIgj'
    ACCESS_TOKEN = 'bf8879b3b3375566d88b07856ecfe623'
    HASHED_ACCESS_KEY = b'$2b$10$IHVrssCLQyKJAuQ46/FFJ./mz6C7bIkZLh.Pa2g2FkyylDMHBuj8m'
    HASHED_SECRET_KEY = b'$2b$10$IHVrssCLQyKJAuQ46/FFJ.AsMYQ/ijDYKwu7l8M0Bm0f7x.nIBotu'
    ACCOUNT_PURGE_BUCKET_NAME = 'account-shield'
    CHILDREN__GAMEPLAY_REPORT_BUCKET_NAME = 'children-gameplay-report'
    CHILDREN__GAMEPLAY_REPORT_UPLOAD_PATH = 'children-gameplay-report'
    NOTIFY_UPLOAD_PATH = 'notify_upload'
    NOTIFY_READ_COMPLETE_PATH = 'notify_read_complete'
    NOTIFY_ERROR_PATH = 'notify_error'
    PURGE_UPLOAD_PATH = 'purge_upload'
    STATUS_2_PURGE_UPLOAD_PATH = 'status_2_upload'
    MASS_PURGE_UPLOAD_PATH = 'mass_purge_upload'
    TW_REACTIVATE_UPLOAD_PATH = 'tw_reactivate_upload'
    TOONILAND_PURGE_UPLOAD_PATH = 'tooniland'
    PURGE_READ_COMPLETE_PATH = 'purge_read_complete'
    PURGE_ERROR_PATH = 'purge_error'
    S3_ENDPOINT = 'https://baobab.ncsoft.com'

class LiveNCSConfig(Config):
    DEBUG = True
    ENV = 'LIVE_NCS'
    ACCESS_KEY = '1X68YX0EAQQ6744LZA3Q'
    SECRET_KEY = 'RwppXgwDqCDoNG6Rc8spuRxz7vkE0m7zGugWPYzO'
    ACCESS_TOKEN = '8f61fea4bef21bdfeca72a9acdfc6fd4'
    HASHED_ACCESS_KEY = b'$2b$10$IHVrssCLQyKJAuQ46/FFJ./mz6C7bIkZLh.Pa2g2FkyylDMHBuj8m'
    HASHED_SECRET_KEY = b'$2b$10$IHVrssCLQyKJAuQ46/FFJ.AsMYQ/ijDYKwu7l8M0Bm0f7x.nIBotu'
    ACCOUNT_PURGE_BUCKET_NAME = 'account-shield'
    CHILDREN__GAMEPLAY_REPORT_BUCKET_NAME = 'children-gameplay-report'
    CHILDREN__GAMEPLAY_REPORT_UPLOAD_PATH = 'children-gameplay-report-live'
    NOTIFY_UPLOAD_PATH = 'notify_upload_live'
    NOTIFY_READ_COMPLETE_PATH = 'notify_read_complete_live'
    NOTIFY_ERROR_PATH = 'notify_error_live'
    PURGE_UPLOAD_PATH = 'purge_upload_live'
    STATUS_2_PURGE_UPLOAD_PATH = 'status_2_upload_live'
    MASS_PURGE_UPLOAD_PATH = 'mass_purge_upload_live'
    TW_REACTIVATE_UPLOAD_PATH = 'tw_reactivate_upload_live'
    TOONILAND_PURGE_UPLOAD_PATH = 'tooniland_live'
    PURGE_READ_COMPLETE_PATH = 'purge_read_complete_live'
    PURGE_ERROR_PATH = 'purge_error_live'
    S3_ENDPOINT = 'http://hugo.cloud.ncsoft'

appConfig = {
        'op_ncs' : OpNCSConfig,
        'rc_ncs' : RcNCSConfig,
        'sadbox_ncs' : SandboxNCSConfig,
        'live_ncs' : LiveNCSConfig
        }
