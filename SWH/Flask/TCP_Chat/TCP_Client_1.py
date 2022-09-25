import socket
import threading
import json

def worker(conn):
    while True:
        s = int(Receive(conn, 4))
        body = json.loads(Receive(conn, s))
        print("[ " + body["id"] + " : " + body["value"] + " ]")
    conn.close()

def Receive(conn, len):
    data = conn.recv(len)
    s = data.decode()
    return s

def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 4000))
        print("클라이언트 소켓정보 : ", s)
        th = threading.Thread(target=worker, name="[스레드 이름 {}]".format(s), args=(s,))
        th.start()  # 생성한 스레드를 시작한다
        print("아이디 입력 : ", end="")
        id = input()
        while True:
            line = Input()
            s.send(lineLength(id, line).encode() + jsonDump(id, line).encode())  # 서버가 빈 데이터를 받고 연결을 종료할 수 있도록
            if not line: break  # 빈 데이터를 먼저 보낸 후 루프를 탈출

def lineLength(id, line):
    length = str(len(jsonDump(id, line).encode()))
    return length.zfill(4)

def jsonDump(id, line):
    dic = {'id' : id, 'value' : line}
    body = json.dumps(dic)
    return body

def Input():
    line = input()
    return line

if __name__ == '__main__':
    run()