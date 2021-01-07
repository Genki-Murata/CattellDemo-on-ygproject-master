from django.db import models
from django.conf import settings

# 雇用形態マスタ
class M_employment_type(models.Model):
    employment_type_id = models.SmallIntegerField(primary_key=True)
    employment_type = models.CharField(max_length=100)
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employment_type

# 業種マスタ
class M_business_type(models.Model):
    business_type_id = models.SmallIntegerField(primary_key=True)
    business_type = models.CharField(max_length=100)
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_type

# 職種マスタ
class M_job_type(models.Model):
    job_type_id = models.SmallIntegerField(primary_key=True)
    job_type = models.CharField(max_length=100)
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_type

# 被験者基本情報
class Examinee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name_kana = models.CharField(max_length=50)
    first_name_kana = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.BooleanField(null=True, blank=True)
    final_education = models.CharField(max_length=100, null=True, blank=True)
    graduation = models.DateField(null=True, blank=True)
    last_career = models.CharField(max_length=100, null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)
    employment_type = models.ForeignKey(
        M_employment_type,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    duration = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    business_type = models.ForeignKey(
        M_business_type,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    job_type = models.ForeignKey(
        M_job_type,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    comment = models.CharField(max_length=200, null=True, blank=True)
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

# 診断結果マスタ
class M_result(models.Model):
    criteria = models.CharField(max_length=2, primary_key=True)
    item_no = models.SmallIntegerField()
    feature_group_id = models.SmallIntegerField()
    feature_group_top = models.CharField(max_length=20)
    feature_group_bottom = models.CharField(max_length=20)
    feature_detail_id = models.SmallIntegerField()
    feature_detail_top = models.CharField(max_length=20)
    feature_detail_bottom = models.CharField(max_length=20)
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.criteria

# 設問マスタ
class M_question(models.Model):
    question_id = models.SmallIntegerField(primary_key=True,)
    question = models.TextField(max_length=50)
    criteria = models.ForeignKey(M_result, on_delete=models.CASCADE)
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        id = str(self.question_id)
        return id

# 回答結果
class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(M_question, on_delete=models.CASCADE)
    answer = models.SmallIntegerField()
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

# 村田追加
# 回答結果(キャッテル)
class Cattell_Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.SmallIntegerField()
    answer = models.SmallIntegerField()
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

# 村田追加
# 回答結果(キャッテル一時保存用)
class Cattell_Answer_tmp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.SmallIntegerField()
    answer = models.SmallIntegerField()
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)



# 利用規約
class Terms(models.Model):
    item_no = models.IntegerField()
    display_flag = models.BooleanField(null=True, blank=True)
    terms = models.TextField(max_length=400)
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

# アクセス履歴
class L_access(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    ip_address = models.GenericIPAddressField()
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

# ワンタイムパスワード発行履歴
class L_issued_password(models.Model):
    issue_datetime = models.DateTimeField(primary_key=True)
    one_time_password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE)
    usage = models.BooleanField(null=True, blank=True)
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

# 判定型マスタ
class M_decision_type(models.Model):
    decision_type_id = models.CharField(max_length=3)
    decision_type = models.CharField(max_length=3)
    type_pattern = models.CharField(max_length=3)
    category_a = models.SmallIntegerField()
    category_b = models.SmallIntegerField()
    category_c = models.SmallIntegerField()
    category_d = models.SmallIntegerField()
    category_e = models.SmallIntegerField()
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.decision_type_id

# 診断結果
class Result(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    criteria = models.ForeignKey(
        M_result,
        on_delete=models.CASCADE,
    )
    point = models.SmallIntegerField(null=True, blank=True)
    percentile = models.SmallIntegerField(null=True, blank=True)
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

# 診断結果サマリ
class Result_summary(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    decision_type = models.ForeignKey(
        M_decision_type,
        on_delete=models.CASCADE,
    )
    points_category_e = models.SmallIntegerField()
    points_category_c = models.SmallIntegerField()
    points_category_a = models.SmallIntegerField()
    points_category_b = models.SmallIntegerField()
    points_category_d = models.SmallIntegerField()
    exam_date = models.DateField()
    delete_flag = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)