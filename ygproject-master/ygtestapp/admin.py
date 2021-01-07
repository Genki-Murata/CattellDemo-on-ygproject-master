from django.contrib import admin
from .models import (
    M_employment_type,
    M_business_type,
    M_job_type,
    Examinee,
    M_result,
    M_question,
    Answer,
    Terms,
    L_access,
    L_issued_password,
    M_decision_type,
    Result,
    Result_summary,
    Cattell_Answer,
    Cattell_Answer_tmp,
)

admin.site.register(M_employment_type)
admin.site.register(M_business_type)
admin.site.register(M_job_type)
admin.site.register(Examinee)
admin.site.register(M_result)
admin.site.register(M_question)
admin.site.register(Answer)
admin.site.register(Terms)
admin.site.register(L_access)
admin.site.register(L_issued_password)
admin.site.register(M_decision_type)
admin.site.register(Result)
admin.site.register(Result_summary)
admin.site.register(Cattell_Answer)
admin.site.register(Cattell_Answer_tmp)
