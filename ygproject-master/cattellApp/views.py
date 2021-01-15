from django.shortcuts import render

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
        return redirect(cattell_example,page_no)

    return render(request,template_name,context)


def cattell_break(request):
    template_name = "ygtestapp/cattell_break.html"
    return render(request,template_name)

