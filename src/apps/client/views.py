from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_safe
from .utils import get_filtered_contacts # 検索機能
from apps.core.models import Contact

import csv, logging


@login_required
@require_safe
def admin_view(request):
    contacts = Contact.objects.all().order_by('-created_at')
    paginator = Paginator(contacts, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'contacts': page_obj,
        'gender_choices': Contact.GENDER_CHOICES, # セレクトボックス用
        'category_choices': Contact.CATEGORY_CHOICES, # セレクトボックス用
    }

    return render(request, 'client/admin.html', context)


@login_required
@require_http_methods(["GET"])
def search_view(request):
    contacts = get_filtered_contacts(request.GET)

    paginator = Paginator(contacts, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    params = request.GET.copy()
    if 'page' in params:
        del params['page']
    get_params = "&" + params.urlencode() if params else ""
    context = {
        'contacts': page_obj,
        'get_params': get_params,
        'gender_choices': Contact.GENDER_CHOICES, # セレクトボックス用
        'category_choices': Contact.CATEGORY_CHOICES, # セレクトボックス用
    }

    return render(request, 'client/admin.html', context)


@login_required
@require_http_methods(["POST"])
def delete_view(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()

    return redirect('client:admin')


logger = logging.getLogger(__name__) # エクスポートのログを保存

@login_required
@require_http_methods(["GET"])
def export_view(request):
    contacts = get_filtered_contacts(request.GET)

    # csvヘッダーを持つHttpResponseオブジェクトの作成
    response = HttpResponse(
        content_type="text/csv",
        headers={ "Content-Disposition": 'attachment; filename="inquiry_list.csv"' },
    )

    # csvライターを初期化
    writer = csv.writer(response)

    # ヘッダー行の追加
    writer.writerow([
        "姓",
        "名",
        "性別",
        "メールアドレス",
        "電話番号",
        "住所",
        "建物名",
        "お問い合わせの種類",
        "お問い合わせ内容",
        "お問い合わせ日"
    ])

    # データ行の追加
    for contact in contacts:
        writer.writerow([
            contact.last_name,
            contact.first_name,
            contact.get_gender_display(),
            contact.email,
            contact.tell,
            contact.address,
            contact.building or '',
            contact.get_category_display(),
            contact.detail,
            contact.created_at.strftime('%Y-%m-%d %H:%M'),
        ])

    logger.info(f"{request.user} exported {contacts.count()} contact(s) at {timezone.now()}")

    return response