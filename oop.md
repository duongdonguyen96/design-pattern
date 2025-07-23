# 🚀 Object-Oriented Programming

**OOP (Object-Oriented Programming)** là phương pháp lập trình dựa trên khái niệm "đối tượng" (object), trong đó mỗi đối tượng là một thực thể có trạng thái (thuộc tính) và hành vi (phương thức). OOP giúp mô hình hóa các thực thể trong thế giới thực vào chương trình, tăng tính tổ chức, dễ bảo trì và mở rộng.

**Các tính chất của OOP:**
1. **Tính đóng gói (Encapsulation):**
   - Đóng gói dữ liệu và các phương thức thao tác dữ liệu vào cùng một đối tượng, che giấu chi tiết bên trong đối tượng với bên ngoài.
   - *Ví dụ lời:* Một chiếc điện thoại có các chức năng gọi, nhắn tin, nhưng người dùng không cần biết chi tiết bên trong hoạt động thế nào.
   - *Ví dụ code Python:*
     ```python
     class Phone:
         def __init__(self, number):
             self.__number = number  # thuộc tính private
         def call(self, to_number):
             print(f"Gọi từ {self.__number} đến {to_number}")
     phone = Phone("0123456789")
     phone.call("0987654321")
     ```
2. **Tính kế thừa (Inheritance):**
   - Cho phép lớp con kế thừa thuộc tính và phương thức từ lớp cha, giúp tái sử dụng mã nguồn.
   - *Ví dụ lời:* Xe máy và ô tô đều là phương tiện giao thông, có thể kế thừa các thuộc tính chung như tốc độ, màu sắc.
   - *Ví dụ code Python:*
     ```python
     class Vehicle:
         def __init__(self, color):
             self.color = color
         def move(self):
             print("Di chuyển...")
     class Car(Vehicle):
         def move(self):
             print("Ô tô di chuyển...")
     car = Car("đỏ")
     car.move()
     ```
3. **Tính đa hình (Polymorphism):**
   - Cho phép đối tượng có thể thực hiện các hành động khác nhau tùy vào ngữ cảnh.
   - *Ví dụ lời:* Cùng một phương thức "move", nhưng xe máy và ô tô có cách di chuyển khác nhau.
   - *Ví dụ code Python:*
     ```python
     class Animal:
         def speak(self):
             pass
     class Dog(Animal):
         def speak(self):
             print("Gâu gâu")
     class Cat(Animal):
         def speak(self):
             print("Meo meo")
     animals = [Dog(), Cat()]
     for animal in animals:
         animal.speak()
     ```
4. **Tính trừu tượng (Abstraction):**
   - Ẩn đi chi tiết cài đặt, chỉ hiển thị những gì cần thiết.
   - *Ví dụ lời:* Người dùng chỉ cần biết sử dụng remote để bật tivi, không cần biết bên trong remote hoạt động thế nào.
   - *Ví dụ code Python:*
     ```python
     from abc import ABC, abstractmethod
     class Remote(ABC):
         @abstractmethod
         def turn_on(self):
             pass
     class TVRemote(Remote):
         def turn_on(self):
             print("Bật tivi")
     remote = TVRemote()
     remote.turn_on()
     ```

- Nêu ưu điểm, nhược điểm của OOP

**Ưu điểm:**
- Dễ bảo trì, mở rộng nhờ tính đóng gói và kế thừa.
- Tái sử dụng mã nguồn.
- Dễ mô hình hóa các bài toán thực tế.
- Tăng tính bảo mật dữ liệu nhờ che giấu thông tin.

**Nhược điểm:**
- Có thể phức tạp, tốn thời gian thiết kế ban đầu.
- Đôi khi hiệu suất thấp hơn so với lập trình thủ tục do phải quản lý nhiều đối tượng.
- Không phù hợp với các bài toán đơn giản, xử lý tuần tự.

**Khi nào dùng OOP:**
- Khi bài toán cần mô hình hóa các thực thể, có nhiều trạng thái và hành vi.
- Khi cần mở rộng, bảo trì lâu dài.
- Ví dụ: Xây dựng hệ thống quản lý, game, phần mềm lớn.

