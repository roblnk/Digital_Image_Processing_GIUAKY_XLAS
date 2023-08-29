3.7 Histogram equalization

Cách chạy: cd vào thư mục bai5 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai5_histogram_equalization.py


Giải thích: 
   Chương trình thực hiện cân bằng biểu đồ trên hình ảnh đầu vào, tăng cường phạm vi tông màu và làm cho nó ít nhạy cảm hơn với các cài đặt phơi sáng. Các bước tùy chọn như ánh xạ một phần pixel thành đen trắng thuần túy và giới hạn mức tăng cục bộ trong hàm truyền cũng được bao gồm. Xử lý trường hợp các giá trị màu bão hòa trong ảnh gốc. Nó lặp qua từng pixel trong hình ảnh màu và kiểm tra xem có bất kỳ kênh màu nào (R, G hoặc B) đã bão hòa hoàn toàn chưa (được cắt bớt ở 255 hoặc 0). Nếu một pixel có bất kỳ kênh bão hòa nào, thì pixel tương ứng trong hình ảnh đã cân bằng sẽ giữ nguyên giá trị màu ban đầu, thay vì bị sửa đổi thông qua cân bằng biểu đồ. Hình ảnh cân bằng được hiển thị cùng với hình ảnh gốc để so sánh.

- input: joker_batman.jpg
- output: giao diện Tkinter với ảnh input đã được cân băng màu

