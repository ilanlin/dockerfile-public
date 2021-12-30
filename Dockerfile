FROM harbor.uat.cloudtogo.local/cloudtogo/python:2.7.18-alpine3.11
COPY . /workspace
WORKDIR /workspace/${SUBMODULE}
RUN pip install --no-cache-dir -r requirements.txt
RUN touch Dockerfile11.txt
CMD ["python", "./main.py"]
