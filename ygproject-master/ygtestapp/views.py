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

