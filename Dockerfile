FROM python:3.10

#WORKDIR fastrg

COPY . .

RUN pip install --root-user-action=ignore -r src/requirements.txt
#RUN pip-upgrader -p fastapi -p  SQLAlchemy -p  pydantic -p  uvicorn
#RUN pip install --root-user-action=ignore  -r src/requirements.txt
#criararquivorequirements

CMD [ "python", "-m", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0" ]