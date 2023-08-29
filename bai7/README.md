3.12 Sharpening, Blur and Noise removal

Cách chạy: cd vào thư mục bai7 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai7_sharpening_blur_noise_removal.py


Giải thích: 
+ Trong mã được cập nhật này, hàm apply_unsharp_mask áp dụng kỹ thuật mặt nạ không sắc nét, bao gồm làm mờ hình ảnh bằng bộ lọc Gaussian, sau đó trừ hình ảnh bị mờ khỏi ảnh gốc để tăng cường các cạnh và chi tiết. Tham số sigma kiểm soát mức độ mờ và tham số cường độ điều chỉnh cường độ của hiệu ứng làm sắc nét. Điều chỉnh các thông số này sẽ cho phép bạn tinh chỉnh hiệu ứng làm sắc nét theo ý thích của mình.

Hàm apply_bilateral_filter áp dụng bộ lọc song phương, giúp làm mờ hình ảnh một cách hiệu quả trong khi vẫn giữ nguyên các cạnh. Tham số d xác định đường kính của từng vùng lân cận pixel và tham số sigma_color và sigma_space kiểm soát ảnh hưởng của bộ lọc dựa trên độ tương tự màu và khoảng cách không gian. Điều chỉnh các thông số này sẽ giúp bạn đạt được hiệu ứng làm mờ và loại bỏ nhiễu mong muốn trong khi vẫn duy trì các chi tiết cạnh.

Vui lòng thử nghiệm với các giá trị tham số khác nhau cho mặt nạ không sắc nét và bộ lọc song phương để thu được kết quả tốt nhất cho hình ảnh và yêu cầu cụ thể của bạn.
- input: darkroom.jpg
- output: các bức ảnh với kết quả làm mờ, làm rõ nét

