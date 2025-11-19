from email.policy import default

from fastapi import  FastAPI
from pydantic import BaseModel

#데이터 유효성 검사와 설정 관리에 사용되는 라이브러리(모델링이 쉽고 강력함
from starlette.middleware.base import BaseHTTPMiddleware
#요청과 응답사이에 특정 작업 수행
#미들 웨어는 모든 요청에 대해 실행되며, 요청을 처리하기 전에 응답을 반환하기 전에 특정 작업을 수행할 수 있음
#예를 들어 로깅, 인증, cors처리, 압축등
import logging #로깅 처리용 메서드
class LoggingMiddleware(BaseHTTPMiddleware): #로그인 콘솔에 출력하는 용도 1개의 사용위치
    logging.basicConfig(level=logging.INFO) #로그 출력 추가
    async def dispatch(self, request, call_next) :
        logging.info(f"Req: {request.method}{request.url}")
        response = await call_next(request)
        logging.info(f"Status Code : {response.status_code}")
        return response

    app.add_middleware(LoggingMiddleware) #모든 요청에 대해 로그를 남기는 미들웨어 클래스를 사용함

    class Item(BaseModel): #아이템 객체생성(BaseModel:객체 연결->상속)1개의 사용 위치
        name : str         #상품명: 문자열
        description : str = None #상품설명: 문자열(null)
app = FastAPI(#앱의 시그니처와 환경설정을 담당) #java -> new FASTAPI();객체만듬
    title="MBC Ai study",
    description="MBC Ai study",
    version="0.0.1",
    docs_url = None,#http://localhost:8001/docs #보안상 None처리로
    redoc_url= None #http://localhost:8001/redoc #보안상 None처리로
)
class Item(BaseModel):
    name:str
    description:str=None
    price:float
    tax:float


@app.post("/items")  #웹 브라우저에 http://localhost:8001/ -> get요청시 처리
async def create_item(item: Item):
    #BaseModel은 데이터 모델링을 쉽게 도와주고 유효성검사도 수행
    #잘못된 데이터가 돌아오면 422qksghks
    return item

@app.get("/") ##http://localhost:8001/ ->get요청시 처리
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") #http://localhost:8001/items/1 ->\post요청시
async def read_item(item_id: int, q: str =None):
    return {"item_id": item_id, "q": q}
# item_id: 상품의 번호->경로 매개변수
#q: 쿼리 매개변수(기본값:none)

#podyman은 프론트가 없는 백엔드 테스트용 프로그램으로 활용
#서버실행은 uvicorn main;app --reload --port 8001
#         파이썬 백엔드 가동 서버로 main.py에 app이라는 메서드를 사용
#                            갱신      포트번호 변경 8001
