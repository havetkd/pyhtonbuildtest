FROM python as build
WORKDIR /install
COPY ./requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM python:slim
WORKDIR /testpyhton
COPY --from=build /install /usr/local
COPY ./*.py ./
EXPOSE 8000


ENTRYPOINT ["uvicorn", "app:app", "--reload", "--host=0.0.0.0", "--port=8015"]
