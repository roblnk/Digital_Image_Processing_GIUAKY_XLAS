3.10 Seperable Filters

Cách chạy: cd vào thư mục bai6 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai6_separable_filters.py


Giải thích: 
+ Để triển khai kỹ thuật của Pietro Perona để xấp xỉ tích chập dưới dạng tổng của các hạt nhân có thể tách rời, bạn có thể sửa đổi hàm xấp xỉ_convolution. Hàm lấy một hình ảnh và danh sách các hạt nhân có thể tách rời làm đầu vào và thực hiện tích chập bằng cách sử dụng từng hạt nhân. Sau đó, nó tổng hợp các hình ảnh được tích hợp để tạo ra một hình ảnh gần đúng của hình ảnh gốc.

+ Để đo độ trung thực gần đúng, bạn có thể sử dụng nhiều số liệu khác nhau như lỗi bình phương trung bình (MSE) hoặc tỷ lệ tín hiệu trên nhiễu cao nhất (PSNR). Các số liệu này so sánh hình ảnh gần đúng với hình ảnh gốc để xác định chất lượng của hình ảnh gần đúng. Bạn có thể tính toán các số liệu này bằng cách so sánh giá trị pixel của hai hình ảnh.
- input: darkroom.jpg
- output: giao diện Tkinter với ảnh input đã được lọc separable

