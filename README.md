# 🚀 Django REST Framework Design Patterns

**Design Pattern là gì?**
Design Pattern (Mẫu thiết kế) là các giải pháp tối ưu, đã được kiểm chứng để giải quyết các vấn đề phổ biến trong phát triển phần mềm. Chúng giúp code dễ bảo trì, mở rộng, tái sử dụng và giảm lỗi.

**Cách dùng trong dự án Django/Django REST Framework:**
- Áp dụng các pattern để xây dựng API linh hoạt, dễ mở rộng, dễ bảo trì.
- Tăng khả năng tái sử dụng code giữa các module, giảm lặp lại.
- Giúp đội nhóm dễ thống nhất cách triển khai, dễ onboarding thành viên mới.

**Ưu điểm:**
- Tăng tính nhất quán, dễ bảo trì, mở rộng.
- Giảm lỗi, tăng khả năng tái sử dụng.
- Dễ áp dụng cho nhiều dự án khác nhau.

**Nhược điểm:**
- Có thể làm code phức tạp hơn nếu lạm dụng.
- Đòi hỏi hiểu biết về pattern để áp dụng đúng.
- Tăng số lượng class, file trong dự án.

**Ứng dụng thực tế:**
- Xây dựng API, service, workflow, quản lý trạng thái, kiểm soát truy cập, logging, notification, ...

## 📑 Table of Contents
- [🏗️ Creational Patterns](#creational-patterns)
  - [Singleton](#1-singleton)
  - [Factory Method](#2-factory-method)
  - [Builder](#3-builder)
  - [Prototype](#4-prototype)
  - [Abstract Factory](#5-abstract-factory)
- [🏛️ Structural Patterns](#structural-patterns)
  - [Adapter](#1-adapter)
  - [Decorator](#2-decorator)
  - [Facade](#3-facade)
  - [Proxy](#4-proxy)
  - [Composite](#5-composite)
  - [Bridge](#6-bridge)
- [🔄 Behavioral Patterns](#behavioral-patterns)
  - [Strategy](#1-strategy)
  - [Command](#2-command)
  - [Observer](#3-observer)
  - [Chain of Responsibility](#4-chain-of-responsibility)
  - [Mediator](#5-mediator)
  - [State](#6-state)
  - [Iterator](#7-iterator)
  - [Template Method](#8-template-method)
  - [Visitor](#9-visitor)
  - [Memento](#10-memento)
  - [Interpreter](#11-interpreter)
  - [Null Object](#12-null-object)

---

## 🏗️ Creational Patterns

### 1. Singleton
**Định nghĩa:** Đảm bảo một class chỉ có một instance duy nhất.

**Ví dụ tự code:**
```python
class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log = []
        return cls._instance
    def write(self, message):
        self.log.append(message)

logger1 = Logger()
logger2 = Logger()
logger1.write("Hello")
print(logger2.log)  # ['Hello']
```
**Ví dụ Django:** Django settings sử dụng Singleton để đảm bảo cấu hình chỉ được load một lần.
```python
from django.conf import settings
print(settings.DEBUG)
```
**Ưu điểm:**
- Tiết kiệm tài nguyên, dễ quản lý trạng thái toàn cục.
**Nhược điểm:**
- Khó test, dễ gây phụ thuộc.
**Ứng dụng:**
- Kết nối database, cấu hình hệ thống.

---

### 2. Factory Method
**Định nghĩa:** Tạo đối tượng mà không cần chỉ rõ class cụ thể.

**Ví dụ tự code:**
```python
class Animal:
    def speak(self): pass
class Dog(Animal):
    def speak(self): return "Woof!"
class Cat(Animal):
    def speak(self): return "Meow!"
class AnimalFactory:
    def create_animal(self, type):
        if type == "dog":
            return Dog()
        elif type == "cat":
            return Cat()
        else:
            return None

animal = AnimalFactory().create_animal("dog")
print(animal.speak())  # Woof!
```
**Ví dụ Django:**
```python
from django.db import connections
conn = connections['default']
```
**Ưu điểm:**
- Dễ mở rộng, giảm phụ thuộc.
**Nhược điểm:**
- Tăng số lượng class.
**Ứng dụng:**
- Tạo serializer, viewset động.

---

### 3. Builder
**Định nghĩa:** Tách quá trình xây dựng đối tượng phức tạp thành các bước nhỏ.

**Ví dụ tự code:**
```python
class User:
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
class UserBuilder:
    def __init__(self):
        self.user = User()
    def set_name(self, name):
        self.user.name = name
        return self
    def set_email(self, email):
        self.user.email = email
        return self
    def build(self):
        return self.user

user = UserBuilder().set_name("Alice").set_email("alice@example.com").build()
print(user.name, user.email)
```
**Ví dụ Django:**
```python
from django.forms import Form, CharField
class UserForm(Form):
    name = CharField()
    email = CharField()
```
**Ưu điểm:**
- Dễ kiểm soát quá trình tạo đối tượng.
**Nhược điểm:**
- Tăng độ phức tạp.
**Ứng dụng:**
- Tạo response phức tạp, xây dựng query.

---

### 4. Prototype
**Định nghĩa:** Tạo đối tượng mới bằng cách clone từ đối tượng gốc.

**Ví dụ tự code:**
```python
import copy
class Document:
    def __init__(self, content):
        self.content = content
    def clone(self):
        return copy.deepcopy(self)

original = Document("Hello")
cloned = original.clone()
cloned.content = "Hi!"
print(original.content)  # Hello
print(cloned.content)    # Hi!
```
**Ví dụ Django:**
```python
user_copy = User.objects.get(pk=1)
user_copy.pk = None
user_copy.save()
```
**Ưu điểm:**
- Tạo nhanh đối tượng tương tự.
**Nhược điểm:**
- Dễ lỗi nếu đối tượng phức tạp.
**Ứng dụng:**
- Tạo bản nháp, nhân bản dữ liệu.

---

### 5. Abstract Factory
**Định nghĩa:** Tạo nhóm đối tượng liên quan mà không cần chỉ rõ class cụ thể.

**Ví dụ tự code:**
```python
class SerializerFactory:
    def create(self, type):
        if type == "user":
            return UserSerializer()
        elif type == "product":
            return ProductSerializer()
class UserSerializer:
    pass
class ProductSerializer:
    pass
serializer = SerializerFactory().create("user")
print(type(serializer))
```
**Ví dụ Django:**
```python
from rest_framework import serializers, viewsets
class UserSerializer(serializers.ModelSerializer): ...
class UserViewSet(viewsets.ModelViewSet): ...
```
**Ưu điểm:**
- Dễ mở rộng, quản lý nhóm đối tượng.
**Nhược điểm:**
- Cấu trúc phức tạp.
**Ứng dụng:**
- Tạo API đa nền tảng.

---

## 🏛️ Structural Patterns

### 1. Adapter
**Định nghĩa:** Chuyển đổi interface của class thành interface khác.

**Ví dụ tự code:**
```python
class OldSystem:
    def get_data(self): return "old data"
class NewSystemAdapter:
    def __init__(self, old_system):
        self.old_system = old_system
    def fetch(self):
        return self.old_system.get_data()

adapter = NewSystemAdapter(OldSystem())
print(adapter.fetch())  # old data
```
**Ví dụ Django:**
```python
from rest_framework.renderers import JSONRenderer, XMLRenderer
```
**Ưu điểm:**
- Tái sử dụng code, tích hợp dễ dàng.
**Nhược điểm:**
- Tăng lớp trung gian.
**Ứng dụng:**
- Tích hợp hệ thống bên ngoài.

---

### 2. Decorator
**Định nghĩa:** Thêm chức năng cho đối tượng mà không thay đổi cấu trúc.

**Ví dụ tự code:**
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def say_hello():
    print("Hello!")

say_hello()
```
**Ví dụ Django:**
```python
from django.contrib.auth.decorators import login_required
@login_required
def my_view(request): ...
```
**Ưu điểm:**
- Dễ mở rộng, không thay đổi code gốc.
**Nhược điểm:**
- Khó debug.
**Ứng dụng:**
- Logging, kiểm tra quyền.

---

### 3. Facade
**Định nghĩa:** Cung cấp interface đơn giản cho hệ thống phức tạp.

**Ví dụ tự code:**
```python
class Database:
    def connect(self): print("Connected")
    def query(self, sql): print(f"Query: {sql}")
class DatabaseFacade:
    def __init__(self):
        self.db = Database()
    def get_users(self):
        self.db.connect()
        self.db.query("SELECT * FROM users")

facade = DatabaseFacade()
facade.get_users()
```
**Ví dụ Django:**
```python
from django.db import models
models.Model.objects.filter()
```
**Ưu điểm:**
- Dễ sử dụng, giảm phức tạp.
**Nhược điểm:**
- Giới hạn tính năng nâng cao.
**Ứng dụng:**
- API gateway, service layer.

---

### 4. Proxy
**Định nghĩa:** Đại diện cho đối tượng khác để kiểm soát truy cập.

**Ví dụ tự code:**
```python
class RealService:
    def request(self): return "data"
class AuthProxy:
    def __init__(self, service, user):
        self.service = service
        self.user = user
    def request(self):
        if self.user == "admin":
            return self.service.request()
        return "Access Denied"

proxy = AuthProxy(RealService(), "admin")
print(proxy.request())  # data
```
**Ví dụ Django:**
```python
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@method_decorator(login_required, name='dispatch')
class MyView(View): ...
```
**Ưu điểm:**
- Bảo mật, kiểm soát truy cập.
**Nhược điểm:**
- Tăng độ trễ.
**Ứng dụng:**
- Cache, kiểm tra quyền.

---

### 5. Composite
**Định nghĩa:** Quản lý đối tượng dạng cây.

**Ví dụ tự code:**
```python
class Component:
    def operation(self): pass
class Leaf(Component):
    def operation(self): return "Leaf"
class Composite(Component):
    def __init__(self): self.children = []
    def add(self, component): self.children.append(component)
    def operation(self):
        results = [child.operation() for child in self.children]
        return "+".join(results)

root = Composite()
root.add(Leaf())
root.add(Leaf())
print(root.operation())  # Leaf+Leaf
```
**Ví dụ Django:**
```python
from django.template import Template, Context
```
**Ưu điểm:**
- Dễ quản lý cấu trúc phức tạp.
**Nhược điểm:**
- Khó debug.
**Ứng dụng:**
- Menu, category.

---

### 6. Bridge
**Định nghĩa:** Tách abstraction và implementation.

**Ví dụ tự code:**
```python
class Renderer:
    def render(self, data): pass
class JSONRenderer(Renderer):
    def render(self, data): return f"JSON: {data}"
class View:
    def __init__(self, renderer): self.renderer = renderer
    def display(self, data): return self.renderer.render(data)

view = View(JSONRenderer())
print(view.display({"a": 1}))
```
**Ví dụ Django:**
```python
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
```
**Ưu điểm:**
- Dễ mở rộng, thay đổi implementation.
**Nhược điểm:**
- Tăng số lượng class.
**Ứng dụng:**
- Đa dạng hóa response.

---

## 🔄 Behavioral Patterns

### 1. Strategy
**Định nghĩa:** Thay đổi thuật toán động.

**Ví dụ tự code:**
```python
class SortStrategy:
    def sort(self, data): pass
class QuickSort(SortStrategy):
    def sort(self, data): return sorted(data)
class ReverseSort(SortStrategy):
    def sort(self, data): return sorted(data, reverse=True)
class Context:
    def __init__(self, strategy): self.strategy = strategy
    def sort(self, data): return self.strategy.sort(data)

context = Context(QuickSort())
print(context.sort([3,1,2]))  # [1,2,3]
```
**Ví dụ Django:**
```python
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
```
**Ưu điểm:**
- Dễ thay đổi hành vi.
**Nhược điểm:**
- Tăng số lượng class.
**Ứng dụng:**
- Sắp xếp, lọc dữ liệu.

---

### 2. Command
**Định nghĩa:** Đóng gói yêu cầu thành đối tượng.

**Ví dụ tự code:**
```python
class Command:
    def execute(self): pass
class PrintCommand(Command):
    def __init__(self, msg): self.msg = msg
    def execute(self): print(self.msg)
class Invoker:
    def __init__(self): self.commands = []
    def add_command(self, cmd): self.commands.append(cmd)
    def run(self):
        for cmd in self.commands:
            cmd.execute()

invoker = Invoker()
invoker.add_command(PrintCommand("Hello"))
invoker.add_command(PrintCommand("World"))
invoker.run()
```
**Ví dụ Django:**
```python
from django.core.management.base import BaseCommand
class MyCommand(BaseCommand):
    def handle(self, *args, **options): ...
```
**Ưu điểm:**
- Dễ undo/redo, log.
**Nhược điểm:**
- Tăng số lượng class.
**Ứng dụng:**
- Task queue, event.

---

### 3. Observer
**Định nghĩa:** Theo dõi và phản ứng khi trạng thái thay đổi.

**Ví dụ tự code:**
```python
class Subject:
    def __init__(self): self.observers = []
    def attach(self, observer): self.observers.append(observer)
    def notify(self, data):
        for obs in self.observers:
            obs.update(data)
class Observer:
    def update(self, data): print(f"Received: {data}")

subject = Subject()
subject.attach(Observer())
subject.notify("Hello")
```
**Ví dụ Django:**
```python
from django.db.models.signals import post_save
```
**Ưu điểm:**
- Tự động cập nhật.
**Nhược điểm:**
- Khó kiểm soát luồng.
**Ứng dụng:**
- Notification, audit.

---

### 4. Chain of Responsibility
**Định nghĩa:** Truyền request qua chuỗi handler.

**Ví dụ tự code:**
```python
class Handler:
    def __init__(self, successor=None): self.successor = successor
    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)
        return None
class AuthHandler(Handler):
    def handle(self, request):
        if request.get("auth"):
            return "Auth Success"
        return super().handle(request)
class LogHandler(Handler):
    def handle(self, request):
        print("Logging request")
        return super().handle(request)

chain = LogHandler(AuthHandler())
print(chain.handle({"auth": True}))
```
**Ví dụ Django:**
```python
from django.utils.deprecation import MiddlewareMixin
class MyMiddleware(MiddlewareMixin): ...
```
**Ưu điểm:**
- Dễ mở rộng, phân tách trách nhiệm.
**Nhược điểm:**
- Khó debug.
**Ứng dụng:**
- Xử lý request, validation.

---

### 5. Mediator
**Định nghĩa:** Quản lý giao tiếp giữa các đối tượng.

**Ví dụ tự code:**
```python
class Mediator:
    def __init__(self): self.colleagues = []
    def register(self, colleague): self.colleagues.append(colleague)
    def send(self, sender, message):
        for c in self.colleagues:
            if c != sender:
                c.receive(message)
class Colleague:
    def __init__(self, mediator): self.mediator = mediator; mediator.register(self)
    def send(self, message): self.mediator.send(self, message)
    def receive(self, message): print(f"Received: {message}")

m = Mediator()
c1 = Colleague(m)
c2 = Colleague(m)
c1.send("Hello")
```
**Ví dụ Django:**
```python
from django.forms import Form
```
**Ưu điểm:**
- Giảm phụ thuộc.
**Nhược điểm:**
- Tăng độ phức tạp.
**Ứng dụng:**
- Quản lý form, workflow.

---

### 6. State
**Định nghĩa:** Thay đổi hành vi dựa trên trạng thái.

**Ví dụ tự code:**
```python
class State:
    def handle(self): pass
class ActiveState(State):
    def handle(self): print("Active")
class InactiveState(State):
    def handle(self): print("Inactive")
class User:
    def __init__(self, state): self.state = state
    def request(self): self.state.handle()

user = User(ActiveState())
user.request()  # Active
user.state = InactiveState()
user.request()  # Inactive
```
**Ví dụ Django:**
```python
user.is_active
```
**Ưu điểm:**
- Dễ mở rộng trạng thái.
**Nhược điểm:**
- Tăng số lượng class.
**Ứng dụng:**
- Quản lý trạng thái đơn hàng.

---

### 7. Iterator
**Định nghĩa:** Duyệt qua phần tử của collection.

**Ví dụ tự code:**
```python
class MyIterator:
    def __init__(self, data): self.data = data; self.index = 0
    def __iter__(self): return self
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        raise StopIteration

for item in MyIterator([1,2,3]):
    print(item)
```
**Ví dụ Django:**
```python
for obj in queryset.iterator(): ...
```
**Ưu điểm:**
- Dễ duyệt dữ liệu.
**Nhược điểm:**
- Khó kiểm soát hiệu năng.
**Ứng dụng:**
- Phân trang, duyệt dữ liệu lớn.

---

### 8. Template Method
**Định nghĩa:** Định nghĩa skeleton của thuật toán.

**Ví dụ tự code:**
```python
class BaseView:
    def get(self):
        self.prepare()
        self.render()
    def prepare(self): print("Prepare data")
    def render(self): print("Render view")

class CustomView(BaseView):
    def prepare(self): print("Custom prepare")

view = CustomView()
view.get()
```
**Ví dụ Django:**
```python
from django.views.generic import TemplateView
```
**Ưu điểm:**
- Tái sử dụng code.
**Nhược điểm:**
- Khó tùy biến sâu.
**Ứng dụng:**
- Tạo view chuẩn hóa.

---

### 9. Visitor
**Định nghĩa:** Thêm thao tác cho đối tượng mà không thay đổi class.

**Ví dụ tự code:**
```python
class Element:
    def accept(self, visitor): visitor.visit(self)
class Visitor:
    def visit(self, element): print(f"Visited {element}")

e = Element()
v = Visitor()
e.accept(v)
```
**Ví dụ Django:**
```python
from django.db.migrations.operations import RunPython
```
**Ưu điểm:**
- Dễ mở rộng thao tác.
**Nhược điểm:**
- Tăng độ phức tạp.
**Ứng dụng:**
- Kiểm tra dữ liệu, migration.

---

### 10. Memento
**Định nghĩa:** Lưu trạng thái đối tượng để khôi phục.

**Ví dụ tự code:**
```python
class Memento:
    def __init__(self, state): self.state = state
class Originator:
    def __init__(self): self.state = None
    def set_state(self, state): self.state = state
    def save(self): return Memento(self.state)
    def restore(self, memento): self.state = memento.state

origin = Originator()
origin.set_state("A")
m = origin.save()
origin.set_state("B")
origin.restore(m)
print(origin.state)  # A
```
**Ví dụ Django:**
```python
from django.contrib.admin.models import LogEntry
```
**Ưu điểm:**
- Dễ khôi phục trạng thái.
**Nhược điểm:**
- Tốn bộ nhớ.
**Ứng dụng:**
- Undo, backup.

---

### 11. Interpreter
**Định nghĩa:** Xây dựng trình thông dịch cho ngôn ngữ riêng.

**Ví dụ tự code:**
```python
class Expression:
    def interpret(self): pass
class Number(Expression):
    def __init__(self, value): self.value = value
    def interpret(self): return self.value
class Add(Expression):
    def __init__(self, left, right): self.left = left; self.right = right
    def interpret(self): return self.left.interpret() + self.right.interpret()

expr = Add(Number(1), Number(2))
print(expr.interpret())  # 3
```
**Ví dụ Django:**
```python
from django.template import Template
```
**Ưu điểm:**
- Dễ mở rộng ngôn ngữ.
**Nhược điểm:**
- Khó debug.
**Ứng dụng:**
- Template, query DSL.

---

### 12. Null Object
**Định nghĩa:** Đối tượng không làm gì cả.

**Ví dụ tự code:**
```python
class NullLogger:
    def log(self, msg): pass

logger = NullLogger()
logger.log("This will do nothing")
```
**Ví dụ Django:**
```python
from django.core.cache import cache
cache = cache
```
**Ưu điểm:**
- Giảm kiểm tra null.
**Nhược điểm:**
- Dễ bỏ sót lỗi.
**Ứng dụng:**
- Logging, cache.

---

