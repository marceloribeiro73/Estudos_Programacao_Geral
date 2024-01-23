FROM ubuntu

RUN apt update -y && apt upgrade -y

RUN apt install python3 -y

COPY  ./square_root.py .

CMD ["python3", "square_root.py"]