import uvicorn
from controler import app

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='localhost')