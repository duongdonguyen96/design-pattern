
# 🚀 SOLID

## 1. Khái niệm Dependency Injection (DI)
- **Dependency Injection (DI)** là một kỹ thuật trong lập trình giúp tách biệt việc khởi tạo và sử dụng các phụ thuộc (dependencies) của một đối tượng. Thay vì đối tượng tự tạo ra các phụ thuộc, chúng được "tiêm" từ bên ngoài, giúp mã nguồn dễ kiểm thử, mở rộng và bảo trì.
- **Các khái niệm liên quan:**
  - **Dependency:** Đối tượng hoặc thành phần mà một class cần để hoạt động.
  - **Inversion of Control (IoC):** Nguyên lý đảo ngược quyền kiểm soát việc khởi tạo phụ thuộc từ bên trong class sang bên ngoài.
  - **Service Container:** Thành phần quản lý và cung cấp các phụ thuộc.

## 1.1. DI nên dùng Interface
- Khi sử dụng DI, việc dùng **interface** giúp tách biệt logic triển khai và định nghĩa chức năng, tăng khả năng mở rộng, kiểm thử và thay thế các thành phần dễ dàng.
- **Ví dụ với interface (Python dùng abstract base class):**
```python
from abc import ABC, abstractmethod

class IEmailService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(IEmailService):
    def send(self, message):
        print(f"Sending email: {message}")

class UserController:
    def __init__(self, email_service: IEmailService):
        self.email_service = email_service
    def notify(self, msg):
        self.email_service.send(msg)
```

---

## 2. Ví dụ về DI
### a. Không áp dụng DI
```python
class EmailService:
    def send(self, message):
        print(f"Sending email: {message}")

class UserController:
    def __init__(self):
        self.email_service = EmailService()
    def notify(self, msg):
        self.email_service.send(msg)
```
### b. Áp dụng DI
```python
class EmailService:
    def send(self, message):
        print(f"Sending email: {message}")

class UserController:
    def __init__(self, email_service):
        self.email_service = email_service
    def notify(self, msg):
        self.email_service.send(msg)

# Khởi tạo bên ngoài
email_service = EmailService()
user_controller = UserController(email_service)
```
### Bảng so sánh ưu nhược điểm
| Tiêu chí           | Không áp dụng DI           | Áp dụng DI                |
|--------------------|---------------------------|---------------------------|
| Kiểm thử           | Khó kiểm thử              | Dễ kiểm thử               |
| Mở rộng            | Khó mở rộng               | Dễ mở rộng                |
| Phụ thuộc          | Gắn chặt                  | Lỏng lẻo                  |
| Bảo trì            | Khó bảo trì               | Dễ bảo trì                |


## 3. Khái niệm SOLID
- **SOLID** là tập hợp 5 nguyên lý thiết kế hướng đối tượng giúp mã nguồn dễ mở rộng, bảo trì, kiểm thử và giảm rủi ro lỗi.


## 4. Ví dụ về SOLID
### a. Không áp dụng SOLID
```python
class Report:
    def generate(self, data):
        # Tạo báo cáo
        print("Generating report...")
    def save_to_file(self, filename):
        # Lưu báo cáo
        print(f"Saving to {filename}")
```
- **Giải thích:** Class `Report` vi phạm nguyên lý Single Responsibility (SRP) vì vừa tạo báo cáo vừa lưu file.

### b. Áp dụng SOLID
```python
class ReportGenerator:
    def generate(self, data):
        print("Generating report...")

class ReportSaver:
    def save_to_file(self, report, filename):
        print(f"Saving to {filename}")
```
- **Giải thích:** Tách riêng hai trách nhiệm, tuân thủ nguyên lý SRP trong SOLID.

---

## Ví dụ minh họa từng nguyên lý SOLID

### 1. Single Responsibility Principle (SRP)
**Vi phạm:**
```python
class User:
    def save(self, data):
        # Lưu dữ liệu
        pass
    def send_email(self, msg):
        # Gửi email
        pass
```
**Đúng SOLID:**
```python
class UserRepository:
    def save(self, data):
        pass
class EmailService:
    def send_email(self, msg):
        pass
```
*Giải thích: Tách riêng từng trách nhiệm cho từng class.*

### 2. Open/Closed Principle (OCP)
**Vi phạm:**
```python
class Discount:
    def get(self, type):
        if type == "student": return 0.1
        elif type == "vip": return 0.2
```
**Đúng SOLID:**
```python
class Discount(ABC):
    @abstractmethod
    def get(self): pass
class StudentDiscount(Discount):
    def get(self): return 0.1
class VIPDiscount(Discount):
    def get(self): return 0.2
```
*Giải thích: Mở rộng bằng class mới, không sửa code cũ.*

### 3. Liskov Substitution Principle (LSP)
**Vi phạm:**
```python
class Bird:
    def fly(self): pass
class Ostrich(Bird):
    def fly(self): raise Exception("Ostrich can't fly")
```
**Đúng SOLID:**
```python
class Bird(ABC): pass
class FlyingBird(Bird):
    def fly(self): pass
class Sparrow(FlyingBird):
    def fly(self): print("Sparrow flying")
class Ostrich(Bird): pass
```
*Giải thích: Class con thay thế class cha mà không phá vỡ logic.*

---

## Giải thích rõ hơn về Liskov Substitution Principle (LSP)
- **LSP** yêu cầu các class con phải có thể thay thế class cha mà không làm thay đổi tính đúng đắn của chương trình. Điều này nghĩa là nếu một hàm sử dụng class cha, thì khi thay bằng class con, chương trình vẫn hoạt động đúng.
- **Ví dụ dễ hiểu:**
  - Giả sử có class `Bird` với phương thức `fly()`. Nếu bạn tạo class con `Ostrich` kế thừa từ `Bird` nhưng lại không bay được (hoặc ném lỗi), khi thay thế `Bird` bằng `Ostrich` sẽ gây lỗi cho chương trình. Đó là vi phạm LSP.
  - Để tuân thủ LSP, bạn nên phân loại lại:
```python
class Bird(ABC): pass
class FlyingBird(Bird):
    def fly(self): pass
class Sparrow(FlyingBird):
    def fly(self): print("Sparrow flying")
class Ostrich(Bird): pass  # Không có phương thức fly
```
*Giải thích: Khi thay thế `FlyingBird` bằng `Sparrow` chương trình vẫn đúng, còn `Ostrich` không bị ép phải bay.*

---

### 4. Interface Segregation Principle (ISP)
- **Khái niệm:** Interface Segregation Principle (ISP) yêu cầu không ép các class phải implement những phương thức mà chúng không sử dụng. Nên chia nhỏ interface theo từng chức năng thay vì gộp chung tất cả vào một interface lớn.

**Vi phạm ISP:**
```python
class IMachine(ABC):
    @abstractmethod
    def print(self): pass
    @abstractmethod
    def scan(self): pass

class OldPrinter(IMachine):
    def print(self): pass
    def scan(self): raise Exception("Can't scan")
```
*Giải thích: OldPrinter bị ép phải implement phương thức scan dù không dùng.*

**Đúng ISP:**
```python
class IPrinter(ABC):
    @abstractmethod
    def print(self): pass
class IScanner(ABC):
    @abstractmethod
    def scan(self): pass

class OldPrinter(IPrinter):
    def print(self): pass
```
*Giải thích: Tách interface, mỗi class chỉ implement chức năng cần thiết.*


### 5. Dependency Inversion Principle (DIP)
- **Khái niệm:**: Các module cấp cao không nên phụ thuộc trực tiếp vào module cấp thấp, mà nên phụ thuộc vào abstraction (interface).
**Vi phạm:**
```python
class LightBulb:
    def turn_on(self): pass
class Switch:
    def __init__(self):
        self.bulb = LightBulb()
    def operate(self):
        self.bulb.turn_on()
```
**Đúng SOLID:**
```python
class IBulb(ABC):
    @abstractmethod
    def turn_on(self): pass
class LightBulb(IBulb):
    def turn_on(self): pass
class Switch:
    def __init__(self, bulb: IBulb):
        self.bulb = bulb
    def operate(self):
        self.bulb.turn_on()
```
*Giải thích: Phụ thuộc vào abstraction, không phụ thuộc vào triển khai cụ thể.*

## Ví dụ DIP gần gũi, dễ hiểu
- **Ví dụ thực tế:**
  - Ổ cắm điện là abstraction, các thiết bị điện (quạt, tivi, máy sấy...) đều có thể cắm vào ổ cắm mà không cần biết chi tiết bên trong thiết bị.
  - Khi bạn thiết kế một ổ cắm, bạn chỉ cần đảm bảo nó cung cấp nguồn điện, còn thiết bị nào sử dụng nguồn đó là tuỳ ý.
```python
from abc import ABC, abstractmethod

class IDevice(ABC):
    @abstractmethod
    def turn_on(self): pass

class Fan(IDevice):
    def turn_on(self): print("Fan is running")

class TV(IDevice):
    def turn_on(self): print("TV is on")

class PowerSocket:
    def plug_in(self, device: IDevice):
        device.turn_on()

# Sử dụng
socket = PowerSocket()
socket.plug_in(Fan())
socket.plug_in(TV())
```
*Giải thích: Ổ cắm (PowerSocket) chỉ biết abstraction (IDevice), không phụ thuộc vào từng loại thiết bị cụ thể.*

### Ưu nhược điểm của SOLID
| Tiêu chí      | Ưu điểm                                 | Nhược điểm                |
|---------------|-----------------------------------------|---------------------------|
| Bảo trì       | Dễ bảo trì, sửa lỗi nhanh                | Đôi khi phức tạp hóa code |
| Mở rộng       | Dễ mở rộng, thêm tính năng mới           | Tốn thời gian thiết kế    |
| Kiểm thử      | Dễ kiểm thử từng thành phần              | Có thể sinh nhiều class   |
| Tái sử dụng   | Tăng khả năng tái sử dụng                | Yêu cầu hiểu rõ nguyên lý |

---
