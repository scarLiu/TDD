from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
#home_page = None
# 现在使用Django render 函数，
# 而不是构建我们自己的HttpResponse。
# 它的第一个参数是请求，第二个参数要呈现的模板的名称。 Django将在应用程序目录中自动搜索名为templates的文件夹。
# 然后，它会根据模板的内容为您构建一个HttpResponse。
def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
