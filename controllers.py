from fastapi import FastAPI
from starlete.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI(
    title="FastAPIでつくるtoDoアプリケーション",
    description="FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリ",
    version='0.9 beta'
)

# new テンプレート関連の設定(Jinja2)
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env # Jinja2.Environment : filterやglobalの設定


def index(request: Request):
    return {"Hello": "World"}
