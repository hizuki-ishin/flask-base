FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
ADD . /usr/src/app/
# sampleファイルをadd
ADD flask_sample.py ./usr/src/app/

# 実行 (本番環境)
#CMD ["gunicorn", "flask_sample:app", "-b", ":5000"]
# 実行 (デバッグ環境)
CMD ["python", "flask_sample.py"]
