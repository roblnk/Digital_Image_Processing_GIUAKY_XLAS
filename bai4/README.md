3.6 Photo Effects

Cách chạy: cd vào thư mục bai4 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai4_photo_effects.py


Giải thích: 
    Hàm điều chỉnh độ tương phản lấy hình ảnh đầu vào và hệ số tương phản làm tham số và nó nhân từng giá trị pixel với hệ số tương phản để điều chỉnh độ tương phản của hình ảnh. Hàm apply_solarization lấy một hình ảnh đầu vào và một giá trị ngưỡng, đồng thời nó đảo ngược các giá trị pixel trên ngưỡng để đạt được hiệu ứng năng lượng mặt trời.

Bạn có thể điều chỉnh tham số contrast_factor để kiểm soát mức độ tăng cường độ tương phản. Giá trị cao hơn sẽ tăng độ tương phản, trong khi giá trị thấp hơn sẽ làm giảm độ tương phản. Tham số solarization_threshold xác định giá trị ngưỡng cho quá trình năng lượng mặt trời. Các pixel có giá trị cường độ trên ngưỡng này sẽ bị đảo ngược.

Vui lòng thử nghiệm các giá trị khác nhau cho hệ số tương phản và ngưỡng phơi nắng để đạt được các hiệu ứng và cải tiến ảnh khác nhau. Ngoài ra, bạn có thể khám phá và triển khai các bộ lọc và hiệu ứng khác, chẳng hạn như điều chỉnh độ sáng, phân loại màu, làm mờ nét ảnh, v.v., dựa trên các yêu cầu cụ thể và sở thích sáng tạo của bạn.
Thuật toán VNG đã được chứng minh là tạo ra kết quả chất lượng cao, đặc biệt đối với hình ảnh có độ nhiễu thấp và độ sắc nét cao. Tuy nhiên, nó có thể tương đối chậm so với các thuật toán giải mã khác do độ phức tạp tính toán của nó.

- input: input_image_cat.jpg
- output: giao diện Tkinter và ảnh input điều chỉnh độ tương phản và độ phơi nắng

