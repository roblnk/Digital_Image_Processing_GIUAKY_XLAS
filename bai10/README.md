3.30 Image Denoising

Cách chạy: cd vào thư mục bai10 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai10_image_denoising.py


Giải thích thuật toán dùng trong bài: 

Hiệu suất của các thuật toán khử nhiễu có thể phụ thuộc vào ước tính chính xác của mức độ tiếng ồn. Trong chương trình được cung cấp, độ lệch chuẩn cố định được sử dụng để thêm nhiễu Gaussian, nhưng trên thực tế, việc ước tính mức độ nhiễu từ hình ảnh hoặc sử dụng kiến thức theo miền cụ thể có thể mang lại kết quả tốt hơn.
Việc lựa chọn kỹ thuật khử nhiễu phụ thuộc vào nhiều yếu tố khác nhau, chẳng hạn như bản chất của nhiễu, sự đánh đổi mong muốn giữa loại bỏ nhiễu và bảo toàn chi tiết cũng như độ phức tạp tính toán. Lọc Gaussian cung cấp khả năng làm mịn nhưng có thể làm mờ các chi tiết, trong khi Khử nhiễu phương tiện phi cục bộ bảo tồn các chi tiết tốt hơn nhưng có thể tốn kém về mặt tính toán. Bạn nên thử nghiệm các kỹ thuật và cài đặt tham số khác nhau để xác định xem cái nào hoạt động tốt hơn cho một tình huống cụ thể.
- input: chantroi.jpg
- output: hình ảnh được thay đổi kích thước lớn hơn dùng các thuật toán nearest, window_sinc và bilinear
