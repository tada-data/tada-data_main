from flask import Flask, render_template, url_for, request, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/board")
def board():
    return render_template("board.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        id = request.form["username"]
        pw = request.form["password"]
        if id=="tiger" and pw=="1111":
            session["id"]=id
            # 회원임을 증명할 수 있는 전역변수 필요
            # session에 정보를 저장해서 얘가 회원이라는 것을 표시할 수 있도록
            # 회원이다 아니다 표시해주는 session에 파트를 만들어서 그 부분이 저장되면 login이 된 것으로 처리되도록
            # id와 pw가 일치하면 session에 어떤 값이 저장이 되도록
            # 보통 id로 저장되게 하는 것이 쓸모가 많음
            return render_template("index.html")
            # 아니면 redirect 써도 됨
            # session을 쓰기 위해서는 secret_key를 반드시 지정
            
            # 로그인을 하고 나서는 로그인 탭을 로그아웃으로 바꾸고 회원 이름으로 바뀌도록
        else:
            return render_template("login.html", msg=True)
        # 원래 DB로 연결해서 id와 pw가 맞는지 확인해야 하지만 지금은 조건문으로 처리    
    # 이렇게 조건문으로 처리하거나 아니면 route method post인 것 따로 만들어서 설정

@app.route("/logout")
def logout():
    session["id"] = False
    return render_template("index.html")
    # del로 하면 id라는 변수 자체가 삭제되어서 예외가 발생할 수 있으므로
    # 변수 자체를 삭제하는 것보다 false로 집어넣어서 변수가 걸리도록
    # false or None 이렇게 넣어주면 됨

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.secret_key = "abcd#$%"
    # 실행하기 전에만 설정이 되면 됨(+session["id"]=id 가 실행되기 전에)
    # 보통 기본적인 환경설정을 여기서 함
    # 처음 실행할 때 여기부터 시작 >> 그래서 환경설정으로 바꾸기  
    app.run(debug=True, host="0.0.0.0")
    # 정식으로 올리기 위해 host 0.0.0.0으로 설정
    # 외부 인터넷과 연결하는 방법인 듯

    # 디자인 다운 받은 페이지(부트스트랩):https://getbootstrap.com/docs/5.2/components/carousel/