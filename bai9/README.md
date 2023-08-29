3.18 High-quality image resampling

Cách chạy: cd vào thư mục bai9 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai9_high_quality_image_resampling.py


Giải thích thuật toán dùng trong bài: 
+ Nearest neighbor:
    Thuật toán này chọn pixel gần nhất từ ảnh gốc để xác định giá trị pixel trong ảnh đã thay đổi kích thước. Đây là thuật toán đơn giản nhất và nhanh nhất nhưng có thể dẫn đến hiện tượng pixel hóa và mất chi tiết.

+ Bilinear (song tuyến tính):
    Phép nội suy song tuyến tính tính toán giá trị pixel trong hình ảnh đã thay đổi kích thước bằng cách lấy giá trị trung bình có trọng số của 4 pixel gần nhất từ hình ảnh gốc. Nó cung cấp kết quả mượt mà hơn so với phép nội suy lân cận gần nhất nhưng vẫn có thể bị mờ.

+ Windowed sinc:
    Thuật toán chân thành cửa sổ sử dụng bộ lọc thông thấp để giảm răng cưa và tạo ra kết quả chất lượng cao. Nó áp dụng một hàm chân thành có cửa sổ làm hạt nhân bộ lọc để kết hợp với hình ảnh trong quá trình thay đổi kích thước. Hàm chân thành là một hàm nội suy có giới hạn băng tần cung cấp khả năng tái tạo tín hiệu tuyệt vời. Cửa sổ giúp giảm hiện vật đổ chuông.

Trong mã, nhân bộ lọc được tạo bằng cách sử dụng hàm scipy.signal.firwin, hàm này xây dựng bộ lọc đáp ứng xung hữu hạn (FIR) với tần số cắt và loại cửa sổ được chỉ định (trong trường hợp này, cửa sổ Hamming được sử dụng).
Bằng cách áp dụng bộ lọc chân thành có cửa sổ, thuật toán bảo toàn hiệu quả các cạnh sắc nét và các chi tiết nhỏ trong hình ảnh đã thay đổi kích thước.
Chương trình cho phép bạn so sánh kết quả của các thuật toán khác nhau này bằng cách thay đổi kích thước hình ảnh đầu vào bằng nhiều bộ lọc khác nhau. Đầu ra được ghép nối hiển thị hình ảnh gốc và hình ảnh đã thay đổi kích thước bằng cách sử dụng từng thuật toán cạnh nhau để so sánh trực quan.

Hãy nhớ rằng việc lựa chọn thuật toán lấy mẫu lại phụ thuộc vào các yêu cầu cụ thể của ứng dụng của bạn, xem xét các yếu tố như tốc độ, chất lượng và mức độ bảo toàn chi tiết cần thiết.
- input: chantroi.jpg
- output: hình ảnh được thay đổi kích thước lớn hơn dùng các thuật toán nearest, window_sinc và bilinear
