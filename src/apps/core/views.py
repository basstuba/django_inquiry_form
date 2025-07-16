from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import CreateInquiryForm
from .models import Contact

GENDER_DISPLAY = {
    "1": "男性",
    "2": "女性",
    "3": "未回答"
}

CATEGORY_DISPLAY = {
    "1": "商品のお届けについて",
    "2": "商品の交換について",
    "3": "商品トラブル",
    "4": "ショップへのお問い合わせ",
    "5": "その他"
}

# css記述が終了したらコメントアウト解除
# @require_http_methods(["GET", "POST"])
def top_view(request):
    if request.method == "POST":
        form = CreateInquiryForm(request.POST)
        if form.is_valid(): # 保存せずにそのまま確認画面へ
            gender_label = GENDER_DISPLAY.get(form.cleaned_data['gender'])
            category_label = CATEGORY_DISPLAY.get(form.cleaned_data['category'])
            context = {
                'form': form,
                'gender_label': gender_label,
                'category_label': category_label,
            }
            return render(request, 'core/confirm.html', context)
    else:
        form = CreateInquiryForm()

    context = {
        'form': form,
        'gender_choices': Contact.GENDER_CHOICES,
        'category_choices': Contact.CATEGORY_CHOICES,
    }
    return render(request, 'core/top.html', context)


# @require_http_methods(["POST"])
def confirm_view(request):
    form = CreateInquiryForm(request.POST)
    if form.is_valid(): # ここで保存
        contact = form.save(commit=False)
        contact.tell = form.cleaned_data['tell']
        contact.save()
        return redirect('core:thanks')
    return redirect('core:top')


# @require_http_methods(["GET"])
def thanks_view(request):
    return render(request, 'core/thanks.html')


# @require_http_methods(["POST"])
def edit_view(request):
    form = CreateInquiryForm(request.POST)
    return render(request, 'core/top.html', {'form': form})