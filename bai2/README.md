3.2 Demosaicing

Cách chạy: cd vào thư mục bai2 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai2_demosaicing.py


- Giải thích: 
Thuật toán khử màu theo định hướng đồng nhất thích ứng (AHD) được sử dụng trong chương trình này để tái tạo lại hình ảnh đủ màu từ hình ảnh một kênh được chụp bằng Mảng bộ lọc màu (CFA). Thuật toán AHD bắt đầu bằng cách sao chép trực tiếp các giá trị kênh màu đỏ và màu xanh lam đã biết từ hình ảnh một kênh sang các kênh tương ứng của hình ảnh RGB. Tiếp theo, nó nội suy các giá trị kênh màu lục bị thiếu bằng cách lấy trung bình các pixel màu lục lân cận. Nếu một pixel màu lục bị thiếu, nó sẽ tính toán giá trị trung bình của các pixel màu lục xung quanh và gán giá trị đó cho pixel bị thiếu. Sau đó, thuật toán nội suy các giá trị kênh màu đỏ và màu xanh bị thiếu bằng cách lấy trung bình các pixel lân cận theo đường chéo. Nó tính toán giá trị trung bình của các giá trị màu đỏ (hoặc xanh lam) của các pixel cách hai bước theo cả chiều dọc và chiều ngang và gán giá trị đó cho pixel bị thiếu.

Thuật toán AHD nhằm mục đích duy trì tính đồng nhất của hình ảnh và giảm giả bằng cách sử dụng các đặc điểm hình ảnh cục bộ để nội suy. Nó cung cấp một sự cân bằng tốt giữa việc bảo tồn các chi tiết và giảm thiểu các tạo tác nội suy. Nhìn chung, thuật toán khử màu AHD giúp tái tạo lại hình ảnh đủ màu từ hình ảnh một kênh được chụp bằng CFA bằng cách nội suy hiệu quả thông tin màu bị thiếu và tạo ra kết quả đẹp mắt.

- Câu hỏi:
1. Máy ảnh của bạn có thực hiện ánh xạ tuyến tính đơn giản giữa các giá trị RAW và các giá trị cân bằng màu trong JPEG không? Một số máy ảnh cao cấp có chế độ RAW+JPEG, giúp việc so sánh này dễ dàng hơn nhiều?
+ Trả lời: Hầu hết các máy ảnh đều thực hiện ánh xạ tuyến tính đơn giản giữa các giá trị RAW và các giá trị cân bằng màu trong JPEG. Tuy nhiên, một số máy ảnh cao cấp cung cấp chế độ RAW+JPEG để ghi cả dữ liệu RAW và ảnh JPEG đã xử lý. Chế độ này cho phép chúng tôi so sánh hình ảnh RAW được khử màu với đầu ra JPEG của máy ảnh và đánh giá chất lượng của thuật toán khử màu.


- input: input_image2.jpg
- output: ảnh output.png đã khử màu.

