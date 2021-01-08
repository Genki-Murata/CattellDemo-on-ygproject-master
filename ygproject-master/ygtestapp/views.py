from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth.decorators import login_required

def system_terms(request):
    template_name = "ygtestapp/system_terms.html"
    context = {
        "terms":models.Terms.objects.filter(display_flag=True, delete_flag=False),
    }
    return render(request, template_name, context)

def user_login(request):
    template_name = "ygtestapp/user_login.html"
    error_message = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(top)
        else:
            error_message = "ログインエラー"
    context = {
        "error_message":error_message,
    }
    return render(request, template_name, context)

def user_logout(request):
    logout(request)
    return redirect(user_login)

@login_required(login_url='/user_login/')
def top(request):
    user = request.user
    if user.clark_flag or user.system_flag:
        template_name = "ygtestapp/admin_menu.html"
    else:
        template_name = "ygtestapp/test_description.html"
    return render(request, template_name)

def test(request,page_no):
    template_name = "ygtestapp/test.html"
    q_cnt = 12
    q_cnt_per_page = 4
    start_id = (page_no - 1) * q_cnt_per_page + 1
    user = request.user
    page_no_str = str(page_no)
    if "answers" in request.session:
        answers = request.session["answers"]
    else:
        #村田メモ anwersリストを定義している（12個要素が入るようにしている）
        answers = [None] * q_cnt
    context = {
        "pre_page_no":page_no - 1,
        "current_page_no":page_no,
        "next_page_no":page_no + 1,
        "questions":models.M_question.objects.filter(question_id__range=[start_id, start_id + q_cnt_per_page - 1]),
        "answers":answers,
    }
    if request.method == "POST":
        # POSTメソッドの値をanswers代入
        for i in range(q_cnt_per_page):
            q_id_str = str(start_id + i)
            #村田メモ answersリストに回答結果を詰めている。
            answers[(page_no - 1) * q_cnt_per_page + i] = request.POST.get("q_" + q_id_str, None)
        # answersをセッションに保存
        request.session["answers"] = answers

        if request.POST["link_to"] == "検査を終了する":
            # 未回答項目がないか確認
            for answer in answers:
                if answer == None:
                     return redirect(test, page_no)
            # # 回答項目を登録
            questions = models.M_question.objects.all()
            for question in questions:
                answer = int(answers[question.question_id - 1])
                models.Answer.objects.create(
                    answer=answer,
                    question_id=question.question_id,
                    user_id=user.id
                )
            # return redirect(test_close)
            return redirect(cattell_detail,1)
        else:
            if request.POST["link_to"] == "<":
                page_no = page_no - 1
            elif request.method == "POST" and request.POST["link_to"] == ">":
                page_no = page_no + 1
            return redirect(test, page_no)

    return render(request, template_name, context)

def test_close(request):
    template_name = "ygtestapp/test_close.html"
    return render(request, template_name)

def participant_index(request):
    template_name = "ygtestapp/participant_index.html"
    context = {
        "participants":models.Examinee.objects.filter(delete_flag=False)
    }
    return render(request, template_name, context)

def participant_show(request, user_id):
    template_name = "ygtestapp/participant_show.html"
    context = {
        "participant":models.Examinee.objects.get(user_id=user_id),
        "answers":models.Answer.objects.filter(user_id=user_id),    
        #   {% comment %}▽▽ Murata ADD ▽▽{% endcomment %}        
        "cattell_answers":models.Cattell_Answer.objects.filter(user_id=user_id),        
    }
    return render(request, template_name, context)

#キャッテル_テスト前
def cattell_detail(request,page_no):
    template_name = "ygtestapp/cattell_detail.html"

    context = {
        "current_page_no":page_no,
    }

    return render(request,template_name,context)

#キャッテル_例題
def cattell_example(request,page_no):
    template_name = "ygtestapp/cattell_example.html"

    context = {
        "current_page_no":page_no,
        "current_page_no_formB":page_no - 4,         
        "next_page_no":page_no + 1,     
        
    }

    return render(request,template_name,context)    

#キャッテル_テスト    
def cattell_test(request,page_no):
    #固定値 (表示する問題数)
    q_cnt_per_page = 3
    #問題番号(例：1ページ目であれば"1"、2ページ目では"4")    
    start_id = (page_no - 1) * q_cnt_per_page + 1

    # 下記のテンプレートファイルを返す
    template_name = "ygtestapp/cattell_test.html"

    # current_page_no:現在のページ
    # current_page_no_formB:フォームB用ページ番号
    # next_page_no:次のページ
    context = {
        "current_page_no":page_no,
        "current_page_no_formB":page_no - 4, 
        "next_page_no":page_no + 1,
    }

    # POSTのリクエストが来た場合
    if request.method == "POST":

        # current_page_no:現在のページ番号
        # current_page_no_formB:フォームB用ページ番号        
        # next_page_no:次のページ番号

        context = {
                "current_page_no":page_no,
                "current_page_no_formB":page_no - 4,                
                "next_page_no":page_no + 1,            
        }        

        #一時テーブルに回答結果を保存する。
        # **************/
        # answer:回答結果
        # question:問題番号
        # user: ユーザID
        # **************/
        for i in range(q_cnt_per_page):
            models.Cattell_Answer_tmp.objects.create(
                answer=request.POST.get("mondai"+str(page_no)+"-"+str(i+1)),
                question=start_id+i,
                user=request.user
            )
        page_no = page_no + 1

        #フォームA検査4が終了したら休憩画面に遷移
        if page_no == 5:
            return redirect(cattell_break)
        #フォームB検査4が終了したらテスト終了画面に遷移
        if page_no == 9:
            # テスト終了時に一時テーブルから本テーブルに一括でINSERTする。
            cattell_tmp = models.Cattell_Answer_tmp.objects.filter(user_id=request.user).order_by('question')
            for cattell_tmps in cattell_tmp:                
                models.Cattell_Answer.objects.create(
                    answer=cattell_tmps.answer,
                    question = cattell_tmps.question,
                    user = cattell_tmps.user 
                )
            return redirect(test_close)


        # 次のページへ移行
        return redirect(cattell_test,page_no)

    return render(request,template_name,context)


def cattell_break(request):
    template_name = "ygtestapp/cattell_break.html"
    return render(request,template_name)
