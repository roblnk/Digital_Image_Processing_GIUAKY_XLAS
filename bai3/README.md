3.4 Blue Screen Matting

Cách chạy: cd vào thư mục bai3 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai3_green_or_blue_screen_matting.py


- Giải thích: 
    + Variable Number of Gradients (VNG) là một thuật toán phổ biến để khử màu cho các hình ảnh mẫu của Bayer. Nó hoạt động bằng cách ước tính thông tin màu còn thiếu dựa trên thông tin độ dốc có trong ảnh. Ý tưởng cơ bản đằng sau thuật toán VNG là sử dụng thực tế là các pixel lân cận trong cùng một kênh màu có độ dốc cường độ tương tự nhau. Do đó, thuật toán ước tính các giá trị màu bị thiếu bằng cách xem độ dốc cường độ của các pixel lân cận và sử dụng thông tin này để nội suy các giá trị bị thiếu, điều này làm cho thuật toán thích ứng hơn với các nội dung hình ảnh và mức độ nhiễu khác nhau, dựa trên sự khác biệt về cường độ giữa các pixel lân cận. Các độ dốc này sau đó được sử dụng để ước tính các giá trị màu còn thiếu cho mỗi pixel trong hình ảnh mẫu của Bayer.

    + Ta thay đổi kích thước hình nền để phù hợp với kích thước của hình nền trước bằng cách sử dụng cv2.resize. Tiếp theo, chúng ta chuyển đổi alpha matte thành mặt nạ bằng cách sử dụng ngưỡng với cv2.threshold và đảo ngược mặt nạ bằng cách sử dụng cv2.bitwise_not.

    + Sau đó, chúng ta chuyển đổi hình ảnh nền trước và nền thành biểu diễn dấu phẩy động bằng cách sử dụng astype(float). Chúng ta áp dụng hiệu ứng mờ alpha cho nền trước và nền sau bằng cách sử dụng phép nhân theo từng phần tử với cv2.multiply.

    + Cuối cùng, chúng ta kết hợp nền trước và nền sau bằng cv2.add và lưu kết quả bằng cv2.imwrite.

Thuật toán VNG đã được chứng minh là tạo ra kết quả chất lượng cao, đặc biệt đối với hình ảnh có độ nhiễu thấp và độ sắc nét cao. Tuy nhiên, nó có thể tương đối chậm so với các thuật toán giải mã khác do độ phức tạp tính toán của nó.

- Câu hỏi:
1. Hầu hết các ảnh đã chụp đều được áp dụng hiệu chỉnh gamma. Điều này có làm mất hiệu lực phương trình tổng hợp cơ bản (3.8); nếu vậy, làm thế nào nó nên được sửa chữa?
+ Trả lời: Hiệu chỉnh gamma có thể ảnh hưởng đến độ chính xác của phương trình tổng hợp (3.8) vì nó thay đổi mối quan hệ giữa cường độ ánh sáng và giá trị pixel đầu ra. Mối quan hệ này thường là phi tuyến tính và hiệu chỉnh gamma nhằm mục đích hiệu chỉnh nó. Do đó, khi ghép ảnh với các giá trị hiệu chỉnh gamma khác nhau, chúng ta cần điều chỉnh các giá trị pixel tương ứng để tính đến hiệu chỉnh gamma. Một cách để thực hiện việc này là áp dụng hiệu chỉnh gamma nghịch đảo cho các hình ảnh đầu vào trước khi thực hiện thao tác tổng hợp và sau đó áp dụng lại hiệu chỉnh gamma cho hình ảnh thu được.

2. Mô hình phụ gia (phản ánh thuần túy) có thể có những hạn chế. Điều gì xảy ra nếu kính bị nhuốm màu, đặc biệt là màu không xám? Làm thế nào nếu kính bị bẩn hoặc nhòe? Làm thế nào bạn có thể lập mô hình thủy tinh lượn sóng hoặc các loại vật thể khúc xạ khác?
+ Trả lời: Mô hình bổ sung giả định rằng ánh sáng phản xạ chỉ góp phần vào cường độ của điểm ảnh phản xạ và điều này có thể không đúng nếu kính bị pha màu. Kính màu sẽ ảnh hưởng đến màu sắc của ánh sáng phản xạ và chúng ta cần tính đến điều đó trong phương trình tổng hợp. Chúng ta có thể làm điều này bằng cách phân tách ánh sáng phản xạ thành các thành phần màu của nó và kết hợp từng thành phần riêng biệt. Nếu kính bị bẩn hoặc bị nhòe, nó sẽ tán xạ ánh sáng phản xạ và chúng ta cần mô hình hóa sự tán xạ này để thu được vật liệu tổng hợp chính xác. Chúng ta cũng có thể sử dụng các mô hình nâng cao hơn, chẳng hạn như phương trình Fresnel, để mô hình hóa thủy tinh gợn sóng hoặc các loại vật thể khúc xạ khác.

- input: input_bayer.jpg
- output: giao diện Tkinter và ảnh input đã lọc màu

