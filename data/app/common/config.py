from dataclasses import dataclass, asdict
from os import path, environ
import json

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True
    SECRET_FILE = path.join(path.dirname(path.dirname(path.abspath(__file__)))+"/database", 'secrets.json')
    secrets = json.loads(open(SECRET_FILE).read())
    DB = secrets["DB"]
   # DB_URL: str = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?useUniCode=yes&characterEncoding=UTF-8&serverTimezone=Asia/Seoul"
    DB_URL : str = "mysql+pymysql://root:j301##@j4a301.p.ssafy.io:3306/ssafy?charset=UTF-8"

@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True




@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))