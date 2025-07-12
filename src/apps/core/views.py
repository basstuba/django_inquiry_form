from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import CreateInquiryForm
from .models import Contact

# css記述が終了したらコメントアウト解除
# @require_http_methods(["GET", "POST"])
def top_view(request):
    if request.method == "POST":
        form = CreateInquiryForm(request.POST)
        if form.is_valid(): # 保存せずにそのまま確認画面へ
            return render(request, 'core/confirm.html', {'form': form})
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